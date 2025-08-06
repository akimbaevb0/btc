import sys
from pathlib import Path

from PySide6.QtCore import QEasingCurve, QPropertyAnimation
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from i18n import I18N
import lib_wrapper


class MainWindow(QMainWindow):
    def __init__(self, i18n: I18N) -> None:
        super().__init__()
        self.i18n = i18n
        self.setWindowTitle(self.i18n.t("app_title"))

        self.label = QLabel(self.i18n.t("status_ready"))
        self.button = QPushButton(self.i18n.t("scan_button"))
        self.button.clicked.connect(self.on_scan)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def on_scan(self) -> None:
        self.label.setText(self.i18n.t("status_scanning"))
        lib_wrapper.scan()
        anim = QPropertyAnimation(self.label, b"geometry")
        anim.setDuration(500)
        anim.setStartValue(self.label.geometry())
        anim.setEndValue(self.label.geometry().adjusted(0, 0, 0, 10))
        anim.setEasingCurve(QEasingCurve.OutBounce)
        anim.start()
        self._anim = anim  # keep reference


def main() -> int:
    app = QApplication(sys.argv)
    i18n = I18N(Path(__file__).parent / "locales", "ru")
    window = MainWindow(i18n)
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
