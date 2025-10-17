#!/bin/env python

import meraki
from lehost import MERAKI_DASHBOARD_API_KEY as lekey
ORGANIZATION_NAME = "DevNet Sandbox"

def get_org_id():
    dashboard = meraki.DashboardAPI(lekey)
    organizations = dashboard.organizations.getOrganizations()  # get list of organizations 
    for org in organizations:
        if org['name'] == ORGANIZATION_NAME:
            org_id = org['id']
            print(f"Organization ID for '{ORGANIZATION_NAME}' is: {org_id}")
            return org_id
    return None


def main():
    get_org_id()


if __name__ == "__main__":
    main()  
