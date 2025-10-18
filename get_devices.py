#!/bin/env python
"""
Get Meraki devices for a specific network and save to JSON file.

"""
import meraki
import json
from lehost import MERAKI_DASHBOARD_API_KEY as lekey
from get_org_id import get_org_id
from get_network_id import get_network_id   


def devices():
    dashboard = meraki.DashboardAPI(api_key=lekey, 
                                    output_log=False,
                                    print_console=False)
    # Get organization ID and network ID
    organization_id = get_org_id()
    network_id = get_network_id(organization_id) 

    # Get devices for the network
    devices = dashboard.networks.getNetworkDevices(network_id)

    # Write device info to a JSON file
    with open('devices_output.json', 'w') as dev_file:
        json.dump(devices, dev_file, indent=3)
    
def main():
    devices()
      

if __name__ == "__main__":
    main()      
