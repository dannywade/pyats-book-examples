from pyats.topology.loader import load

# Initialize and load testbed
testbed = load("../testbed.yaml")
# Identify device from testbed
xe_router = testbed.devices["cat8k-rt1"]

# Connect to device, learn BGP feature, and disconnect from the device
xe_router.connect()
bgp_state = xe_router.learn("bgp")
xe_router.disconnect()

# Print BGP feature output
print(bgp_state.info)

# Example Output:
# {'instance': {'default': {'bgp_id': 65000, 'vrf': {'default': {'cluster_id': '10.254.1.1', 'neighbor': {'172.16.1.2': {'remote_as': 65001, 'shutdown': False, 'bgp_version': 4, 'session_state': 'Established', 'bgp_negotiated_keepalive_timers': {'keepalive_interval': 60, 'hold_time': 180}, 'bgp_session_transport': {'connection': {'state': 'Established', 'last_reset': 'never'}, 'transport': {'local_port': '179', 'local_host': '172.16.1.1', 'foreign_port': '18680', 'foreign_host': '172.16.1.2', 'mss': 1460}}, 'bgp_negotiated_capabilities': {'route_refresh': 'advertised and received(new)', 'four_octets_asn': 'advertised and received', 'enhanced_refresh': 'advertised and received', 'stateful_switchover': 'NO for session 1'}, 'bgp_neighbor_counters': {'messages': {'sent': {'opens': 1, 'updates': 2, 'notifications': 0, 'keepalives': 7}, 'received': {'opens': 1, 'updates': 2, 'notifications': 0, 'keepalives': 7}}}, 'address_family': {'ipv4 unicast': {'bgp_table_version': 3, 'routing_table_version': 3, 'prefixes': {'total_entries': 2, 'memory_usage': 496}, 'path': {'total_entries': 2, 'memory_usage': 272}, 'total_memory': 1384}}}}}}}}}
