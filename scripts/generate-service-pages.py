#!/usr/bin/env python3
"""Deprecated alias — use scripts/generate-servico-pages.py instead."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

if __name__ == "__main__":
    print("Note: generate-service-pages.py is deprecated. Running generate-servico-pages.py …\n")
    target = Path(__file__).parent / "generate-servico-pages.py"
    spec = importlib.util.spec_from_file_location("generate_servico_pages", target)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["generate_servico_pages"] = mod
    spec.loader.exec_module(mod)
    mod.main()
