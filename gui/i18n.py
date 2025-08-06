from __future__ import annotations

import json
from pathlib import Path
from typing import Dict


class I18N:
    """Simple JSON-based translation loader."""

    def __init__(self, locale_dir: Path, lang: str = "ru") -> None:
        self.locale_dir = Path(locale_dir)
        self.translations: Dict[str, str] = {}
        self.lang = lang
        self.load(lang)

    def load(self, lang: str) -> None:
        path = self.locale_dir / f"{lang}.json"
        with path.open(encoding="utf-8") as f:
            self.translations = json.load(f)
        self.lang = lang

    def t(self, key: str) -> str:
        return self.translations.get(key, key)

