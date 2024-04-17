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

        for employee in self.c.execute('''SELECT employee_id, name, surname FROM employees'''):
            item = QListWidgetItem(employee[1] + ' ' + employee[2])
            item.setData(Qt.UserRole, employee[0])
            self.ui.employees_list.addItem(item)
        self.clear_employee_screen()

        for ticket in self.c.execute('''SELECT ticket_id, car_brand, car_registration_id, employee_id FROM tickets
                                        WHERE ticket_status='created' OR ticket_status='in progress'
                                     '''):
            item = QListWidgetItem(ticket[1] + ' ' + ticket[2] + ': ' + (ticket[3] if ticket[3] else 'unassigned'))
            item.setData(Qt.UserRole, ticket[0])
            self.ui.tickets_list.addItem(item)

        for ticket in self.c.execute('''SELECT ticket_id, car_brand, car_registration_id, employee_id FROM tickets
                                        WHERE ticket_status='closed' OR ticket_status='done'
                                     '''):
            item = QListWidgetItem(ticket[1] + ' ' + ticket[2] + ': ' + (ticket[3] if ticket[3] else 'unassigned'))
            item.setData(Qt.UserRole, ticket[0])
            self.ui.tickets_list.addItem(item)
        
        self.ui.employees_list.itemClicked.connect(self.on_employee_selected)
        self.ui.add_employee_button.clicked.connect(self.add_employee)
        self.ui.tickets_list.itemClicked.connect(self.on_ticket_selected)
        

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
        self.ui.employee_salary_edit.setText(str(self.c.execute('''SELECT salary FROM employees WHERE employee_id=?''', (curr_employee_id,)).fetchone()[0]))
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
        self.c.execute('''DELETE FROM employees WHERE employee_id=?''', (employee_id,))
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


    def set_ticket_on_screen(self, ticket_id):
        car_brand, car_model, car_registration_id, ticket_description, employee_id, ticket_status = self.c.execute('''SELECT car_brand, car_model, 
                                                                                             car_registration_id, ticket_description, employee_id, ticket_status 
                                                                                             FROM tickets WHERE ticket_id=?''', (ticket_id,)).fetchone()
        self.ui.car_brand_edit.setText(car_brand)
        self.ui.car_brand_edit.setEnabled(False)
        self.ui.car_model_edit.setText(car_model)
        self.ui.car_model_edit.setEnabled(False)
        self.ui.registration_number_edit.setText(car_registration_id)
        self.ui.registration_number_edit.setEnabled(False)
        self.ui.description_text_edit.setText(ticket_description)
        self.ui.description_text_edit.setEnabled(True)
        self.ui.ticket_status_combo_box.setCurrentText(ticket_status)
        self.ui.ticket_status_combo_box.setEnabled(True)
    

    def on_ticket_selected(self):
        self.ui.save_button.hide()
        ticket_id = self.ui.tickets_list.currentItem().data(Qt.UserRole)
        self.set_ticket_on_screen(ticket_id)

        self.ui.description_text_edit.textChanged.connect(self.description_change)
        self.ui.ticket_status_combo_box.currentTextChanged.connect(self.ticket_status_change)

    
    def description_change(self):
        self.ui.save_button.show()
        self.ui.save_button.clicked.connect(self.save_description)


    def ticket_status_change(self):
        self.ui.save_button.show()
        self.ui.save_button.clicked.connect(self.save_status)

    def save_status(self):
        ticket_id = self.ui.tickets_list.currentItem().data(Qt.UserRole)
        status = self.ui.ticket_status_combo_box.currentText()
        self.c.execute('''UPDATE tickets SET ticket_status=? WHERE ticket_id=?''', (status, ticket_id))
        
        self.conn.commit()
        self.ui.save_button.hide()

    
    def save_description(self):
        ticket_id = self.ui.tickets_list.currentItem().data(Qt.UserRole)
        description = self.ui.description_text_edit.toPlainText()
        self.c.execute('''UPDATE tickets SET ticket_description=? WHERE ticket_id=?''', (description, ticket_id))
        
        self.conn.commit()
        #self.ui.description_text_edit.textChanged.disconnect(self.description_change)
        self.ui.save_button.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())