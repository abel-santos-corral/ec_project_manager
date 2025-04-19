# tests/app/projects/infrastructure/test_json_project_repository.py

import os
import json
import sys
import tempfile

from dotenv import load_dotenv
from app.projects.infrastructure.json_project_repository import JsonProjectRepository

# Load environment variables from .env file
load_dotenv()

# Add the project root to the sys.path
sys.path.insert(0, os.getenv('PYTHONPATH'))

def test_load_projects_and_get_by_id():
    test_data = {
        "0": {
            "Project key": "ABC",
            "Project name": "Test",
            "Project initials": "T",
            "Project full name": "Test Full",
            "Component prefix": "test_",
            "Project id": 12345
        }
    }

    # Define the base directory for temporary files
    base_tmp_dir = os.path.join(os.path.dirname(__file__), '../../../fixtures/tmp')

    # Create a temporary directory inside the base directory
    with tempfile.TemporaryDirectory(dir=base_tmp_dir) as tmp_dir:
        tmp_input_file = os.path.join(tmp_dir, 'input.json')
        with open(tmp_input_file, 'w') as f:
            json.dump(test_data, f)

        repo = JsonProjectRepository(input_file=tmp_input_file, persistence_path=tmp_dir)
        repo.load_all()
        project = repo.get_by_id("ABC")

        assert project is not None
        assert project.project_key == "ABC"
