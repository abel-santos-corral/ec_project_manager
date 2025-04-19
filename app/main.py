from loguru import logger
import os

from src.shared.infrastructure.config.config_loader import FOLDERS
from app.projects.infrastructure.json_project_repository import JsonProjectRepository
from app.projects.application.project_service import ProjectService

def main():
    # Make sure the folder exists
    log_folder = "app/data/logs"
    os.makedirs(log_folder, exist_ok=True)

    # Define log file path
    log_path = os.path.join(log_folder, "app.log")

    # Clear default handler and add our own
    logger.remove()
    logger.add(log_path, level="DEBUG", rotation="500 KB", retention=10)

    for name, path in FOLDERS.folders.items():
            logger.info(f"Folder name: {name} and folder: {path}")

    repo = JsonProjectRepository(
        input_file="app/data/persistence/projects.json",
        persistence_path=f"{FOLDERS.persistence}/projects"
    )
    service = ProjectService(repo)

    # Load projects
    service.load_projects()

    # Print mappings
    for key, prefix in service.get_project_mapping().items():
        logger.info(f"Project mapping: {key} -> {prefix}")

if __name__ == "__main__":
    main()
