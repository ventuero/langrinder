import importlib.resources
import sys
from dataclasses import dataclass
from pathlib import Path

import toml

LANGRINDER_PATH = importlib.resources.files("langrinder")


def load_config():
    current_dir = Path.cwd()
    pyproject_path = None

    for parent in [current_dir] + list(current_dir.parents):
        potential_path = parent / "pyproject.toml"
        if potential_path.exists():
            pyproject_path = potential_path
            break

    if not pyproject_path:
        return {}

    try:
        config_data = toml.load(pyproject_path)
        return config_data.get("tool", {}).get("langrinder", {})
    except FileNotFoundError:
        sys.exit(1)


@dataclass
class LangrinderConfig:
    locales_path: str
    output: str

    default_locale: str = "ru"
    node: str = "langrinder.nodes.ConstLanguageNode"
    base_node_template: str = f"{LANGRINDER_PATH}/generator/base_node.mako"
    base_translation_template: str = (
        f"{LANGRINDER_PATH}/generator/base_translation.mako"
    )
    translation_name: str = "Translation"


config = LangrinderConfig(**load_config())
