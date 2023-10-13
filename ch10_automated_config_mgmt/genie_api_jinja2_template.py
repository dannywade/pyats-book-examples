from pyats.topology.loader import load

# Load testbed and select “cat8k-rt1” device
my_testbed = load("testbed.yaml")
xe_router = my_testbed.devices["cat8k-rt1"]

# Render config with load_jinja_template() device API
logging_config = xe_router.api.load_jinja_template(
    path="config_templates", file="ios_logging.j2", hosts=["10.1.1.1", "10.1.1.2"]
)

# Print rendered config
print(logging_config)
