#!/bin/env python

import meraki
from lehost import MERAKI_DASHBOARD_API_KEY as lekey
ORGANIZATION_NAME = "DevNet Sandbox"

dashboard = meraki.DashboardAPI(lekey)
organizations = dashboard.organizations.getOrganizations()  # get list of organizations 
# import json; print(json.dumps(organizations, indent=4))  # check output
"""
A successful result here will yeild the organization name and ID we need for future API calls. 
"""
for org in organizations:
    if org['name'] == ORGANIZATION_NAME:
        org_id = org['id']
        print(f"Found {ORGANIZATION_NAME} with ID {org_id}")
        break       
    


# print(org_id)
# devices = dashboard.organizations.getOrganizationDevices(org_id)
# print(devices)  # if I convert this to JSON can I get rid of all this header garbage???


