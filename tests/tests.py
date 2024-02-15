from typing import List
from snakemake_interface_report_plugins.registry import ReportPluginRegistry
from snakemake_interface_common.plugin_registry.tests import TestRegistryBase
from snakemake_interface_common.plugin_registry.plugin import PluginBase, SettingsBase
from snakemake_interface_common.plugin_registry import PluginRegistryBase

from snakemake.report import html_reporter


class TestRegistry(TestRegistryBase):
    __test__ = True

    def get_registry(self) -> PluginRegistryBase:

        # ensure that the singleton is reset
        ReportPluginRegistry._instance = None
        registry = ReportPluginRegistry()
        registry.register_plugin("html", html_reporter)

        return registry

    def get_test_plugin_name(self) -> str:
        return "html"

    def validate_plugin(self, plugin: PluginBase):
        assert plugin._report_settings_cls is not None
        assert plugin.reporter is not None

    def validate_settings(self, settings: SettingsBase, plugin: PluginBase):
        assert isinstance(settings, plugin._report_settings_cls)

    def get_example_args(self) -> List[str]:
        return ["--report-html-path", "report.zip"]
