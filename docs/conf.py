import importlib
import inspect
import os
from typing import Any, Dict, List, Optional

project: str = 'hanime'
author: str = 'alluding'
version: str = '2.0.0'
copyright: str = f'Copyright © {author}'

extensions: List[str] = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.linkcode",
    "myst_parser",
]

templates_path: List[str] = ['_templates']
exclude_patterns: List[str] = ['_build', 'Thumbs.db', '.DS_Store']

myst_enable_extensions: List[str] = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

myst_heading_anchors: int = 3

html_theme: str = 'furo'
html_static_path: List[str] = ['_static']

source_suffix: str = '.md'
master_doc: str = 'index'


def linkcode_resolve(domain: str, info: Dict[str, Any]) -> Optional[str]:
    try:
        if domain != "py" or not info["module"]:
            return None

        mod = importlib.import_module(info["module"])

        if "." in info["fullname"]:
            objname, attrname = info["fullname"].split(".")
            obj = getattr(mod, objname)

            try:
                obj = getattr(obj, attrname)
            except AttributeError:
                return None
        else:
            obj = getattr(mod, info["fullname"])

        try:
            file = inspect.getsourcefile(obj)
            lines = inspect.getsourcelines(obj)
        except TypeError:
            # e.g., object is a typing.Union
            return None

        file = os.path.relpath(file, os.path.abspath(".."))
        start, end = lines[1], lines[1] + len(lines[0]) - 1

        return f"https://github.com/alluding/hanime/blob/main/{file}#L{start}-L{end}"
    except Exception:
        return None
