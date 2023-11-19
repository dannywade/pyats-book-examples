from pyats.topology.loader import load


def verify_ospf_state(obj, process_id, router_id):
    # Obj is the feature object which is being learnt
    # Confirm learned process ID and router ID are correct
    assert (
        obj.info["vrf"]["default"]["address_family"]["ipv4"]["instance"][process_id][
            "router_id"
        ]
        == router_id
    )


# Load testbed and connect to 'cat8k-rt1' device
testbed = load("../testbed.yaml")
xe_router = testbed.devices["cat8k-rt1"]
xe_router.connect()

# Learn OSPF feature from device
ospf = xe_router.learn("ospf")

# Learn OSPF and confirm the process ID and corresponding router ID are correct
# using the verify_ospf_state function. It will try up to 5 times,
# and sleep 10 seconds between each attempt.
ospf.learn_poll(
    verify=verify_ospf_state,
    sleep=10,
    attempt=5,
    process_id="10",
    router_id="10.254.1.1",
)

print("Feature verified - Polling was a success!")

# Disconnect from device
xe_router.disconnect()
