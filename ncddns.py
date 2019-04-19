#!/usr/bin/env python3

import configparser
import os
import re

import requests

import netcupapi

# Read config file
configfile = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ncddns.conf')
config = configparser.ConfigParser()
config.read(configfile)
apikey = config['ncddns']['apikey']
apipassword = config['ncddns']['apipassword']
customernumber = config['ncddns']['customernumber']
domainname = config['ncddns']['domainname']
hostname = config['ncddns']['hostname']
ipcheckurl = config['ncddns']['ipcheckurl']

# Get public ip
response = requests.get(ipcheckurl)
if response.status_code != 200:
    raise Exception

match = re.search(r"\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3}", response.text)
if match is None:
    raise Exception

publicip = match.string

lastip = None

# Quit if public ip hasn't changed
try:
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lastip'), 'r') as ipfile:
        lastip = ipfile.read()
except FileNotFoundError:
    pass

if publicip == lastip:
    exit()

# Login to netcup API
netcupapi.login(apikey, apipassword, customernumber)
result = netcupapi.info_dns_record(domainname)

# Get DNS record that should be updated
recordid = None
for record in result['responsedata']['dnsrecords']:
    if record['hostname'] == hostname:
        recordid = record['id']
        break

if recordid is None:
    raise Exception

# Update DNS record with new IP
netcupapi.update_dns_record(domainname, recordid, hostname, 'A', publicip)
netcupapi.logout()

# Update last public ip record
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lastip'), 'w') as ipfile:
    ipfile.write(publicip)

