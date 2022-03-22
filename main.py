from classes import Store, Request, Shop

store = Store()
if input('Хотите добавить товар?\ny/n\n').lower() == 'y':
    print(f"Свободных мест на складе: {store.get_free_space()}")
    store.add("зонт", 3)
    print(f"На складе свободных мест: {store.get_free_space()}")
else:
    print('Переходим к заказам')

if __name__ == '__main__':
    item = input("Что желаете приобрести?\n")
    count = input("Укажите количество\n")
    order = Request(f"Доставим {count} {item} со склада в магазин")
    print(order)
    shop = Shop()
    print(f"На {order.of} хранится:")
    for i, k in store.get_items().items():
        print(k, i)
    if store.get_items().get(order.goods, 0) < order.amount:
        print('Не хватает остатков на складе, попробуйте уменьшить количество или выберите другой товар')
    else:
        print('Заказ принят')
        store.remove(name=order.goods, count=order.amount)
        print(f'Курьер доставит {order.amount} {order.goods} со склада в магазин.')
        shop.add(name=order.goods, count=order.amount)

    print(f"На {order.of}е хранится:")
    for i, k in store.get_items().items():
        print(k, i)

    print(f"В {order.to}е хранится:")
    for i, k in shop.get_items().items():
        print(k, i)
