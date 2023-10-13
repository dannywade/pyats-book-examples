from jinja2 import Environment, FileSystemLoader, FileSystemLoader, select_autoescape
import yaml

from interface_data import SINGLE_INTERFACE, ALL_INTERFACES

env = Environment(
    loader=FileSystemLoader("config_templates"),
    autoescape=select_autoescape(),
)

# Get J2 template for single interface config
SINGLE_INTERFACE_TMPL = env.get_template("single_interface.j2")
# Get J2 template for all interfaces
ALL_INTERFACES_TMPL = env.get_template("all_interfaces.j2")

### RENDER WITH PYTHON DICTS ###
# Render single interface config
single_interface_cfg = SINGLE_INTERFACE_TMPL.render(interface=SINGLE_INTERFACE)
print("*" * 20 + " Single Interface with Python dict " + "*" * 20)
print(single_interface_cfg)

# Render config for all interfaces
all_interfaces_cfg = ALL_INTERFACES_TMPL.render(interfaces=ALL_INTERFACES)
print("*" * 20 + " All Interfaces with Python dict " + "*" * 20)
print(all_interfaces_cfg)

### RENDER WITH YAML FILE ###
# Load YAML file into Python object
with open("interfaces.yaml", encoding="utf-8") as f:
    interface_config = yaml.safe_load(f.read())

# Render single interface config (only GigabitEthernet1)
single_interface_cfg = SINGLE_INTERFACE_TMPL.render(interface=interface_config[0])
print("*" * 20 + " Single Interface with YAML File " + "*" * 20)
print(single_interface_cfg)

# Render config for all interfaces
all_interfaces_cfg = ALL_INTERFACES_TMPL.render(interfaces=interface_config)
print("*" * 20 + " All Interfaces with YAML File " + "*" * 20)
print(all_interfaces_cfg)
