from abc import abstractmethod, ABC


class Storage(ABC):

    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    """Склад. В нем хранится любое количество любых товаров.
            Store не может быть заполнен если свободное место закончилось"""
    def __init__(self):
        self.items = {"печеньки" : 20, "пельмени" : 30, "собачки" : 10}
        self.capacity = 100


    def add(self, name, count):
        """увеличивает запас items с учетом лимита"""
        is_found = False
        if self.get_free_space() > count:
            for key in self.items.keys():
                if name == key:
                    self.items[key] = self.items[key] + count
                    is_found = True
            if not is_found:
                self.items[name]= count
                is_found = True
        if is_found:
            print(f"{name} - {count}шт - добавлен")
            print(self.items)
            print(f"На складе свободных мест: {Store().get_free_space()}")

        else:
            print(f"Товар не добавлен, нехватка мест. "
                  f"Осталось:{self.get_free_space()} мест")



    def remove(self, name, count):
        """уменьшение остатков до нуля"""
        for key in self.items.keys():
            if name == key:
                if self.items[key] - count > 0:
                    self.items[key] = self.items[key] - count
                    print(f"Товар {name} удален со склада")
                    break
                else:
                    print(f"Товара {name} на складе сталось только {self.items[key] - count} штук")
            else:
                print(f"Товара {name.title()} нет на складе")

    def get_free_space(self):
        """свободные места"""
        return self.capacity - sum(self.items.values())

    def get_items(self):
        """остатки склада (dict)"""
        return self.items

    def get_unique_items_count(self):
        """уникальные товары"""
        return len(self.items.keys())


class Shop(Store):
    """Магазин. В нем хранится **не больше 5 разных товаров**.
            Shop не может быть наполнен, если свободное место закончилось или в нем уже есть 5 разных товаров."""
    def __init__(self, limit=5):
        super().__init__()
        self.items = {}
        self.capacity = 20
        self.limit = limit

    @property
    def get_limit(self):
        return self.limit

    def add(self, name, count):
        """увеличивает запас items с учетом лимита capacity"""
        if self.get_unique_items_count() < self.limit:
            super().add(name, count)
        else:
            print(f"Товар {name} не может быть добавлен")


class Request:
    def __init__(self, str):

        lst = self.split(str)
        self.of = lst[4]       #Откуда
        self.to = lst[6]        #Куда
        self.amount = int(lst[1])
        self.goods = lst[2]

    def split(self, str):
        return str.split(" ")

    def __repr__(self):
        return f"Доставим {self.amount} {self.goods} со {self.of} в {self.to}"
