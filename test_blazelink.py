# test_blazelink.py
"""
Tests for BlazeLink module.
"""

import unittest
from blazelink import BlazeLink

class TestBlazeLink(unittest.TestCase):
    """Test cases for BlazeLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlazeLink()
        self.assertIsInstance(instance, BlazeLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlazeLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
