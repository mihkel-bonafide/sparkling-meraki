#!/bin/env python
"""
IMPORTANT NOTE!!
The documentation at developer.cisco is flat out incorrect as to how device info is returned via the Meraki Dashboard API.

For reference, see: https://developer.cisco.com/meraki/api-v1/getting-started/#find-your-devices-and-their-serials
^^^ this is wrong. 
Their version: 
response = dashboard.organizations.getOrganizationDevices({organizationId})  # this will 404-error you all day
Correct version: 
response = dashboard.networks.getNetworkDevices(organizationId) 

Pay particular note of the fact that the SDK's negotiated path here is dashboard.networks, not dashboard.organizations.
There has GOT to be better documentation for this somewhere, just not with Cisco, apparently.  10/16 MG 

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
