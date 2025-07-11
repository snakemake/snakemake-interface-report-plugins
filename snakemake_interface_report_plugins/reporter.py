__author__ = "Johannes Köster"
__copyright__ = "Copyright 2024, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"


from abc import ABC, abstractmethod
from typing import List, Mapping, Dict, Optional, Union
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
        metadata: Optional[
            Dict[str, Union[str, int, float, List[str], List[int], List[float]]]
        ] = {},
    ):
        self.rules = rules
        self.jobs = jobs
        self.results = results
        self.configfiles = configfiles
        self.settings = settings
        self.workflow_description = workflow_description
        self.dag = dag

        # ensure that metadata is a key value dictionary
        if not validate_flat_dict(metadata):
            raise TypeError(
                (
                    "Metadata must be single level "
                    "dict[str, str | int | float | list[str] | list[int] | list[float]]]"
                )
            )

        self.metadata = metadata

        self.__post_init__()

    def __post_init__(self):
        pass

    @abstractmethod
    def render(self): ...


def is_valid_flat_value(value) -> bool:
    if isinstance(value, (str, int, float)):
        return True
    elif isinstance(value, list):
        return all(isinstance(item, (str, int, float)) for item in value)
    else:
        return False


def validate_flat_dict(metadata: dict) -> bool:
    if not isinstance(metadata, dict):
        return False

    for k, v in metadata.items():
        if not isinstance(k, str):
            return False
        if not is_valid_flat_value(v):
            return False

    return True
