from pyats import aetest 


class Testcase(aetest.Testcase): 
 
    # associating this testcase to 2 separate groups 
    groups = ["routing", "bgp"] 

if __name__ == "__main__":
    aetest.main()