from PyQt6.QtWidgets import *
from gui import *
from datetime import date


class Logic(QMainWindow, Ui_ProduceShop):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.clear_button.clicked.connect(lambda: self.clear())
        self.submit_button.clicked.connect(lambda: self.submit())
        self.receipt_button.clicked.connect(lambda: self.receipt_print())

    def clear(self):
        self.exception_label.clear()
        self.pear_input.clear()
        self.strawberry_input.clear()
        self.pineapple_input.clear()
        self.apple_input.clear()
        self.banana_input.clear()
        self.watermelon_input.clear()
        self.total_label.clear()
        self.produce_label.clear()
        self.cost_label.clear()
        self.dollars_label.clear()
        self.receipt_label_printed.clear()

    def convert_to_zero(self, text):
        if text == '':
            return 0.0
        else:
            return text

    def is_negative(self, text):
        if text < 0:
            return 0.0
        else:
            return text

    def submit(self):
        try:
            # Converting to a float
            pear_cost = float(self.convert_to_zero(self.pear_input.text().strip())) * (0.30)
            strawberries_cost = float(self.convert_to_zero(self.strawberry_input.text().strip())) * (0.40)
            # Logic handling negatives values
            pear_cost = self.is_negative(pear_cost)
            strawberries_cost = self.is_negative(strawberries_cost)
            # Cost calculations
            total = pear_cost + strawberries_cost
            if total >= 50:
                total -= 5
            # Setting the GUI labels
            self.total_label.setText('TOTAL:')
            self.produce_label.setText('Pears - \nStrawberries - \nPineapples - \nApples - \nBananas - \nWatermelons -')
            self.cost_label.setText(f'${pear_cost:.2f}\n${strawberries_cost:.2f}\n')
            self.dollars_label.setText(f'${total:.2f}')
            self.exception_label.clear()
            self.receipt_label_printed.clear()
        except:
            self.exception_label.setText(
                'Enter values that are numeric,\n e.g. 4 or 5.25. Input only numerical\n values; do not include "lbs"')
            self.total_label.clear()
            self.pear_input.clear()
            self.strawberry_input.clear()
            self.pineapple_input.clear()
            self.apple_input.clear()
            self.banana_input.clear()
            self.watermelon_input.clear()
            self.produce_label.clear()
            self.cost_label.clear()
            self.dollars_label.clear()
            self.receipt_label_printed.clear()

    def receipt_print(self):
        try:
            # Converting to a float
            pear_cost = float(self.convert_to_zero(self.pear_input.text().strip())) * (0.30)
            strawberries_cost = float(self.convert_to_zero(self.strawberry_input.text().strip())) * (0.40)
            # Logic handling negatives values
            pear_cost = self.is_negative(pear_cost)
            strawberries_cost = self.is_negative(strawberries_cost)
            # Cost calculations
            total = pear_cost + strawberries_cost
            if total >= 50:
                total -= 5
            # Clearing all labels
            self.exception_label.clear()
            self.pear_input.clear()
            self.strawberry_input.clear()
            self.pineapple_input.clear()
            self.apple_input.clear()
            self.banana_input.clear()
            self.watermelon_input.clear()
            self.total_label.clear()
            self.produce_label.clear()
            self.cost_label.clear()
            self.dollars_label.clear()

            self.receipt_label_printed.setText('Receipt Printed!\nThanks for shopping!')

            file = 'receipt'
            now = date.today()
            # Writing the TXT file
            with open(file, 'w') as receipt:
                receipt.write('-' * 50)
                receipt.write('\n{: ^50}\n'.format("The Produce Shop"))
                receipt.write('\n{: ^50}\n'.format('6001 Dodge Street'))
                receipt.write('{: ^50}\n'.format('Omaha, Nebraska'))
                receipt.write('{: ^50}\n'.format(f'Date: {now}'))
                receipt.write('-' * 50)
                receipt.write('\n{: ^50}'.format(f'Pears              ${pear_cost:.2f}'))
                receipt.write('\n{: ^50}'.format(f'Strawberries       ${strawberries_cost:.2f}'))
        except:
            self.exception_label.setText(
                'Enter values that are numeric,\n e.g. 4 or 5.25. Input only numerical\n values; do not include "lbs"')
            self.total_label.clear()
            self.pear_input.clear()
            self.strawberry_input.clear()
            self.pineapple_input.clear()
            self.apple_input.clear()
            self.banana_input.clear()
            self.watermelon_input.clear()
            self.produce_label.clear()
            self.cost_label.clear()
            self.dollars_label.clear()
            self.receipt_label_printed.clear()
