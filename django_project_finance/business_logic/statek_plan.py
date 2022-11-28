from db_tables.db_work import select_db_purposes


class Purposes_result:
    """Структура целей из БД"""

    def __init__(self, p_id_user_tg, p_codename, p_category, p_aliases, p_price, p_data):
        self.p_id_user_tg = p_id_user_tg
        self.p_codename = p_codename
        self.p_category = p_category
        self.p_aliases = p_aliases
        self.p_price = p_price
        self.p_data = p_data


class Purposes:
    """Класс для работы с целями"""

    def __init__(self):
        self.list_purposes = []

    def load_purposes(self):
        """Возвращает справочник категорий расходов из БД"""
        purposes = select_db_purposes()

        for pur in purposes:
            id_user_tg = pur[0],
            codename = pur[1],
            category = pur[2],
            aliases = pur[3],
            price = pur[4],
            data = pur[5]

            purposes_object = Purposes_result(
                p_id_user_tg=id_user_tg,
                p_codename=codename,
                p_category=category,
                p_aliases=aliases,
                p_price=price,
                p_data=data
            )
            self.list_purposes.append(purposes_object)

    def check_purposes(self, id_user_tg, v_income):
        """для проверки равенства целей с доходами. В два этапа
            1) сумма всех целей == доходности за 12 мес
            2) установленный временной промежуток достижения цели == выделяемой сумме за этот период из дохода"""
        sum_price_goal = 0.0
        sum_price_income = 0.0
        price_log = None

        # нахождение общей суммы целей
        for check in self.list_purposes:
            check_id_user_tg = check.p_id_user_tg[0]
            check_p_price = check.p_price[0]
            while id_user_tg == int(check_id_user_tg):
                sum_price_goal += float(check_p_price)
                break
        # нахождение общей суммы доходности за год
        var_income = v_income['income']
        sum_price_income = float(var_income) * 12.0

        # 1)
        if sum_price_goal == sum_price_income:
            price_log = None
        else:
            price_log = False

        # 2)
        for check in self.list_purposes:
            check_p_aliases = check.p_aliases[0]
            check_p_price = check.p_price[0]
            check_p_data_day = check.p_data
