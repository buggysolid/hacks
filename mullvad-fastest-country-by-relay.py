import requests
import socket
from ping3 import ping, verbose_ping
import operator

def get_ip_address(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        print(f'Error resolving hostname. {hostname}')

def ping_ip(ip_address):
    try:
        return ping(ip_address)
    except Exception as e:
        print(f'Error pinging IP. {ip_address}')

API_REQUEST='https://api.mullvad.net/www/relays/all'
response = requests.get(API_REQUEST)
hostnames_to_check = []

for relay in response.json():
    if relay.get('owned') == True:
        hostname = relay.get('fqdn')
        hostnames_to_check.append(hostname)

results = []
for hostname in hostnames_to_check:
    ip_address = get_ip_address(hostname)
    if ip_address:
        latency = ping_ip(ip_address)
        if latency:
            results.append((hostname, ip_address, latency))

results.sort(key=operator.itemgetter(2), reverse=True)

for hostname, ip_address, latency in results:
    print(f'Hostname: {hostname}, IP address: {ip_address}, Latency: {latency} ms')

