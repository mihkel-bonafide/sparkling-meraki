#!/bin/env python

import meraki
from lehost import MERAKI_DASHBOARD_API_KEY as lekey
from get_org_id import get_org_id as org_id


def get_network_id(org_id):
    dashboard = meraki.DashboardAPI(lekey)
    org_id = org_id()
    networks = dashboard.organizations.getOrganizationNetworks(org_id)
    for net in networks:
        if net['organizationId'] == org_id:
            net_id = net['id']
            print(f"Network ID for organization ID '{org_id}' is: {net_id}")  # this is to verify it works
            return net_id   
        return None 
    
def main():
    get_network_id(org_id)   


if __name__ == "__main__":
    main()      
