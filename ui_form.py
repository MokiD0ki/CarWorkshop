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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_window_tab = QTabWidget(self.centralwidget)
        self.main_window_tab.setObjectName(u"main_window_tab")
        self.main_window_tab.setGeometry(QRect(0, 0, 801, 561))
        self.employees_tab = QWidget()
        self.employees_tab.setObjectName(u"employees_tab")
        self.widget = QWidget(self.employees_tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 251, 501))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.employee_list_label = QLabel(self.widget)
        self.employee_list_label.setObjectName(u"employee_list_label")

        self.verticalLayout.addWidget(self.employee_list_label)

        self.employees_list = QListWidget(self.widget)
        self.employees_list.setObjectName(u"employees_list")

        self.verticalLayout.addWidget(self.employees_list)

        self.frame = QFrame(self.employees_tab)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(350, 10, 441, 511))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.employee_data_widget = QWidget(self.frame)
        self.employee_data_widget.setObjectName(u"employee_data_widget")
        self.employee_data_widget.setGeometry(QRect(0, 0, 441, 501))
        self.employee_calendar = QCalendarWidget(self.employee_data_widget)
        self.employee_calendar.setObjectName(u"employee_calendar")
        self.employee_calendar.setGeometry(QRect(140, 330, 301, 171))
        self.employee_calendar.setGridVisible(True)
        self.remove_employee_button = QPushButton(self.employee_data_widget)
        self.remove_employee_button.setObjectName(u"remove_employee_button")
        self.remove_employee_button.setGeometry(QRect(300, 0, 141, 31))
        self.add_employee_button = QPushButton(self.employee_data_widget)
        self.add_employee_button.setObjectName(u"add_employee_button")
        self.add_employee_button.setGeometry(QRect(0, 0, 161, 31))
        self.widget1 = QWidget(self.employee_data_widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(12, 42, 261, 131))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.employee_name_label = QLabel(self.widget1)
        self.employee_name_label.setObjectName(u"employee_name_label")

        self.verticalLayout_3.addWidget(self.employee_name_label)

        self.employee_surname_label = QLabel(self.widget1)
        self.employee_surname_label.setObjectName(u"employee_surname_label")

        self.verticalLayout_3.addWidget(self.employee_surname_label)

        self.employee_salary_label = QLabel(self.widget1)
        self.employee_salary_label.setObjectName(u"employee_salary_label")

        self.verticalLayout_3.addWidget(self.employee_salary_label)

        self.employe_id_label = QLabel(self.widget1)
        self.employe_id_label.setObjectName(u"employe_id_label")

        self.verticalLayout_3.addWidget(self.employe_id_label)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.employee_name_edit = QLineEdit(self.widget1)
        self.employee_name_edit.setObjectName(u"employee_name_edit")

        self.verticalLayout_2.addWidget(self.employee_name_edit)

        self.employee_surname_edit = QLineEdit(self.widget1)
        self.employee_surname_edit.setObjectName(u"employee_surname_edit")

        self.verticalLayout_2.addWidget(self.employee_surname_edit)

        self.employee_salary_edit = QLineEdit(self.widget1)
        self.employee_salary_edit.setObjectName(u"employee_salary_edit")

        self.verticalLayout_2.addWidget(self.employee_salary_edit)

        self.employee_id_edit = QLineEdit(self.widget1)
        self.employee_id_edit.setObjectName(u"employee_id_edit")

        self.verticalLayout_2.addWidget(self.employee_id_edit)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.main_window_tab.addTab(self.employees_tab, "")
        self.tickets_tab = QWidget()
        self.tickets_tab.setObjectName(u"tickets_tab")
        self.main_window_tab.addTab(self.tickets_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menucar = QMenu(self.menubar)
        self.menucar.setObjectName(u"menucar")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menucar.menuAction())

        self.retranslateUi(MainWindow)

        self.main_window_tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.employee_list_label.setText(QCoreApplication.translate("MainWindow", u"Employees", None))
        self.remove_employee_button.setText(QCoreApplication.translate("MainWindow", u"Remove Employee", None))
        self.add_employee_button.setText(QCoreApplication.translate("MainWindow", u"Add Employee", None))
        self.employee_name_label.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.employee_surname_label.setText(QCoreApplication.translate("MainWindow", u"Surname:", None))
        self.employee_salary_label.setText(QCoreApplication.translate("MainWindow", u"Salary $/h:", None))
        self.employe_id_label.setText(QCoreApplication.translate("MainWindow", u"Employee_id:", None))
        self.main_window_tab.setTabText(self.main_window_tab.indexOf(self.employees_tab), QCoreApplication.translate("MainWindow", u"Employees", None))
        self.main_window_tab.setTabText(self.main_window_tab.indexOf(self.tickets_tab), QCoreApplication.translate("MainWindow", u"Tickets", None))
        self.menucar.setTitle(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

