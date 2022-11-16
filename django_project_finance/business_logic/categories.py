from db_tables.db_work import select_db


class Categories_result:
    """Структура категории из БД"""
    def __init__(self, r_codename, r_category, r_aliases):
        self.r_codename = r_codename
        self.r_category = r_category
        self.r_aliases = r_aliases

class Get_categories:
    """Структура соотношения: codename -> category -> alias"""
    def __init__(self, get_codename, get_category, get_alias):
        self.get_codename = get_codename
        self.get_category = get_category
        self.get_alias = get_alias

class Categories:
    """Класс для работы с категориями"""

    def __init__(self):
        self.list_categories = []
        self.dict_codename_aliases = {}
        self.dict_codename_category = {}
        self.codename_category_aliases = []

    def load_categories(self):
        """Возвращает справочник категорий расходов из БД"""
        categories = select_db()

        for cat in categories:
            codename = (cat[1])
            category = (cat[0])
            aliases = (cat[2])

            cat_object = Categories_result(
                r_codename=codename,
                r_category=category,
                r_aliases=aliases
            )
            self.list_categories.append(cat_object)

    def get_category(self, list_parse):
        """Возвращает категорию по одному из её алиасов."""
        variable_a = None
        variable_b = None
        category_get_category = None
        aliases_get_category = None
        codename_get_category = None

        for codename_aliases in self.list_categories:
            category = codename_aliases.r_category
            aliases = codename_aliases.r_aliases
            codename = codename_aliases.r_codename
            self.dict_codename_aliases[category] = aliases
            self.dict_codename_category[category] = codename #codename_get_category = codename

        for alias_message in list_parse:
            variable_a = alias_message.alias  # Молоко, из парсинга

        while variable_a != variable_b: # Определяется: алиас из БД == алиас из смс -> True: категория из БД == алиас из БД
            for get in self.dict_codename_aliases:
                a = self.dict_codename_aliases[get]  # Магазин:хлеб:вода:картофель. get=Магазин
                b = a.split(':')  # b: ['Такси', 'метро', 'автобус']
                for f in b:
                    variable_b = f
                    if variable_a == variable_b:
                        aliases_get_category = variable_b # Алиас
                        category_get_category = get # Категория
                        codename_get_category = self.dict_codename_category[category_get_category]
                        codename_category_aliases_object = Get_categories(
                            get_codename=codename_get_category,
                            get_category=category_get_category,
                            get_alias=aliases_get_category
                        )
                        self.codename_category_aliases.append(codename_category_aliases_object)
                        break
            break
        return