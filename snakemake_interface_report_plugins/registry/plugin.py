__author__ = "Johannes Köster"
__copyright__ = "Copyright 2024, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

from dataclasses import dataclass
from typing import Optional, Type
from snakemake_interface_report_plugins.settings import (
    ReportSettingsBase,
)
from snakemake_interface_report_plugins import common

from snakemake_interface_common.plugin_registry.plugin import PluginBase


@dataclass
class Plugin(PluginBase):
    reporter: object
    _report_settings_cls: Optional[Type[ReportSettingsBase]]
    _name: str

    @property
    def name(self):
        return self._name

    @property
    def cli_prefix(self):
        return "report-" + self.name.replace(common.report_plugin_module_prefix, "")

    @property
    def settings_cls(self):
        return self._report_settings_cls
