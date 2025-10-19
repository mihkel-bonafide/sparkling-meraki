#!/bin/env python

"""
Consolidated module to list all devices in all networks of a specified Meraki organization.
Prints and writes selected output to meraki/devices.yaml.

""" 

import meraki
import os
import yaml

# API Configuration
from lehost import MERAKI_DASHBOARD_API_KEY as API_KEY
ORGANIZATION_NAME = "DevNet Sandbox"

def list_devices():  
    # print a statement that amounts to: why are we here?
    print(f"This is a list of devices for organization: {ORGANIZATION_NAME}")
    # Initialize the Meraki dashboard
    dashboard = meraki.DashboardAPI(
        api_key=API_KEY,
        output_log=False,
        print_console=False
    )
    
    try:
        # Get all organizations
        organizations = dashboard.organizations.getOrganizations()
     
        # assign your organization ID to "org_id"
        org_id = None
        for org in organizations:
            if org["name"] == ORGANIZATION_NAME:
                org_id = org["id"]
                break
        
        if not org_id:
            print(f"Could not find organization: {ORGANIZATION_NAME}")
            return
            
        print(f"Your organization ID: {org_id}")
        
        # Get all networks for the organization
        networks = dashboard.organizations.getOrganizationNetworks(org_id)
        
        # Get and display devices for each network
        for network in networks:
            print(f"\nDevices in network: {network['name']}")
            
            try:
                devices = dashboard.networks.getNetworkDevices(network['id'])
                
                for device in devices:
                    # Additional device details can be written or printed as needed
                    print(f"- {device.get('name', 'Unnamed Device')} ({device['model']})")
                    print(f"  Serial: {device['serial']}")
                    print(f"  MAC: {device['mac']}")
                    print(f"  Firmware: {device.get('firmware', 'N/A')}")
                    print(f"  Status: {'Online' if device.get('status') == 'online' else 'Offline'}")
                    
                    # writes to meraki/devices.yaml
                    device_entry = {
                        "organization": ORGANIZATION_NAME,
                        "organization_id": org_id,
                        "network": {"id": network["id"], "name": network.get("name")},
                        "device": {
                            "name": device.get("name", "Unnamed Device"),
                            "model": device.get("model"),
                            "serial": device.get("serial"),
                            "mac": device.get("mac"),
                            "firmware": device.get("firmware", "N/A"),
                            "status": "Online" if device.get("status") == "online" else "Offline",
                        },
                    }

                    out_path = os.path.join(os.path.dirname(__file__), "devices.yaml")
                    with open(out_path, "a", encoding="utf-8") as f:
                        f.write("---\n")
                        yaml.safe_dump(device_entry, f, sort_keys=False, default_flow_style=False, allow_unicode=True)
            except meraki.APIError as e:
                print(f"Error fetching devices for network {network['name']}: {str(e)}")
                
    except meraki.APIError as e:
        print(f"Error accessing Meraki Dashboard: {str(e)}")


def main():
    list_devices()


if __name__ == "__main__":
    main() 
    