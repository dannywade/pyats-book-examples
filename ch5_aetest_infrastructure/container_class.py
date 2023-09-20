from pyats import aetest 
 
# Define a container and two subsections 
class MyCommonSetup(aetest.CommonSetup): 
    @aetest.subsection 
    def subsection_one(self): 
        self.a = 1 
        print("hello world") 
 
    @aetest.subsection 
    def subsection_two(self): 
        assert self.a == 1 
 
# Instantiate the class 
common_setup = MyCommonSetup() 
 
# Loop through to see what we get: 
for i in common_setup: 
    print(i)


# Example Output:
# subsection subsection_one
# subsection subsection_two