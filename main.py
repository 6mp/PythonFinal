from gui.WidgetManager import *
from gui.Helper import *
from sportsipy.nfl.teams import Team


info_table = None
combo_box = None

team_lookup = {"Arizona Cardinals": "CAR",
               "Atlanta Falcons": "FAL",
               "Baltimore Ravens": "RAV",
               "Buffalo Bills": "BUF",
               "Carolina Panthers": "CAR",
               "Chicago Bears": "CHI",
               "Cincinnati Bengals": "CIN",
               "Cleveland Browns": "CLE",
               "Dallas Cowboys": "DAL",
               "Denver Broncos": "DEN",
               "Detroit Lions": "DET",
               "Green Bay Packers": "GNB",
               "Houston Texans": "HTX",
               "Indianapolis Colts": "CLT",
               "Jacksonville Jaguars": "JAX",
               "Kansas City Chiefs": "KAN",
               "Las Vegas Raiders": "RAI",
               "Los Angeles Chargers": "SDG",
               "Los Angeles Rams": "RAM",
               "Miami Dolphins": "MIA",
               "Minnesota Vikings": "MIN",
               "New England Patriots": "NWE",
               "New Orleans Saints": "NOR",
               "New York Giants": "NYG",
               "New York Jets": "NYJ",
               "Philadelphia Eagles": "PHI",
               "Pittsburgh Steelers": "PIT",
               "San Francisco 49ers": "SFO",
               "Seattle Seahawks": "SEA",
               "Tampa Bay Buccaneers": "TAM",
               "Tennessee Titans": "OTI",
               "Washington Football Team": "WAS"}


def pressed(button_widget: QtWidgets.QPushButton):
    button_widget.setText("Loading...")
    button_widget.repaint()

    selected_team = combo_box.currentText()
    for i in range(6):
        ravens = Team(team_lookup[selected_team], year=2021 - i)
        win_percentage = QtWidgets.QTableWidgetItem(str(round(ravens.win_percentage * 100, 2)))
        interceptions = QtWidgets.QTableWidgetItem(str(ravens.interceptions))
        fumbles = QtWidgets.QTableWidgetItem(str(ravens.fumbles))
        rush_yards_per_attempt = QtWidgets.QTableWidgetItem(str(ravens.rush_yards_per_attempt))
        pass_yards_per_attempt = QtWidgets.QTableWidgetItem(str(ravens.fumbles))
        yards_per_play = QtWidgets.QTableWidgetItem(str(ravens.fumbles))
        percent_drives_with_points = QtWidgets.QTableWidgetItem(str(round(ravens.percent_drives_with_points, 2)))
        percent_drives_with_turnovers = QtWidgets.QTableWidgetItem(str(round(ravens.percent_drives_with_turnovers, 2)))
        info_table.setItem(i, 0, win_percentage)
        info_table.setItem(i, 1, interceptions)
        info_table.setItem(i, 2, fumbles)
        info_table.setItem(i, 3, rush_yards_per_attempt)
        info_table.setItem(i, 4, pass_yards_per_attempt)
        info_table.setItem(i, 5, yards_per_play)
        info_table.setItem(i, 6, percent_drives_with_points)
        info_table.setItem(i, 7, percent_drives_with_turnovers)

    delegate = AlignDelegate(info_table)
    info_table.setItemDelegate(delegate)
    button_widget.setText("Ok")


if __name__ == "__main__":
    application = setup_gui()

    widget_manager = WidgetManager()
    widget_manager.setWindowTitle("python final: seasonal nfl stats")
    widget_manager.add_label("Instructions", QtCore.Qt.AlignCenter)
    widget_manager.add_label("Select the name of the football team you would like to see the stats of\n"
                             "Press Ok to fetch the data when you have a team selected", QtCore.Qt.AlignCenter)

    combo_box = widget_manager.add_combo_box()
    combo_box.setEditable(True)
    combo_box.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
    combo_box.addItems(team_lookup.keys())

    widget_manager.add_button("Ok", pressed)

    info_table = widget_manager.add_table(5, 8)
    info_table.setHorizontalHeaderLabels([" Win % ", " Interceptions ", " Fumbles ", " Rush Yards / Attempt ",
                                          "Pass Yards / Attempt ", " Avg Yards / Play ", " % Drives With Points ",
                                          " % Drives With Turnovers "])
    info_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
    info_table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
    info_table.setVerticalHeaderLabels(["2021", "2020", "2019", "2018", "2017"])
    info_table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    widget_manager.resize(1000, 800)
    widget_manager.show()

    sys.exit(application.exec())
