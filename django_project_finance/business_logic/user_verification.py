from db_tables.db_work import select_db_user_verification

class Verification_result:
    """Структура user из БД"""
    def __init__(self, user_id, activating_bot):
        self.user_id = user_id
        self.activating_bot = activating_bot

class Verification:
    """Класс аутентификации"""

    def __init__(self):
        self.list_user =[]
        self.dict_id_activating = {}

    def load_user_verification(self):
        """Возвращает список пользователей из БД"""
        user_verification = select_db_user_verification()

        for verification in user_verification:
            user_id_db = (verification[0])
            activating_bot_db = (verification[1])

            user_object = Verification_result(
                user_id=user_id_db,
                activating_bot=activating_bot_db
            )
            self.list_user.append(user_object)

    def user_verification_id(self, user_telegram_id):
        """Cравнивает пользователя телеграмм со списком пользователей из БД"""
        verification_telegram = None
        activating_true_false = None

        for user_id_activating in self.list_user:
            id_db = int(user_id_activating.user_id)
            activating_db = user_id_activating.activating_bot
            if user_telegram_id == id_db and activating_db == 'True':
                self.dict_id_activating[id_db] = True
            else:
                self.dict_id_activating[user_telegram_id] = False
        return