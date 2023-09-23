from pyats import aetest


class TestcaseOne(aetest.Testcase):
    """Testcase One"""

    groups = ["traffic"]

    @aetest.test
    def test1(self):
        """Code for first test"""
        pass

    @aetest.test
    def test2(self):
        """Code for second test"""
        pass

    @aetest.cleanup
    def testcase_cleanup(self):
        """Code to cleanup config on testbed devices"""
        pass


class TestcaseTwo(aetest.Testcase):
    """Testcase One"""

    groups = ["sanity"]

    @aetest.test
    def test1(self):
        """Code for first test"""
        pass

    @aetest.test
    def test2(self):
        """Code for second test"""
        pass

    @aetest.cleanup
    def testcase_cleanup(self):
        """Code to cleanup config on testbed devices"""
        pass
