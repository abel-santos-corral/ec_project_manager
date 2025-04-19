"""
This module defines a class FolderConfig to manage folder configurations
and their paths. It loads a YAML configuration file, creates directories 
as needed, and allows access to those folder paths.

The global instance `FOLDERS` is created to access folder configurations
anywhere in the project.
"""

import os
import yaml

class FolderConfig:
    """
    A class that loads folder paths from a YAML configuration file and ensures 
    the folders exist on the system. Provides an easy way to access folder paths 
    by key.
    """
    def __init__(self, config_path='data/config/config.yaml'):
        """
        Initializes the FolderConfig class by reading the configuration from 
        the specified YAML file, creating any necessary folders, and storing 
        their absolute paths.

        :param config_path: Path to the YAML configuration file.
            Default is 'data/config/config.yaml'.
        """
        with open(config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)

        self.folders = {}
        for key, relative_path in config['folders'].items():
            absolute_path = os.path.abspath(relative_path)
            os.makedirs(absolute_path, exist_ok=True)
            self.folders[key] = absolute_path

    def __getattr__(self, item):
        """
        Retrieves the folder path for the specified key.

        :param item: Key for the folder
        :return: The absolute path of the folder or None if not found
        """
        return self.folders.get(item)

# Global instance (you can import this anywhere)
FOLDERS = FolderConfig()
