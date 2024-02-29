class Pizza:
    class PepperoniPizza:
        def __init__ (self, name, dough, sauce, toppings, price):
            self.name = name
            self.dough = dough
            self.sauce = sauce
            self.toppings = toppings
            self.price = price

    pizza_1 = PepperoniPizza("1.Пепперони пицца","Среднее по толщине тесто","Кетчуп","Пепперони"," - 3100тг")
        
    class BBQPizza:
        def __init__ (self, name, dough, sauce, toppings, price):
            self.name = name
            self.dough = dough
            self.sauce = sauce
            self.toppings = toppings
            self.price = price
        
    pizza_2 = BBQPizza("2.Поганый Австралиец!","Толстое","Барбекю","Мясная вырезка"," - 2700тг")

    class SeafoodPizza:
        def __init__ (self, name, dough, sauce, toppings, price):
            self.name = name
            self.dough = dough
            self.sauce = sauce
            self.toppings = toppings
            self.price = price

    pizza_3 = SeafoodPizza("3.Палубная пицца","Среднее по толщине тесто","Сливочный","Морепродукты"," - 3100тг")

class Terminal:
    def __init__(self) -> None:
        self.menu: dict[int, Pizza] = {
                1: PepperoniPizza(),
                2: BBQPizza(),
                3: SeafoodPizza()
        }
        self.order: Order | None = None

    def display_menu(self) -> None:
        print("Name", "=")

    def take_payment(self) -> None:
        if self.order

    def confirm_order(self) -> bool:
        if self.order:
            print(f"Вся стоимость состовляет: {self.order.calculate_total()} теньге.")
            confirmation = input("Вы хотите подтвердить ваш заказ?(да/нет): ")
            if confirmation.lower() == "да":
                print("Заказ подтвержден.")
                return True
            else:
                print("Заказ отклонен.")
                return False
        else:
            print("Отсутствует заказ.")
            return False
class Order:
    def __init__(self) -> None:
        self.pizzas: list[Pizza] = []

        def add_pizza(self, pizza: Pizza) -> None:
            self.pizzas.append(pizza)

        def calculate_total(self) -> int:
            return sum(pizza.price for pizza in self.pizzas)