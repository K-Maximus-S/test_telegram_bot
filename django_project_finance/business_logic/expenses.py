""" Работа с расходами — их добавление, удаление, статистики"""
from business_logic.categories import Categories
from business_logic.parce import Parse_message


def add_expense(text):
    """Добавляет новое сообщение.
    Принимает на вход текст сообщения, пришедшего в бот."""
    message_t = Parse_message()
    message_t.list_from_message(text)

    category_db = Categories()
    category_db.load_categories()  # TODO передать в метод ->get_category
    category_db.get_category_expense(message_t.list_parse)

    insert_db_message = insert_db_expenses_needs(
        codename=category_db.codename_category_aliases[0].get_codename,
        category=category_db.codename_category_aliases[0].get_category,
        aliases=category_db.codename_category_aliases[0].get_alias,
        price=message_t.list_parse[0].price,
        quantity=message_t.list_parse[0].quantity,
        raw_text=message_t.list_parse[0].raw_text
    )

    return f"Добавлены траты {message_t.list_parse[0].price} руб на " \
           f"{category_db.codename_category_aliases[0].get_codename}.\n\n"
