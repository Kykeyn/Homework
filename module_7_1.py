class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = "products.txt"

    def get_products(self):
        open_file_r = open(self.__file_name, "r")
        read_file = open_file_r.read()
        open_file_r.close()
        return read_file

    def add(self, *products):
        list_ = self.get_products()
        for product in products:
            open_file_a = open(self.__file_name, "a")
            if product.name not in list_:
                open_file_a.write(
                    f"{product.name}, {product.weight}, {product.category}\n"
                )
            else:
                print(f"Продукт {product.name} уже есть в магазине")
        open_file_a.close()


s1 = Shop()
p1 = Product("Potato", 50.5, "Vegetables")
p2 = Product("Spaghetti", 3.4, "Groceries")
p3 = Product("Potato", 5.5, "Vegetables")

print(p2)  # __str__
s1.add(p1, p2, p3)

print(s1.get_products())
