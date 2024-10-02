class Product:

    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop():
    def __init__(self):
        self.__file_name = 'products.txt'   # Инкапсулированный атрибут

    def get_products(self):   # Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
        file = open(self.__file_name, 'r')
        _file = file.read()
        file.close()
        return _file

    def add(self, *products):
        file = open(self.__file_name, 'a')
        for i in products:
            if i.name in self.get_products():
                print(f'Продукт {i} уже есть в магазине')
            else:
                print(file.write(f'{i.name}, {i.weight}, {i.category}\n'))
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
