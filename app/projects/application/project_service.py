from app.projects.domain.project_repository import ProjectRepository

class ProjectService:
    def __init__(self, repository: ProjectRepository):
        self.repository = repository

    def load_projects(self):
        self.repository.load_all()

    def get_component_prefix(self, project_key: str) -> str:
        project = self.repository.get_by_key(project_key)
        return project.component_prefix if project else None

    def get_project_mapping(self) -> dict:
        return self.repository.get_project_mapping()
