# test_hyperwaveform.py
"""
Tests for HyperWaveform module.
"""

import unittest
from hyperwaveform import HyperWaveform

class TestHyperWaveform(unittest.TestCase):
    """Test cases for HyperWaveform class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HyperWaveform()
        self.assertIsInstance(instance, HyperWaveform)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HyperWaveform()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
