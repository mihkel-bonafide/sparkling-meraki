#!/bin/env python

import meraki
from lehost import MERAKI_DASHBOARD_API_KEY as lekey
ORGANIZATION_NAME = "DevNet Sandbox"

def get_org_id():
    # create dashboard object
    dashboard = meraki.DashboardAPI(api_key=lekey, 
                                    output_log=False, 
                                    print_console=False)
    organizations = dashboard.organizations.getOrganizations()  # get list of organizations 
    for org in organizations:
        if org['name'] == ORGANIZATION_NAME:
            org_id = org['id']
            print(f"Organization ID for '{ORGANIZATION_NAME}' is: {org_id}")  # this is to verify it works
            return org_id
    return None


def main():
    get_org_id()


if __name__ == "__main__":
    main()  
