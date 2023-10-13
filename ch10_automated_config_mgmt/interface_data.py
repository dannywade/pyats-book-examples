"""Parameters for rendering interface configurations"""

SINGLE_INTERFACE = {
    "name": "GigabitEthernet1",
    "description": "WAN Link",
    "ip_address": "10.100.1.10",
    "mask": "255.255.255.252",
    "active": True,
}


ALL_INTERFACES = [
    {
        "name": "GigabitEthernet1",
        "description": "WAN Link",
        "ip_address": "10.100.1.10",
        "mask": "255.255.255.252",
        "active": True,
    },
    {
        "name": "GigabitEthernet2",
        "description": "Server Switch",
        "ip_address": "10.100.10.1",
        "mask": "255.255.255.0",
        "active": True,
    },
    {
        "name": "GigabitEthernet3",
        "description": "Firewall",
        "ip_address": "10.100.20.1",
        "mask": "255.255.255.0",
        "active": False,
    },
    {
        "name": "GigabitEthernet4",
        "description": "User Access Switch",
        "ip_address": "10.100.30.1",
        "mask": "255.255.255.0",
        "active": True,
    },
]