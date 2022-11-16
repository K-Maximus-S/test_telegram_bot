from db_tables.models import Aliases, Expenses_needs

def select_db():
    """Получаем результат из БД таблицы db_tables_aliases"""
    result = Aliases.objects.all().values_list('category', 'codename', 'aliases_list')
    return result

def ilnsert_db(codename, category, aliases, price, quantity, raw_text):
    result = Expenses_needs.objects.create(codename=codename, category=category, aliases=aliases, price=price, quantity=quantity, raw_text=raw_text)
    return result