import json
import os
from typing import Optional
from app.projects.domain.project_repository import ProjectRepository
from app.projects.domain.project import Project

class JsonProjectRepository(ProjectRepository):
    def __init__(self, input_file: str, persistence_path: str):
        self.input_file = input_file
        self.persistence_path = persistence_path
        self.projects = {}

    def load_all(self) -> None:
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"No input file at {self.input_file}")
        with open(self.input_file, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
            for item in raw_data.values():  # handles "0", "1", etc.
                project = Project.from_dict({
                    'project_key': item['Project key'],
                    'project_name': item['Project name'],
                    'project_initials': item['Project initials'],
                    'project_full_name': item['Project full name'],
                    'component_prefix': item['Component prefix'],
                    'project_id': item['Project id']
                })
                self.projects[project.project_key] = project

    def save_all(self) -> None:
        os.makedirs(self.persistence_path, exist_ok=True)
        output_file = os.path.join(self.persistence_path, 'projects.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump([p.to_dict() for p in self.projects.values()], f, indent=4)

    def get_by_key(self, project_key: str) -> Optional[Project]:
        return self.projects.get(project_key)

    def get_project_mapping(self) -> dict:
        return {
            project.project_key: project.component_prefix
            for project in self.projects.values()
        }
