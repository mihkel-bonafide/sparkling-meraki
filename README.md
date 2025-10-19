This is an assortment of API-client scripts for the Meraki platform. Everything 
works as of 10/19/25.

get_devices.py: pulls a list of all devices associated with an org-ID and network-ID,
writes the output to meraki/devices.json

alt_get_devices.py: consolidated script that uses alternate syntax (try:except method) to
do the same as get_devices.py, only it creates meraki/devices.yaml 

get_clients.py: pulls a list of clients associated with a network-ID.

get_network_id.py: pulls the network-ID associated with an org-ID

get_org_id.py: pulls the org_id associated with a specific organization name (e.g. "DevNet Sandbox")

sans_sdk.py: consolidated script to pull a list of devices associated with a network-ID, 
only this one uses the requests library rather than the Meraki SDK (this is useful for those
of you studying for the DevNet Associate exam as you may be tested on, e.g., which endpoint
do you hit to pull a list of networks associated with an org ID). 
