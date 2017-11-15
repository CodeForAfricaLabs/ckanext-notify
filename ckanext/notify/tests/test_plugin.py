"""Tests for plugin.py."""
from mock import MagicMock
import ckanext.notify.plugin as plugin
import unittest


class TestNotifyPlugin(unittest.TestCase):
    def setUp(self):
        """Create Instances"""
        self.notify = plugin.NotifyPlugin()

    def test_update_config(self):
        """Test that CKAN uses the plugin's custom templates."""
        self._toolkit = plugin.toolkit
        plugin.toolkit = MagicMock()
        config = MagicMock()
        self.notify.update_config(config)
        plugin.toolkit.add_template_directory.assert_called_once_with(config, 'templates')
        plugin.toolkit = self._toolkit

    def test_get_actions(self):
        actions = self.notify.get_actions()
        self.assertEqual(type(actions), dict)

    def test_get_auth_functions(self):
        auth_functions = self.notify.get_auth_functions()
        self.assertEqual(type(auth_functions), dict)


if __name__ == "__main__":
    unittest.main(verbosity=2)
