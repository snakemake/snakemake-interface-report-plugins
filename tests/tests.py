from typing import List
from snakemake_interface_report_plugins.registry import ReportPluginRegistry
from snakemake_interface_common.plugin_registry.tests import TestRegistryBase
from snakemake_interface_common.plugin_registry.plugin import PluginBase, SettingsBase
from snakemake_interface_common.plugin_registry import PluginRegistryBase
from snakemake_interface_report_plugins.logging import LoggingReportInterface
from snakemake_interface_report_plugins.reporter import ReporterBase
from snakemake_interface_report_plugins.settings import ExecMode, ReportSettingsBase

from snakemake.report import html_reporter


class TestRegistry(TestRegistryBase):
    __test__ = True

    def get_registry(self) -> PluginRegistryBase:
        # ensure that the singleton is reset
        ReportPluginRegistry._instance = None
        registry = ReportPluginRegistry()
        registry.register_plugin("html", html_reporter)

        # Keep only the "html" plugin so that collect_plugins() auto-discovered
        # locally installed plugins (e.g. snakemake-report-plugin-nanopub) do
        # not leak into tests that assert a specific cli_prefix.
        registry.plugins = {
            name: plugin for name, plugin in registry.plugins.items() if name == "html"
        }

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


class TestLogger(LoggingReportInterface):
    def info(self, msg: str) -> None:
        pass

    def error(self, msg: str) -> None:
        pass

    def debug(self, msg: str) -> None:
        pass

    def warning(self, msg: str) -> None:
        pass


class ReporterForTest(ReporterBase):
    def get_exec_mode(self) -> ExecMode:
        return ExecMode.DEFAULT

    def render(self):
        return None


def test_reporter_base_exposes_logger():
    logger = TestLogger()
    reporter = ReporterForTest(
        rules={},
        results={},
        logger=logger,
        configfiles=[],
        jobs=[],
        settings=ReportSettingsBase(),
        workflow_description="",
        dag=None,
    )

    assert reporter.logger is logger
