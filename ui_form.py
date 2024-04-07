# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(919, 631)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_window_tab = QTabWidget(self.centralwidget)
        self.main_window_tab.setObjectName(u"main_window_tab")
        self.employees_tab = QWidget()
        self.employees_tab.setObjectName(u"employees_tab")
        self.gridLayout_2 = QGridLayout(self.employees_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.emploees_list_frame = QFrame(self.employees_tab)
        self.emploees_list_frame.setObjectName(u"emploees_list_frame")
        self.emploees_list_frame.setFrameShape(QFrame.StyledPanel)
        self.emploees_list_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.emploees_list_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.employee_list_widget = QWidget(self.emploees_list_frame)
        self.employee_list_widget.setObjectName(u"employee_list_widget")
        self.verticalLayout_6 = QVBoxLayout(self.employee_list_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.employee_list_label = QLabel(self.employee_list_widget)
        self.employee_list_label.setObjectName(u"employee_list_label")

        self.verticalLayout_5.addWidget(self.employee_list_label)

        self.employees_list = QListWidget(self.employee_list_widget)
        self.employees_list.setObjectName(u"employees_list")

        self.verticalLayout_5.addWidget(self.employees_list)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout.addWidget(self.employee_list_widget)


        self.gridLayout_2.addWidget(self.emploees_list_frame, 0, 0, 1, 1, Qt.AlignHCenter)

        self.employee_data_frame = QFrame(self.employees_tab)
        self.employee_data_frame.setObjectName(u"employee_data_frame")
        self.employee_data_frame.setFrameShape(QFrame.StyledPanel)
        self.employee_data_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.employee_data_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.employee_data_widget = QWidget(self.employee_data_frame)
        self.employee_data_widget.setObjectName(u"employee_data_widget")
        self.verticalLayout_4 = QVBoxLayout(self.employee_data_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.add_employee_button = QPushButton(self.employee_data_widget)
        self.add_employee_button.setObjectName(u"add_employee_button")

        self.verticalLayout_4.addWidget(self.add_employee_button)

        self.remove_employee_button = QPushButton(self.employee_data_widget)
        self.remove_employee_button.setObjectName(u"remove_employee_button")

        self.verticalLayout_4.addWidget(self.remove_employee_button)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.employee_name_label = QLabel(self.employee_data_widget)
        self.employee_name_label.setObjectName(u"employee_name_label")

        self.verticalLayout_3.addWidget(self.employee_name_label)

        self.employee_surname_label = QLabel(self.employee_data_widget)
        self.employee_surname_label.setObjectName(u"employee_surname_label")

        self.verticalLayout_3.addWidget(self.employee_surname_label)

        self.employee_salary_label = QLabel(self.employee_data_widget)
        self.employee_salary_label.setObjectName(u"employee_salary_label")

        self.verticalLayout_3.addWidget(self.employee_salary_label)

        self.employe_id_label = QLabel(self.employee_data_widget)
        self.employe_id_label.setObjectName(u"employe_id_label")

        self.verticalLayout_3.addWidget(self.employe_id_label)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.employee_name_edit = QLineEdit(self.employee_data_widget)
        self.employee_name_edit.setObjectName(u"employee_name_edit")

        self.verticalLayout_2.addWidget(self.employee_name_edit)

        self.employee_surname_edit = QLineEdit(self.employee_data_widget)
        self.employee_surname_edit.setObjectName(u"employee_surname_edit")

        self.verticalLayout_2.addWidget(self.employee_surname_edit)

        self.employee_salary_edit = QLineEdit(self.employee_data_widget)
        self.employee_salary_edit.setObjectName(u"employee_salary_edit")

        self.verticalLayout_2.addWidget(self.employee_salary_edit)

        self.employee_id_edit = QLineEdit(self.employee_data_widget)
        self.employee_id_edit.setObjectName(u"employee_id_edit")

        self.verticalLayout_2.addWidget(self.employee_id_edit)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.employee_calendar = QCalendarWidget(self.employee_data_widget)
        self.employee_calendar.setObjectName(u"employee_calendar")
        self.employee_calendar.setGridVisible(True)

        self.verticalLayout_4.addWidget(self.employee_calendar)


        self.verticalLayout_7.addWidget(self.employee_data_widget)


        self.gridLayout_2.addWidget(self.employee_data_frame, 0, 1, 1, 1)

        self.main_window_tab.addTab(self.employees_tab, "")
        self.tickets_tab = QWidget()
        self.tickets_tab.setObjectName(u"tickets_tab")
        self.gridLayout_3 = QGridLayout(self.tickets_tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ticket_list_frame = QFrame(self.tickets_tab)
        self.ticket_list_frame.setObjectName(u"ticket_list_frame")
        self.ticket_list_frame.setFrameShape(QFrame.StyledPanel)
        self.ticket_list_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.ticket_list_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.ticket_list_widget = QWidget(self.ticket_list_frame)
        self.ticket_list_widget.setObjectName(u"ticket_list_widget")
        self.widget = QWidget(self.ticket_list_widget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(60, 20, 260, 442))
        self.verticalLayout_12 = QVBoxLayout(self.widget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.unfinished_tickets_label = QLabel(self.widget)
        self.unfinished_tickets_label.setObjectName(u"unfinished_tickets_label")

        self.verticalLayout_10.addWidget(self.unfinished_tickets_label)

        self.unfinished_tickets_list = QListWidget(self.widget)
        self.unfinished_tickets_list.setObjectName(u"unfinished_tickets_list")

        self.verticalLayout_10.addWidget(self.unfinished_tickets_list)


        self.verticalLayout_12.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.finished_tickets_label = QLabel(self.widget)
        self.finished_tickets_label.setObjectName(u"finished_tickets_label")

        self.verticalLayout_11.addWidget(self.finished_tickets_label)

        self.finished_tickets_list = QListWidget(self.widget)
        self.finished_tickets_list.setObjectName(u"finished_tickets_list")

        self.verticalLayout_11.addWidget(self.finished_tickets_list)


        self.verticalLayout_12.addLayout(self.verticalLayout_11)


        self.verticalLayout_8.addWidget(self.ticket_list_widget)


        self.horizontalLayout_2.addWidget(self.ticket_list_frame)

        self.ticket_info_frame = QFrame(self.tickets_tab)
        self.ticket_info_frame.setObjectName(u"ticket_info_frame")
        self.ticket_info_frame.setFrameShape(QFrame.StyledPanel)
        self.ticket_info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.ticket_info_frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.ticket_info_widget = QWidget(self.ticket_info_frame)
        self.ticket_info_widget.setObjectName(u"ticket_info_widget")
        self.widget1 = QWidget(self.ticket_info_widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 30, 347, 293))
        self.verticalLayout_15 = QVBoxLayout(self.widget1)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.car_brand_label = QLabel(self.widget1)
        self.car_brand_label.setObjectName(u"car_brand_label")

        self.verticalLayout_13.addWidget(self.car_brand_label)

        self.car_model_label = QLabel(self.widget1)
        self.car_model_label.setObjectName(u"car_model_label")

        self.verticalLayout_13.addWidget(self.car_model_label)

        self.registration_number_label = QLabel(self.widget1)
        self.registration_number_label.setObjectName(u"registration_number_label")

        self.verticalLayout_13.addWidget(self.registration_number_label)


        self.horizontalLayout_3.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.car_brand_edit = QLineEdit(self.widget1)
        self.car_brand_edit.setObjectName(u"car_brand_edit")

        self.verticalLayout_14.addWidget(self.car_brand_edit)

        self.car_model_edit = QLineEdit(self.widget1)
        self.car_model_edit.setObjectName(u"car_model_edit")

        self.verticalLayout_14.addWidget(self.car_model_edit)

        self.registration_number_edit = QLineEdit(self.widget1)
        self.registration_number_edit.setObjectName(u"registration_number_edit")

        self.verticalLayout_14.addWidget(self.registration_number_edit)


        self.horizontalLayout_3.addLayout(self.verticalLayout_14)


        self.verticalLayout_15.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.desctiption_label = QLabel(self.widget1)
        self.desctiption_label.setObjectName(u"desctiption_label")

        self.horizontalLayout_4.addWidget(self.desctiption_label)

        self.description_text_edit = QTextEdit(self.widget1)
        self.description_text_edit.setObjectName(u"description_text_edit")

        self.horizontalLayout_4.addWidget(self.description_text_edit)


        self.verticalLayout_15.addLayout(self.horizontalLayout_4)


        self.verticalLayout_9.addWidget(self.ticket_info_widget)


        self.horizontalLayout_2.addWidget(self.ticket_info_frame)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.main_window_tab.addTab(self.tickets_tab, "")

        self.gridLayout.addWidget(self.main_window_tab, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 919, 22))
        self.menucar = QMenu(self.menubar)
        self.menucar.setObjectName(u"menucar")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menucar.menuAction())

        self.retranslateUi(MainWindow)

        self.main_window_tab.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.employee_list_label.setText(QCoreApplication.translate("MainWindow", u"Employees", None))
        self.add_employee_button.setText(QCoreApplication.translate("MainWindow", u"Add Employee", None))
        self.remove_employee_button.setText(QCoreApplication.translate("MainWindow", u"Remove Employee", None))
        self.employee_name_label.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.employee_surname_label.setText(QCoreApplication.translate("MainWindow", u"Surname:", None))
        self.employee_salary_label.setText(QCoreApplication.translate("MainWindow", u"Salary $/h:", None))
        self.employe_id_label.setText(QCoreApplication.translate("MainWindow", u"Employee_id:", None))
        self.main_window_tab.setTabText(self.main_window_tab.indexOf(self.employees_tab), QCoreApplication.translate("MainWindow", u"Employees", None))
        self.unfinished_tickets_label.setText(QCoreApplication.translate("MainWindow", u"Unfinished Tickets", None))
        self.finished_tickets_label.setText(QCoreApplication.translate("MainWindow", u"Finished Tickets", None))
        self.car_brand_label.setText(QCoreApplication.translate("MainWindow", u"Car brand:", None))
        self.car_model_label.setText(QCoreApplication.translate("MainWindow", u"Car model:", None))
        self.registration_number_label.setText(QCoreApplication.translate("MainWindow", u"Registration number:", None))
        self.desctiption_label.setText(QCoreApplication.translate("MainWindow", u"Description:", None))
        self.main_window_tab.setTabText(self.main_window_tab.indexOf(self.tickets_tab), QCoreApplication.translate("MainWindow", u"Tickets", None))
        self.menucar.setTitle(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

