# Проект сосздания анлитического отчета из списка покупок
---
### Проект содержит аналитические функции:
- ```total_revenue(purchases)``` - Возвращает общую выручку.
- ```items_by_category(purchases)``` - Возвращает словарь,
    где ключ — категория, а значение — список уникальных товаров в этой.
- ```expensive_purchases(purchases, min_price)``` - Выводит все покупки, где цена товара больше или равна min_price.
- ```average_price_by_category(purchases)``` - Считает среднюю цену товаров по каждой категории.
- ```most_frequent_category``` - Опеределяет самую популярную категорю товаров.

---

### Данные о покупках хранятся в файле ```data.py``` в виде списка словарей.