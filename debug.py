#!/bin/env python

import meraki
from lehost import MERAKI_DASHBOARD_API_KEY as lekey
ORGANIZATION_NAME = "DevNet Sandbox"

def get_org_id():
    dashboard = meraki.DashboardAPI(lekey)
    organizations = dashboard.organizations.getOrganizations()  # get list of organizations 
    # import json; print(json.dumps(organizations, indent=4))  # check output

    """
    A successful result here will yeild the organization name and ID we need for future API calls. 
    """
    for org in organizations:
        if org['name'] == ORGANIZATION_NAME:
            org_id = org['id']
            print(f"bro I found {ORGANIZATION_NAME} with ID {org_id}")
            get_networks(org_id)

def get_networks(org_id):
    dashboard = meraki.DashboardAPI(lekey)
    networks = dashboard.organizations.getOrganizationNetworks(org_id)
    import json; print(json.dumps(networks, indent=4))  # check output

    """
    A successful result here will produce a list of dictionary objects which comprise the networks associated with that org ID. 
    """

def main(): 
    get_org_id()

if __name__ == "__main__":
    main()  


