# -*- coding: utf-8 -*-
"""Load templates/partials and substitute {{PLACEHOLDER}} variables."""

from __future__ import annotations

from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = SCRIPTS_DIR / "templates"
PARTIALS_DIR = TEMPLATES_DIR / "partials"


def apply_vars(template: str, variables: dict[str, str]) -> str:
    for key, value in variables.items():
        template = template.replace("{{" + key + "}}", value)
    return template


def load_partial(name: str) -> str:
    path = PARTIALS_DIR / name
    if not path.is_file():
        raise FileNotFoundError(f"Partial not found: {path}")
    return path.read_text(encoding="utf-8")


def load_template(name: str) -> str:
    path = TEMPLATES_DIR / name
    if not path.is_file():
        raise FileNotFoundError(f"Template not found: {path}")
    return path.read_text(encoding="utf-8")


def render_partial(name: str, variables: dict[str, str]) -> str:
    return apply_vars(load_partial(name), variables)


def render_template(name: str, variables: dict[str, str]) -> str:
    return apply_vars(load_template(name), variables)
