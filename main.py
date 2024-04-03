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
        self.clear_employee_screen()
        
        self.ui.employees_list.itemClicked.connect(self.on_employee_selected)
        self.ui.add_employee_button.clicked.connect(self.add_employee)

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
        self.ui.remove_employee_button.clicked.connect(self.remove_employee)

    def remove_employee(self):
        curr_item = self.ui.employees_list.currentItem()
        if curr_item is not None:
            curr_employee_id = curr_item.data(Qt.UserRole)
            self.remove_employee_helper(curr_employee_id)
            

    def remove_employee_helper(self, employee_id):
        self.c.execute('''DELETE FROM employees WHERE id=?''', (employee_id,))
        self.conn.commit()

        self.clear_employee_screen()

        # Remove the selected employee from the list
        for i in range(self.ui.employees_list.count()):
            if self.ui.employees_list.item(i).data(Qt.UserRole) == employee_id:
                self.ui.employees_list.takeItem(i)
                break
        
        # Set the current selection to None
        self.ui.employees_list.setCurrentItem(None)
        self.clear_employee_screen()
        

    def clear_employee_screen(self):
        self.ui.employee_name_edit.clear()
        self.ui.employee_name_edit.setEnabled(False)
        self.ui.employee_surname_edit.clear()
        self.ui.employee_surname_edit.setEnabled(False)
        self.ui.employee_salary_edit.clear()
        self.ui.employee_salary_edit.setEnabled(False)
        self.ui.employee_id_edit.clear()
        self.ui.employee_id_edit.setEnabled(False)

    
    def add_employee(self):
        self.add_employee_helper()
        self.ui.employee_name_edit.setEnabled(True)
        self.ui.employee_surname_edit.setEnabled(True)
        self.ui.employee_salary_edit.setEnabled(True)

        name = self.ui.employee_name_edit.text().strip().capitalize()
        surname = self.ui.employee_surname_edit.text().strip().capitalize()
        salary = self.ui.employee_salary_edit.text().strip()

        if name != '' and surname != '' and salary != '':
            self.c.execute('''INSERT INTO employees VALUES(NULL, ?, ?, ?)''', (name, surname, salary))
            self.conn.commit()

            item = QListWidgetItem(name + ' ' + surname)
            item.setData(Qt.UserRole, self.c.lastrowid)
            self.ui.employees_list.addItem(item)

            self.clear_employee_screen()
        else:
            print(f"name: '{name}', surname: '{surname}', salary: '{salary}'")
            print('Please fill in all fields')


    def add_employee_helper(self):
        employee_id = self.ui.employee_id_edit.text().strip()
        if self.ui.employees_list.currentItem() and self.ui.employees_list.currentItem().data(Qt.UserRole) == int(employee_id):
            self.clear_employee_screen()
            self.ui.employees_list.setCurrentItem(None)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())