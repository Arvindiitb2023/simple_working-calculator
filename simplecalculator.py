import sys
from PyQt5 import QtWidgets, uic  # Use PySide2 if using PySide

class CalculatorApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(CalculatorApp, self).__init__()
        uic.loadUi("calculator.ui", self)  # Load the .ui file

        # Get the display widget
        self.display = self.findChild(QtWidgets.QLineEdit, 'lineEdit')  # The QLineEdit for the display

        # Connect buttons to the corresponding functions
        self.findChild(QtWidgets.QPushButton, 'Button_0').clicked.connect(lambda: self.press_number('0'))
        self.findChild(QtWidgets.QPushButton, 'Button_1').clicked.connect(lambda: self.press_number('1'))
        self.findChild(QtWidgets.QPushButton, 'Button_2').clicked.connect(lambda: self.press_number('2'))
        self.findChild(QtWidgets.QPushButton, 'Button_3').clicked.connect(lambda: self.press_number('3'))
        self.findChild(QtWidgets.QPushButton, 'Button_4').clicked.connect(lambda: self.press_number('4'))
        self.findChild(QtWidgets.QPushButton, 'Button_5').clicked.connect(lambda: self.press_number('5'))
        self.findChild(QtWidgets.QPushButton, 'Button_6').clicked.connect(lambda: self.press_number('6'))
        self.findChild(QtWidgets.QPushButton, 'Button_7').clicked.connect(lambda: self.press_number('7'))
        self.findChild(QtWidgets.QPushButton, 'Button_8').clicked.connect(lambda: self.press_number('8'))
        self.findChild(QtWidgets.QPushButton, 'Button_9').clicked.connect(lambda: self.press_number('9'))
        self.findChild(QtWidgets.QPushButton, 'Button_dot').clicked.connect(lambda: self.press_number('.'))
        self.findChild(QtWidgets.QPushButton, 'Button_in').clicked.connect(lambda: self.press_number('('))
        self.findChild(QtWidgets.QPushButton, 'Button_out').clicked.connect(lambda: self.press_number(')'))
        
        # Connect operator buttons
        self.findChild(QtWidgets.QPushButton, 'Button_add').clicked.connect(lambda: self.press_operator('+'))
        self.findChild(QtWidgets.QPushButton, 'Button_sub').clicked.connect(lambda: self.press_operator('-'))
        self.findChild(QtWidgets.QPushButton, 'Button_multi').clicked.connect(lambda: self.press_operator('*'))
        self.findChild(QtWidgets.QPushButton, 'Button_div').clicked.connect(lambda: self.press_operator('/'))
        self.findChild(QtWidgets.QPushButton, 'Button_percent').clicked.connect(lambda: self. press_operator('%'))

        # Equal and Clear
        self.findChild(QtWidgets.QPushButton, 'Button_equal').clicked.connect(self.calculate_result)
        self.findChild(QtWidgets.QPushButton, 'Button_cancel').clicked.connect(self.clear_display)

        self.current_input = ''

    def press_number(self, number):
        """Add number to the current input."""
        self.current_input += number
        self.display.setText(self.current_input)

    def press_operator(self, operator):
        """Add operator to the current input."""
        if self.current_input and self.current_input[-1] not in '+-*/%':
            self.current_input += operator
            self.display.setText(self.current_input)

    def calculate_result(self):
        """Evaluate the expression and display the result."""
        
        try:
            result = str(eval(self.current_input))  # Evaluate the math expression
            self.display.setText(result)
            self.current_input = result  # Allow further operations on the result
        except Exception as e:
            self.display.setText('Error')
            self.current_input = ''
    # def percent_calculation(self,operator):
    #     if self.current_input and self.current_input[-1] not in '+-*/%':
    #         self.current_input += operator
    #         self.display.setText(self.current_input)
    #     try:
    #         current_value = float(self.current_input)
    #         percent_value = current_value / 100
    #         self.display.setText(str(percent_value))
    #     except Exception as e:
    #         self.display.setText("Error")
    def clear_display(self):
        """Clear the display."""
        self.current_input = ''
        self.display.clear()

# Boilerplate to run the app

app = QtWidgets.QApplication(sys.argv)
window = CalculatorApp()
window.show()
sys.exit(app.exec_())
