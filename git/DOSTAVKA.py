import os
os.system("cls")

class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} so'm"


class Menu:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def display_menu(self):
        print("\nMenu:")
        for i, dish in enumerate(self.dishes, start=1):
            print(f"{i}. {dish}")


class Order:
    order_count = 0

    def __init__(self, selected_dishes):
        Order.order_count += 1
        self.order_id = Order.order_count
        self.selected_dishes = selected_dishes
        self.total_price = sum(dish.price for dish in selected_dishes)

    def __str__(self):
        dish_list = ", ".join([dish.name for dish in self.selected_dishes])
        return (f"Buyurtma raqami: {self.order_id}\n"
                f"Ovqatlar: {dish_list}\n"
                f"Umumiy summa: {self.total_price} so'm")


class Customer:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone = phone_number


class Deliver:
    def __init__(self, name, car_number):
        self.name = name
        self.car = car_number


class System:
    def __init__(self):
        self.menu = Menu()
        self.orders = []

    def create_menu(self):
        self.menu.add_dish(Dish("Somsa", 5000))
        self.menu.add_dish(Dish("Lag'mon", 35000))
        self.menu.add_dish(Dish("Shashlik", 15000))
        self.menu.add_dish(Dish("Norin", 25000))

    def take_order(self):
        self.menu.display_menu()
        selected_dishes = []

        while True:
            choice = input("Ovqat raqamini tanlang (0-exit): ")
            if choice == "0":
                break
            try:
                dish_index = int(choice) - 1
                selected_dishes.append(self.menu.dishes[dish_index])
            except (ValueError, IndexError):
                print("Noto'g'ri tanlov, qayta urinib ko'ring.")

        if selected_dishes:
            order = Order(selected_dishes)
            self.orders.append(order)
            print("\nBuyurtma qabul qilindi:")
            print(order)
            return order
        else:
            print("Buyurtma qilinmadi.")
            return None

    def deliver_order(self, order, delivery_person):
        print(f"\nBuyurtma #{order.order_id} yetkazilmoqda:")
        print(f"Yetkazib beruvchi: {delivery_person.name} ({delivery_person.car})")
        print(f"Mijozga yetkazildi: {order.total_price} so'm")


if __name__ == "__main__":
    system = System()
    system.create_menu()

    customer = Customer("Firdavs", "+998901234567")
    delivery_person = Deliver("Vali", "01A777AA")

    order = system.take_order()
    if order:
        system.deliver_order(order, delivery_person)


