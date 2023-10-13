from genie import testbed

# Load testbed and select “router1” device
my_testbed = testbed.load("testbed.yaml")
xe_router = my_testbed.devices["cat8k-rt1"]

# Configuration is rendered and pushed to “router1” device
logging_config = xe_router.api.configure_by_jinja2(
    path="config_templates", file="ios_logging.j2", hosts=["10.1.1.1", "10.1.1.2"]
)
