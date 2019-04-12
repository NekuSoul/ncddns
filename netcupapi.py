import requests
import json

_endpoint = 'https://ccp.netcup.net/run/webservice/servers/endpoint.php?JSON'
_apikey = None
_apisessionid = None
_customernumber = None


def login(apikey, apipassword, customernumber):
    global _apikey
    global _apisessionid
    global _customernumber

    data = {
        'action': 'login',
        'param': {
            'apikey': apikey,
            'apipassword': apipassword,
            'customernumber': customernumber
        }
    }

    result = _execute(data)
    _apikey = apikey
    _customernumber = customernumber
    _apisessionid = result['responsedata']['apisessionid']
    return result


def logout():
    global _apikey
    global _apisessionid
    global _customernumber

    data = {
        'action': 'logout',
        'param': {
            'apikey': _apikey,
            'apisessionid': _apisessionid,
            'customernumber': _customernumber
        }
    }

    result = _execute(data)
    _apikey = None
    _customernumber = None
    _apisessionid = None
    return result


def update_dns_record(domainname, recordid, hostname, recordtype, destination):
    data = {
        'action': 'updateDnsRecords',
        'param': {
            'apikey': _apikey,
            'apisessionid': _apisessionid,
            'customernumber': _customernumber,
            'dnsrecordset': {
                'dnsrecords': [
                    {
                        'id': recordid,
                        'hostname': hostname,
                        'type': recordtype,
                        'destination': destination
                    }
                ]
            },
            'domainname': domainname
        }
    }
    result = _execute(data)
    return result


def info_dns_record(domainname):
    data = {
        'action': 'infoDnsRecords',
        'param': {
            'apikey': _apikey,
            'apisessionid': _apisessionid,
            'customernumber': _customernumber,
            'domainname': domainname
        }
    }
    result = _execute(data)
    return result


def _execute(data):
    response = requests.post(_endpoint, json=data)
    if response.status_code != 200:
        raise Exception
    result = json.loads(response.text)
    if result['status'] != 'success':
        raise Exception
    return result
