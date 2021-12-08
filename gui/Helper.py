import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QPalette, QColor


def setup_gui() -> QtWidgets.QApplication:
    """
    SetupGui function which creates main window and sets theme
    :return:
    QtWidgets.QApplication
    """
    app = QtWidgets.QApplication([])

    app.setStyle("Fusion")

    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, QColor("white"))
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, QColor("black"))
    palette.setColor(QPalette.ToolTipText, QColor("white"))
    palette.setColor(QPalette.Text, QColor("white"))
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, QColor("white"))
    palette.setColor(QPalette.BrightText, QColor("red"))
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, QColor("black"))
    app.setPalette(palette)

    return app


class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index) -> None:
        """
        function to automatically align table items
        :param option:
        :param index:
        """
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter
