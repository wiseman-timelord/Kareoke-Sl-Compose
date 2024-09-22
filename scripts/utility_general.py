# Script: .\scripts\utility_general.py

import yaml

# Global Variables
SETTINGS_FILE = "data/persistence.yaml"

def load_settings():
    """Load settings from the YAML file."""
    try:
        with open(SETTINGS_FILE, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        return {}

def save_settings(settings):
    """Save settings to the YAML file."""
    with open(SETTINGS_FILE, "w") as file:
        yaml.dump(settings, file)
