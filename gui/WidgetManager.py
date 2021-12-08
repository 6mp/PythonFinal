from PySide6 import QtWidgets, QtCore
from functools import partial


class WidgetManager(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QVBoxLayout(self)

    def add_button(self, name: str, callback: any) -> QtWidgets.QPushButton:
        """
        :param name: text to be displayed on the button
        :param callback: function to be called if the button is clicked
        :return: the button object
        """
        button = QtWidgets.QPushButton(name)
        self.layout.addWidget(button)
        button.clicked.connect(partial(callback, button))
        return button

    def add_label(self, name: str, desired_align: QtCore.Qt.AlignmentFlag) -> QtWidgets.QLabel:
        """
        :param name: text to be displayed on the label
        :param desired_align: alignment of the text
        :return: the label object
        """
        label = QtWidgets.QLabel(name, alignment=desired_align)
        self.layout.addWidget(label)
        return label

    def add_table(self, rows: int, columns: int) -> QtWidgets.QTableWidget:
        """
        :param rows: number of rows the table should have
        :param columns: number of columns the table should have
        :return: the table object
        """
        table = QtWidgets.QTableWidget(rows, columns)
        self.layout.addWidget(table)
        return table

    def add_text_input(self) -> QtWidgets.QLineEdit:
        """
        adds a QLineEdit to the current layout
        :return: text input object
        """
        text_input = QtWidgets.QLineEdit()
        self.layout.addWidget(text_input)
        return text_input

    def add_combo_box(self) -> QtWidgets.QComboBox:
        """
        adds a QComboBox to the current layout
        :return: combo box object
        """
        combo_box = QtWidgets.QComboBox()
        self.layout.addWidget(combo_box)
        return combo_box
