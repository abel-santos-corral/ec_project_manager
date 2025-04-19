# tests/app/projects/domain/test_project.py
import os
import sys
from dotenv import load_dotenv
from app.projects.domain.project import Project

# Load environment variables from .env file
load_dotenv()

# Add the project root to the sys.path
sys.path.insert(0, os.getenv('PYTHONPATH'))

def test_project_creation():
    project = Project(
        project_key="TEST",
        project_name="Test",
        project_initials="T",
        project_full_name="Test Project",
        component_prefix="test_",
        project_id=12344
    )

    assert project.project_key == "TEST"
    assert project.component_prefix == "test_"
