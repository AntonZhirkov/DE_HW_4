from data import PURCHASES


def total_revenue(purchases):
    """Функция для расчета общей выручки."""
    total = 0
    for purchases in purchases:
        total += purchases['price'] * purchases['quantity']
    print('Общая выручка:', total)


def items_by_category(purchases):
    """Возвращает словарь,
    где ключ — категория, а значение — список уникальных товаров в этой.
    """
    categoryes = {}
    for purchases in purchases:
        categoryes.setdefault(
            purchases['category'], set()
        ).add(purchases['item'])
    print('Товары по категориям:', categoryes)


def expensive_purchases(purchases, min_price):
    """Выводит все покупки, где цена товара больше или равна min_price."""
    expensive_purchases = []
    for purchase in purchases:
        if purchase['price'] >= min_price:
            expensive_purchases.append(purchase)
    print(f'Покупки дороже {min_price}: {expensive_purchases}')


def average_price_by_category(purchases):
    """Считает среднюю цену товаров по каждой категории."""
    avg_price_categoryes = {}

    for purchase in purchases:
        avg_price_categoryes.setdefault(
            purchase['category'], list()
        ).append(purchase['price'])

    for avg_price_category in avg_price_categoryes:
        price_list = avg_price_categoryes[avg_price_category]
        avg_price_categoryes[avg_price_category] = (
            sum(price_list) / len(price_list)
        )
    print('Средняя цена по категориям:', avg_price_categoryes)


def most_frequent_category(purchases):
    """Опеределяет самую популярную категорю товаров."""
    popular_category = {}
    for purchase in purchases:
        category = purchase['category']
        popular_category[category] = (
            popular_category.get(category, 0) + purchase['quantity']
        )
    print(
        'Категория с наибольшим количеством проданных товаров:',
        max(popular_category, key=popular_category.get)
    )

if __name__ == '__main__':
    min_price = int(input('Введите минимальную стоимость товара: '))
    total_revenue(PURCHASES)
    items_by_category(PURCHASES)
    expensive_purchases(PURCHASES, 1)
    average_price_by_category(PURCHASES)
    most_frequent_category(PURCHASES)
