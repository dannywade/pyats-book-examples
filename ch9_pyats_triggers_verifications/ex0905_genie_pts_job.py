from genie.harness.main import gRun 
 
# To run job: pyats run job ex0905_genie_pts_job.py --testbed-file testbed.yaml

# NOTE: A testbed device must be named or have an alias of 'uut'. Otherwise, a trigger and/or verification datafile must be included in gRun args

def main(): 
 
    # Profiling built-in features (models)
    gRun(pts_features=["bgp", "interface"],
        pts_datafile="ex0906_pts_datafile.yaml")






### SAMPLE OUTPUT ###
