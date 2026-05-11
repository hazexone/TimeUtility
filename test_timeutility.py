# test_timeutility.py
"""
Tests for TimeUtility module.
"""

import unittest
from timeutility import TimeUtility

class TestTimeUtility(unittest.TestCase):
    """Test cases for TimeUtility class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TimeUtility()
        self.assertIsInstance(instance, TimeUtility)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TimeUtility()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
