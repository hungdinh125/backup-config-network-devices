#!/usr/bin/python3

# This script is to save the running config to start-up config, then upload the file to Chengdu FTP server
# Usage python3 backup-config.py
# Chengdu FTP server: 10.133.10.115
# Username/Password: apacftp / P@ssw0rd

from netmiko import ConnectHandler
import jinja2
import yaml
import datetime

# Retrieve device information from YAML file
with open("device_list.yaml", "r") as f:
    all_devices = yaml.safe_load(f)

# Generate the commands template and push to device
for device_info in all_devices['devices']:
    device_name, device_config = device_info.popitem()
    current_date = datetime.datetime.now().strftime("%m%d%Y")
    # Render the commands from Jinja template
    with open("configuration_commands.j2", "r") as k:
        template_data = k.read()
    template = jinja2.Template(template_data)
    template_output = template.render(device_name=device_name, current_date=current_date)
    
    # Save the commans to text file
    with open("backup_commands", "w") as h:
        h.write(template_output)

    # Start the backup
    print(f"***Connecting to " + device_name)
    device_connect = ConnectHandler(**device_config, global_cmd_verify=False)
    device_connect.enable()
    device_connect.debug = True
    commands = template_output.strip().split("\n")
    for command in commands:
        print(command)
        apply_config = device_connect.send_command_timing(command)
#       if "Destination filename" in apply_config:
#           apply_config = device_connect.send_command_timing("\n")
#    apply_config = device_connect.send_config_from_file('backup_commands')
        print(apply_config)
    print("-" * 30)
    device_connect.disconnect()