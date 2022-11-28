from business_logic.user_verification import Verification
from db_tables.db_work import insert_db_user_verification


def verification_user(user_telegram_id):
    """Аутентификация — пропускаем сообщения только от одного Telegram аккаунта"""
    text_result = None
    user_telegram_verification = Verification()
    user_telegram_verification.load_user_verification()
    user_telegram_verification.user_verification_id(user_telegram_id)

    c = user_telegram_verification.dict_id_activating[user_telegram_id]
    if str(c) == 'True':  # TODO: str(user_telegram_verification.dict_id_activating[user_telegram_id]) == 'True':
        text_result = (
            "Я вас знаю:)\n\n"
            "У вас есть цели. Хотите изменить? /goal_edit\n"
            "Нужна помощь? /help\n"
            "Работа с расходами: /expenses\n")
    else:
        text_result = (
            'Привет. Я бот, который позволит тебе расчитать твой бюджет\n\n'
            'При нажатии команды "/add_goal", готов к общению.\n'
            'При нажатии команды "/cancel", распрощаемся.\n'
            'Если возникнут вопросы, то ты всегда можешь нажать "/help".\n')
    return text_result


def add_user(user_id):
    """Добавление нового пользователя в табл пользователей (User_verification) """
    insert_db_user = insert_db_user_verification(
        user_id=user_id,
        activating_bot=True  # TODO: здесь можно ставить значение в зависимости от того забил пользователь цели или нет. Может выйти раньше и потом началь заново
    )
