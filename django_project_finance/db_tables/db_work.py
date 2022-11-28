from db_tables.models import Aliases, Expenses_needs, User_verification, Purposes


def select_db():
    """Получаем результат из БД таблицы db_tables_aliases"""
    result = Aliases.objects.all().values_list('category', 'codename', 'aliases_list')
    return result

def select_db_user_verification():
    """Получаем результат из БД таблицы User_verification"""
    result = User_verification.objects.all().values_list('user_id', 'activating_bot')
    return result

def select_db_purposes():
    """Получаем результат из БД таблицы Purposes"""
    result = Purposes.objects.all().values_list('id_user_tg', 'codename', 'category', 'aliases', 'price', 'data')
    return result

def insert_db_expenses_needs(codename, category, aliases, price, quantity, raw_text):
    result = Expenses_needs.objects.create(codename=codename, category=category, aliases=aliases, price=price, quantity=quantity, raw_text=raw_text)
    return result

def insert_db_user_verification(user_id, activating_bot):
    result = User_verification.objects.create(user_id=user_id, activating_bot=activating_bot)

def insert_db_purposes(id_user_tg, codename, category, aliases, price, data):
    result = Purposes.objects.create(id_user_tg=id_user_tg, codename=codename, category=category, aliases=aliases, price=price, data=data)
    return result