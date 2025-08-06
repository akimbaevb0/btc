from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[2]))
from gui.i18n import I18N


def test_russian_translation_loaded():
    i18n = I18N(Path(__file__).resolve().parent.parent / "locales", "ru")
    assert i18n.t("scan_button") == "Сканировать"
