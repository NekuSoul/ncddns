# ncddns

Dynamic DNS update client for domains hosted at netcup.

## Features

* Updates a single IPv4 DNS record based on the clients public IP address. 
* Only updates DNS record if the public IP has actually changed.
* Includes install script as well as systemd service and timer for periodical updates.

## Limitations

* Only works with IPv4

## Usage

### Requirements

* [Python 3](https://www.python.org/)

### How to use

* Grab the latest release.
* Create your personal API key and password through the netcup customer control panel.
* Create the DNS record you wish to update through the netcup customer control panel.
  This tool will not automatically create a new entry.
* Create a `ncddns.conf` file based on the provided example config.
* Run the client with python3: `python3 ncddns.py` or just `python ncddns.py` depending on your system.

### How to install on Linux

* Grab the latest release.
* Make the install script executable: `chmod u+x ./install.sh`.
* Run the install script as root: `sudo ./install.sh`.
* The application is now installed at `/opt/ncddns`.
* Make sure to create the `ncddns.conf` before you use the application.

### How to install the systemd timer

* Make sure the application is installed and configured correctly.
* Move into the directory of the installation script: `cd extras/systemd-timer`
* Make the install script executable: `chmod u+x ./install.sh`.
* Run the install script as root: `sudo ./install.sh`.
* The service `ncddns.service` and timer `ncddns.timer` are now installed and active.
* The timer will run every 15 minutes. If necessary, change this behaviour in `/etc/systemd/system/ncddns.timer`.