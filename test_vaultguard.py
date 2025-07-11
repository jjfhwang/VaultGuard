# test_vaultguard.py
"""
Tests for VaultGuard module.
"""

import unittest
from vaultguard import VaultGuard

class TestVaultGuard(unittest.TestCase):
    """Test cases for VaultGuard class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VaultGuard()
        self.assertIsInstance(instance, VaultGuard)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VaultGuard()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
