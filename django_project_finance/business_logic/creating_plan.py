from business_logic.categories import Categories
from db_tables.db_work import insert_db_purposes

def new_purposes(variable_purpose):
    """Проверка цели пользователя.
    Если в БД есть похожее то True.
    Иначе False ->просим помочь определить цель"""

    category_db_plan = Categories()
    category_db_plan.load_categories()
    category_db_plan.get_plan(variable_purpose)
    return category_db_plan

def editing_purposes(variable_purpose, variable_id, codename, category, aliases):
    """Добавление цели в БД Purposes"""
    insert_db_new = insert_db_purposes(
        id_user_tg=variable_id,
        codename=codename,
        category=category,
        aliases=aliases,
        price=variable_purpose['key_amount'],
        data=variable_purpose['key_dataa']
    )
    return

class Statistics:
    """Для расчета статистики"""
