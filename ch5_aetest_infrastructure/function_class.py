from pyats import aetest 
 
 
class MyCommonSetup(aetest.CommonSetup): 
     
    # subsection corresponds to Subsection class 
    @aetest.subsection 
    def subsection_one(self): 
        pass 
 
class MyTestcase(aetest.Testcase): 
 
    # setup corresponds to SetupSection class 
    @aetest.setup 
    def setup(self): 
        pass 
 
    # test corresponds to TestSection class 
    @aetest.test 
    def test_one(self): 
        pass 
 
    # cleanup corresponds to CleanupSection class 
    @aetest.cleanup 
    def cleanup(self): 
        pass 
 
# When container instances are iterated, the returned objects are function 

# class instances 
tc = MyTestcase() 
for obj in tc: 
    print(type(obj)) 
    print(obj.function) 

 

# Example Output: 
# <class 'pyats.aetest.sections.SetupSection'>
# <bound method MyTestcase.setup of <class 'MyTestcase' uid='MyTestcase'>>
# <class 'pyats.aetest.sections.TestSection'>
# <bound method MyTestcase.test_one of <class 'MyTestcase' uid='MyTestcase'>>
# <class 'pyats.aetest.sections.CleanupSection'>
# <bound method MyTestcase.cleanup of <class 'MyTestcase' uid='MyTestcase'>>