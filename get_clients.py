#!/bin/env python
"""
Obtain a list of clients using the Meraki Dashboard API.
Write the output to a JSON file called 'clients.json'.

"""
import meraki
import json
from lehost import MERAKI_DASHBOARD_API_KEY as lekey
from get_org_id import get_org_id
from get_network_id import get_network_id   


def get_clients():
    dashboard = meraki.DashboardAPI(api_key=lekey, 
                                    output_log=False,
                                    print_console=False)
    # Get organization ID and network ID
    organization_id = get_org_id()
    network_id = get_network_id(organization_id) 

    # this request is time-bounded; 86400 seconds = 24 hours
    timespan = 86400

    # Get clients for the network
    clients = dashboard.networks.getNetworkClients(network_id, timespan)
    """
    If you're running this on the Always On DevNet Sandbox, it will likely 
    return an empty list.
    """
    # Write device info to a JSON file
    with open('clients.json', 'w') as client_file:
        json.dump(clients, client_file, indent=3)
    
def main():
    get_clients()
      

if __name__ == "__main__":
    main()      