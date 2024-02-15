__author__ = "Johannes Köster"
__copyright__ = "Copyright 2024, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"


from abc import ABC, abstractmethod
from typing import List, Mapping
from snakemake_interface_report_plugins.interfaces import (
    CategoryInterface,
    ConfigFileRecordInterface,
    JobRecordInterface,
    RuleRecordInterface,
)
from snakemake_interface_report_plugins.settings import ReportSettingsBase
from snakemake_interface_report_plugins.interfaces import DAGReportInterface


class ReporterBase(ABC):
    def __init__(
        self,
        rules: Mapping[str, RuleRecordInterface],
        results: Mapping[
            CategoryInterface, Mapping[CategoryInterface, List[RuleRecordInterface]]
        ],
        configfiles: List[ConfigFileRecordInterface],
        jobs: List[JobRecordInterface],
        settings: ReportSettingsBase,
        workflow_description: str,
        dag: DAGReportInterface,
    ):
        self.rules = rules
        self.jobs = jobs
        self.results = results
        self.configfiles = configfiles
        self.settings = settings
        self.workflow_description = workflow_description
        self.dag = dag

        self.__post_init__()

    def __post_init__(self):
        pass

    @abstractmethod
    def render(self): ...
