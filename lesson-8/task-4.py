"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники."""


class EquipmentWarehouse():
    pass


class OfficeEquipment():

    def __init__(self, eq_params):
        self.price = eq_params.get("price", None)
        self.model = eq_params.get("model", None)
        self.manufacturer = eq_params.get("manufacturer", None)


class Printer(OfficeEquipment):

    def __init__(self, eq_params):
        super().__init__(eq_params)
        self.print_speed = eq_params.get("print_speed", None)
        self.print_resource = eq_params.get("print_resource", None)


class Scanner(OfficeEquipment):

    def __init__(self, eq_params):
        super().__init__(eq_params)
        self.scan_speed = eq_params.get("scan_speed", None)
        self.color_scan = eq_params.get("color_scan", None)


class Copier(OfficeEquipment):

    def __init__(self, eq_params):
        super().__init__(eq_params)
        self.duty_cycle = eq_params.get("duty_cycle", None)
        self.resolution = eq_params.get("resolution", None)
