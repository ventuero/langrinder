project = "Langrinder"  # noqa: INP001
copyright = "2025, tirch"  # noqa: A001
author = "tirch"
release = "3.0.1"

extensions = [
    "sphinx_immaterial",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_immaterial"
html_static_path = ["_static"]

html_theme_options = {
    "repo_url": "https://github.com/tirch/langrinder",
    "repo_name": "tirch/langrinder",
    "icon": {
        "repo": "fontawesome/brands/github",
    },
    "palette": [
        {
            "media": "(prefers-color-scheme)",
            "toggle": {
                "icon": "material/brightness-auto",
                "name": "Switch to light mode",
            },
        },
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "light-green",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/lightbulb",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "deep-orange",
            "accent": "lime",
            "toggle": {
                "icon": "material/lightbulb-outline",
                "name": "Switch to system preference",
            },
        },
    ],
}

