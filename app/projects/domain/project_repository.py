from abc import ABC, abstractmethod
from typing import Optional, List
from .project import Project

class ProjectRepository(ABC):
    @abstractmethod
    def load_all(self) -> None:
        pass

    @abstractmethod
    def get_by_key(self, project_key: str) -> Optional[Project]:
        pass

    @abstractmethod
    def get_by_id(self, project_id: str) -> Optional[Project]:
        pass

    @abstractmethod
    def get_project_mapping(self) -> dict:
        pass
