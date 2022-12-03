from abc import ABC, abstractmethod


class OfficeEquipment(ABC):
    def __init__(self, brand, number, number_in, number_out):
        self.brand = brand
        self.number = number              # количество находящихся на складе единиц техники
        self.number_in = number_in        # количество поступивших на склад единиц техники
        self.number_out = number_out      # количество отгруженных со склада единиц техники

    @abstractmethod
    def traffic_of_equipment(self):
        pass

    @staticmethod
    def valid_number(obj):
        if not isinstance(obj, int):
            return f'Числа вводятся цифрами! Исправьте!'


class Printer(OfficeEquipment):
    def __init__(self, brand, number, number_in, number_out, color_print):
        super().__init__(brand, number, number_in, number_out)
        self.color_print = color_print

    def __str__(self):
        return f'На складе на начало дня: {self.number} шт. - принтер {self.brand}, цветная печать - {self.color_print}'

    def traffic_of_equipment(self):
        return f'На складе на конец дня: {self.number + self.number_in - self.number_out} шт. - ' \
               f' принтер {self.brand}, цветная печать - {self.color_print}'


class MultiFunctionPrinter(OfficeEquipment):
    def __init__(self, brand, number, number_in, number_out, wi_fi):
        super().__init__(brand, number, number_in, number_out)
        self.wi_fi = wi_fi

    def __str__(self):
        return f'На складе на начало дня: {self.number} шт. - МФУ {self.brand} , наличие Wi-Fi - {self.wi_fi}'

    def traffic_of_equipment(self):
        return f'На складе на конец дня: {self.number + self.number_in - self.number_out} шт. - ' \
               f' МФУ {self.brand}, наличие Wi-Fi - {self.wi_fi}'


printer_1 = Printer('Samsung ML-1720', 'one', 2, 3, 'нет')
print(printer_1)
print(Printer.valid_number(printer_1))
print(printer_1.traffic_of_equipment())
print()
printer_2 = Printer('HP P2520', 7, 0, 0, 'да')
print(printer_2)
print(printer_2.traffic_of_equipment())
print()
mfp_1 = MultiFunctionPrinter('Canon LBP-4550', 7, 5, 3, 'да')
print(mfp_1)
print(mfp_1.traffic_of_equipment())