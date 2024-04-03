import sys, sqlite3
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PySide6.QtCore import Qt

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = sqlite3.connect('employees.db')
        self.c = self.conn.cursor()

        for employee in self.c.execute('''SELECT id, name, surname FROM employees'''):
            item = QListWidgetItem(employee[1] + ' ' + employee[2])
            item.setData(Qt.UserRole, employee[0])
            self.ui.employees_list.addItem(item)
        
        self.ui.employees_list.itemClicked.connect(self.on_employee_selected)

    def on_employee_selected(self):
        # Get the selected employee's id, name, surname and salary
        curr_employee_id = self.ui.employees_list.currentItem().data(Qt.UserRole)
        curr_name, *curr_surname = self.ui.employees_list.currentItem().text().split()
        curr_surname = ' '.join(curr_surname)
        
        # Assign the values to the appropriate fields
        self.ui.employee_name_edit.setText(curr_name)
        self.ui.employee_name_edit.setEnabled(True)
        self.ui.employee_surname_edit.setText(curr_surname)
        self.ui.employee_surname_edit.setEnabled(True)
        self.ui.employee_salary_edit.setText(str(self.c.execute('''SELECT salary FROM employees WHERE id=?''', (curr_employee_id,)).fetchone()[0]))
        self.ui.employee_salary_edit.setEnabled(True)
        self.ui.employee_id_edit.setText(str(curr_employee_id))
        self.ui.employee_id_edit.setEnabled(False)

        # Connect the remove_employee method to the remove_employee_button
        self.ui.remove_employee_button.clicked.connect(lambda: self.remove_employee(curr_employee_id))


    def remove_employee(self, employee_id):
        # Remove the selected employee from the database
        if employee_id is None:
            return
        
        self.c.execute('''DELETE FROM employees WHERE id=?''', (employee_id,))
        self.conn.commit()

        self.clear_employee_screen()

        # Remove the selected employee from the list
        selected_item = self.ui.employees_list.currentItem()
        if selected_item is not None:
            self.ui.employees_list.takeItem(self.ui.employees_list.row(selected_item))
        
        # Set the current selection to None
        self.ui.employees_list.setCurrentItem(None)
        

    def clear_employee_screen(self):
        self.ui.employee_name_edit.clear()
        self.ui.employee_name_edit.setEnabled(False)
        self.ui.employee_surname_edit.clear()
        self.ui.employee_surname_edit.setEnabled(False)
        self.ui.employee_salary_edit.clear()
        self.ui.employee_salary_edit.setEnabled(False)
        self.ui.employee_id_edit.clear()
        self.ui.employee_id_edit.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())