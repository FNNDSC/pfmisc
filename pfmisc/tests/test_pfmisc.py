from unittest import TestCase

from pfmisc import pfmisc

class TestPfmisc(TestCase):
    def test_pfmisc_constructor(self):
        myMan = pfmisc()
        # didn't crash
        self.assertTrue(True)
