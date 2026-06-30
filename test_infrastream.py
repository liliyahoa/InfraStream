# test_infrastream.py
"""
Tests for InfraStream module.
"""

import unittest
from infrastream import InfraStream

class TestInfraStream(unittest.TestCase):
    """Test cases for InfraStream class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = InfraStream()
        self.assertIsInstance(instance, InfraStream)
        
    def test_run_method(self):
        """Test the run method."""
        instance = InfraStream()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
