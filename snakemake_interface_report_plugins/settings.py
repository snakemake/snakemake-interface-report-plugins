__author__ = "Johannes Köster"
__copyright__ = "Copyright 2024, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

from dataclasses import dataclass

from snakemake_interface_common.settings import SettingsEnumBase

import snakemake_interface_common.plugin_registry.plugin


class ExecMode(SettingsEnumBase):
    """
    Enum for execution mode of Snakemake
    This handles the behavior of e.g. the logger
    """

    DEFAULT = 0
    SUBPROCESS = 1
    REMOTE = 2


@dataclass
class ReportSettingsBase(
    snakemake_interface_common.plugin_registry.plugin.SettingsBase
):
    pass
