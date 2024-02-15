from abc import ABC, abstractmethod
from pathlib import Path
from typing import Iterable, List, Mapping, Optional

from snakemake_interface_common.rules import RuleInterface


class JobReportInterface(ABC):
    @property
    @abstractmethod
    def rule(self) -> RuleInterface: ...


class CategoryInterface(ABC):
    @property
    @abstractmethod
    def name(self) -> str: ...

    @property
    @abstractmethod
    def is_other(self) -> bool: ...

    @property
    @abstractmethod
    def id(self) -> str: ...


class RuleRecordInterface(ABC):
    @property
    @abstractmethod
    def name(self) -> str: ...

    @property
    @abstractmethod
    def container_img_url(self) -> Optional[str]: ...

    @property
    @abstractmethod
    def conda_env(self) -> Optional[str]: ...

    @property
    @abstractmethod
    def n_jobs(self) -> int: ...

    @property
    @abstractmethod
    def id(self) -> str: ...

    @property
    @abstractmethod
    def source(self) -> str: ...

    @property
    @abstractmethod
    def output(self) -> List[str]: ...

    @property
    @abstractmethod
    def input(self) -> List[str]: ...

    @property
    @abstractmethod
    def language(self) -> str: ...


class ConfigFileRecordInterface(ABC):
    @abstractmethod
    def source(self) -> str: ...


class JobRecordInterface(ABC):
    @property
    @abstractmethod
    def job(self) -> JobReportInterface: ...

    @property
    @abstractmethod
    def rule(self) -> RuleInterface: ...

    @property
    @abstractmethod
    def starttime(self) -> float: ...

    @property
    @abstractmethod
    def endtime(self) -> float: ...

    @property
    @abstractmethod
    def output(self) -> List[str]: ...

    @property
    @abstractmethod
    def conda_env_file(self) -> Optional[Path]: ...

    @property
    @abstractmethod
    def container_img_url(self) -> Optional[str]: ...


class FileRecordInterface(ABC):
    @property
    @abstractmethod
    def path(self) -> Path: ...

    @property
    @abstractmethod
    def labels(self) -> Mapping[str, str]: ...

    @property
    @abstractmethod
    def caption(self) -> str: ...

    @property
    @abstractmethod
    def size(self) -> int: ...

    @property
    @abstractmethod
    def mime(self) -> str: ...

    @property
    @abstractmethod
    def id(self) -> str: ...

    @property
    @abstractmethod
    def wildcards(self) -> str: ...

    @property
    @abstractmethod
    def params(self) -> str: ...

    @property
    @abstractmethod
    def name(self) -> str: ...

    @property
    @abstractmethod
    def job(self) -> JobReportInterface: ...


class DAGReportInterface(ABC):
    @abstractmethod
    def toposorted(self) -> Iterable[List[JobReportInterface]]: ...

    @property
    @abstractmethod
    def dependencies(self) -> Mapping[JobReportInterface, JobReportInterface]: ...
