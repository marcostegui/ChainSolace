# test_chainsolace.py
"""
Tests for ChainSolace module.
"""

import unittest
from chainsolace import ChainSolace

class TestChainSolace(unittest.TestCase):
    """Test cases for ChainSolace class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = ChainSolace()
        self.assertIsInstance(instance, ChainSolace)

    def test_run_method(self):
        """Test the run method."""
        instance = ChainSolace()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
