from pyats.topology.loader import load

# Initialize and load testbed
testbed = load("../testbed.yaml")
# Identify device from testbed
xe_router = testbed.devices["cat8k-rt1"]

# Connect to device
xe_router.connect()
# Capture state of OSPF and Interface features before changes
pre_ospf = xe_router.learn("ospf")
pre_interface = xe_router.learn("interface")

### PERFORM CHANGES ###
input("Perform change! Press enter to continue...")

# Capture state of OSPF and Interface features after changes
post_ospf = xe_router.learn("ospf")
post_interface = xe_router.learn("interface")

# Disconnect from device
xe_router.disconnect()

# Diff OSPF and Interface snapshots
ospf_diff = pre_ospf.diff(post_ospf)
interface_diff = pre_interface.diff(post_interface)

# Compares snapshots - returns boolean
print(pre_ospf == post_ospf)  # False
print(pre_interface == post_interface)  # False

# Print diffs for OSPF and Interface features
print("OSPF DIFF:")
print(ospf_diff)
print("INTERFACE DIFF:")
print(interface_diff)

# Example Output:
# (notice state changes from full to exstart after change occurs - lines 102 and 103 - something broke!)
# OSPF DIFF:
#  info:
#   vrf:
#    default:
#     address_family:
#      ipv4:
#       instance:
#        10:
#         areas:
#          0.0.0.0:
#           database:
#            lsa_types:
#             1:
#              lsas:
#               10.254.1.1 10.254.1.1:
#                ospfv2:
#                 body:
#                  router:
#                   links:
# -                  172.16.1.0:
# -                   link_data: 255.255.255.0
# -                   link_id: 172.16.1.0
# -                   topologies:
# -                    0:
# -                     metric: 1
# -                     mt_id: 0
# -                   type: stub network
# +                  172.16.1.1:
# +                   link_data: 172.16.1.1
# +                   link_id: 172.16.1.1
# +                   topologies:
# +                    0:
# +                     metric: 1
# +                     mt_id: 0
# +                   type: transit network
#                 header:
# -                age: 6
# +                age: 18
# -                checksum: 0x5D88
# +                checksum: 0x83A4
# -                seq_num: 8000000F
# +                seq_num: 8000000E
#               10.254.1.2 10.254.1.2:
#                ospfv2:
#                 header:
# -                age: 87
# +                age: 19
#             2:
#              lsas:
#               172.16.1.1 10.254.1.1:
#                ospfv2:
#                 header:
# -                age: 3607
# +                age: 23
# -                checksum: 0x80D7
# +                checksum: 0x82D6
# -                seq_num: 80000002
# +                seq_num: 80000001
#           interfaces:
#            GigabitEthernet4:
# -           hello_timer: 00:00:05
# +           hello_timer: 00:00:07
#             neighbors:
#              10.254.1.2:
# -             dead_timer: 00:00:38
# +             dead_timer: 00:00:35
# -             state: exstart
# +             state: full
#               statistics:
# -              nbr_event_count: 21
# +              nbr_event_count: 18
# +           bdr_ip_addr: 172.16.1.2
# +           bdr_router_id: 10.254.1.2
#           statistics:
# -          area_scope_lsa_cksum_sum: 0x00C239
# +          area_scope_lsa_cksum_sum: 0x016B2B
# -          area_scope_lsa_count: 2
# +          area_scope_lsa_count: 3
# -          spf_runs_count: 17
# +          spf_runs_count: 16
# interface DIFF:
#  info:
#   GigabitEthernet1:
#    accounting:
#     arp:
# -    chars_in: 948
# +    chars_in: 874
# -    pkts_in: 13
# +    pkts_in: 12
#     ip:
# -    chars_in: 478390
# +    chars_in: 398037
# -    chars_out: 581408
# +    chars_out: 469554
# -    pkts_in: 5141
# +    pkts_in: 4311
# -    pkts_out: 5242
# +    pkts_out: 4349
#     ipv6:
# -    chars_in: 30499
# +    chars_in: 30241
# -    pkts_in: 125
# +    pkts_in: 122
#     other:
# -    chars_in: 948
# +    chars_in: 874
# -    pkts_in: 13
# +    pkts_in: 12
#    counters:
# -   in_octets: 454539
# +   in_octets: 370825
# -   in_pkts: 4724
# +   in_pkts: 3803
# -   out_octets: 524302
# +   out_octets: 409694
# -   out_pkts: 4739
# +   out_pkts: 3761
#     rate:
# -    in_rate_pkts: 1
# +    in_rate_pkts: 2
# -    out_rate: 1000
# +    out_rate: 2000
# -    out_rate_pkts: 1
# +    out_rate_pkts: 2
#   GigabitEthernet4:
#    accounting:
#     arp:
# -    chars_in: 420
# +    chars_in: 300
# -    chars_out: 420
# +    chars_out: 360
# -    pkts_in: 7
# +    pkts_in: 5
# -    pkts_out: 7
# +    pkts_out: 6
#     ip:
# -    chars_in: 29064
# +    chars_in: 26254
# -    chars_out: 21456
# +    chars_out: 19636
# -    pkts_in: 300
# +    pkts_in: 271
# -    pkts_out: 218
# +    pkts_out: 200
#     other:
# -    chars_in: 420
# +    chars_in: 300
# -    chars_out: 420
# +    chars_out: 360
# -    pkts_in: 7
# +    pkts_in: 5
# -    pkts_out: 7
# +    pkts_out: 6
#    counters:
# -   in_octets: 21190
# +   in_octets: 19282
# -   in_pkts: 220
# +   in_pkts: 200
# -   out_octets: 21712
# +   out_octets: 19882
# -   out_pkts: 223
# +   out_pkts: 205
#   Loopback0:
#    accounting:
#     ip:
# -    chars_in: 7520
# +    chars_in: 6744
# -    chars_out: 7520
# +    chars_out: 6744
# -    pkts_in: 94
# +    pkts_in: 84
# -    pkts_out: 94
# +    pkts_out: 84
#    counters:
# -   out_octets: 7448
# +   out_octets: 6744
# -   out_pkts: 93
# +   out_pkts: 84
#   Loopback1:
#    accounting:
#     ip:
# -    chars_in: 7520
# +    chars_in: 6744
# -    chars_out: 7520
# +    chars_out: 6744
# -    pkts_in: 94
# +    pkts_in: 84
# -    pkts_out: 94
# +    pkts_out: 84
#    counters:
# -   out_octets: 7448
# +   out_octets: 6744
# -   out_pkts: 93
# +   out_pkts: 84
