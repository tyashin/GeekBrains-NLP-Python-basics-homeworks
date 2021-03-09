"""5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём 
оргтехники на склад и передачу в определенное подразделение компании. 
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, 
можно использовать любую подходящую структуру, например словарь."""


class EquipmentWarehouse():

    def __init__(self):
        self.storage = {}
        self.orders = []
        self.eq_directory = []

    def recieve_equipment(self):

        print('Введите тип оборудования для оприходования, выбрав его код.', end='\n\n')
        self.list_equipment()

        try:
            eq_id = int(input('Введите код оборудования: '))
            eq = self.eq_directory[eq_id-1]
            quantity = int(input('Укажите количество оборудования: '))
        except:
            print('Неверный ввод!', end='\n\n')
            return

        self.orders.append(
            {"eqipment": eq, "quantity": quantity, "department": "warehouse", "id": len(self.orders)+1})

        current_quantity = self.storage.setdefault(eq.model, 0)
        self.storage[eq.model] = current_quantity + quantity

    def ship_equipment(self):

        print('Введите тип оборудования для отгрузки, выбрав его код.', end='\n\n')
        self.list_equipment()

        try:
            eq_id = int(input('Введите код оборудования: '))
            eq = self.eq_directory[eq_id-1]
            quantity = int(input('Укажите количество оборудования: '))
        except:
            print('Неверный ввод!', end='\n\n')
            return

        current_quantity = self.storage.setdefault(eq.model, 0)
        if current_quantity < quantity:
            print(
                f'Оборудования "{eq.model}" на складе недостаточно. Требуется {quantity} шт. В наличии {current_quantity} шт.')
            return

        department = input(
            'Введите название департмента-получателя оборудования: ')

        self.orders.append(
            {"eqipment": eq, "quantity": -quantity, "department": department, "id": len(self.orders)+1})

        self.storage[eq.model] = current_quantity - quantity

    def list_equipment(self):
        for i, el in enumerate(self.eq_directory, 1):
            print(f'Код: {i}, Модель: {el.model}')
        print()

    def view_inventory_balance(self):
        print(f'Остатки оргтехники на складе: {self.storage}', end='\n\n')

    def view_invoices(self):
        print('Список накладных:')
        [print(el) for el in self.orders]
        print()

    def add_data_to_equipment_directory(self):
        print('Текущие данные в справочнике "Оборудование:"')
        [print(el) for el in self.eq_directory]
        print()

        eq_types = {
            1: {
                'params_str': 'Модель, Производитель, Цена, Скорость печати, Ресурс(стр.). ',
                'class': Printer
            },
            2: {
                'params_str': 'Модель, Производитель, Цена, Скорость сканирования, Цветность. ',
                'class': Scanner
            },
            3: {
                'params_str': 'Модель, Производитель, Цена, Ресурс(стр. в мес.), Разрешение сканирования. ',
                'class': Copier
            }
        }
        try:
            eq_type = int(
                input('Укажите тип добавляемого оборудования: 1 - Принтер, 2 - Сканер, 3 - Ксерокс: '))
            if eq_type not in range(1, 4):
                raise Exception
        except:
            print('Неверный ввод!', end='\n\n')
            return

        user_str = input('Введите строку данных об оборудовании, разделенных пробелами, в следующем формате: '
                         + eq_types[eq_type]['params_str'] + '\nОбязательное поле - "Модель", остальные поля можно не заполнять: ')
        print()
        eq_data = [el.strip()
                   for el in user_str.split(',') if len(el.strip()) != 0]
        if len(eq_data) == 0:
            print('Неверный ввод!', end='\n\n')
            return

        cur_length = len(eq_data)
        for i in range(0, 5 - cur_length):
            eq_data.append(None)

        # price
        try:
            eq_data[2] = float(eq_data[2]) if eq_data[2] != None else 0
        except:
            print('Неверный формат цены!', end='\n\n')
            return

        eq = eq_types[eq_type]['class'](eq_data)
        self.eq_directory.append(eq)


class OfficeEquipment():

    def __init__(self, eq_params):
        self.price = eq_params[2]
        self.model = eq_params[0]
        self.manufacturer = eq_params[1]


class Printer(OfficeEquipment):

    def __init__(self, eq_params):
        super().__init__(eq_params)
        self.print_speed = eq_params[3]
        self.print_resource = eq_params[4]

    def __str__(self):
        return str({
            "Модель": self.model,
            "Производитель": self.manufacturer,
            "Цена": self.price,
            "Скорость печати": self.print_speed,
            "Ресурс(стр.)": self.print_resource,
        })


class Scanner(OfficeEquipment):

    def __init__(self, eq_params):
        super().__init__(eq_params)
        self.scan_speed = eq_params[3]
        self.color_scan = eq_params[4]

    def __str__(self):
        return str({
            "Модель": self.model,
            "Производитель": self.manufacturer,
            "Цена": self.price,
            "Скорость сканирования": self.scan_speed,
            "Цветность": self.color_scan,
        })


class Copier(OfficeEquipment):

    def __init__(self, eq_params):
        super().__init__(eq_params)
        self.duty_cycle = eq_params[3]
        self.resolution = eq_params[4]

    def __str__(self):
        return str({
            "Модель": self.model,
            "Производитель": self.manufacturer,
            "Цена": self.price,
            "Ресурс(стр. в мес.)": self.duty_cycle,
            "Разрешение сканирования.": self.resolution,
        })
