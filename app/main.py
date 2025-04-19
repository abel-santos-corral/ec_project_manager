from src.shared.infrastructure.config.config_loader import FOLDERS
from app.projects.infrastructure.json_project_repository import JsonProjectRepository
from app.projects.application.project_service import ProjectService

def main():
    print("Input folder is:", FOLDERS.input)

    repo = JsonProjectRepository(
        input_file="app/data/config/projects.json",
        persistence_path=f"{FOLDERS.persistence}/projects"
    )
    service = ProjectService(repo)

    # Load projects
    service.load_projects()

    # Print mappings
    print("Project mapping:")
    for key, prefix in service.get_project_mapping().items():
        print(f"{key} -> {prefix}")

if __name__ == "__main__":
    main()
