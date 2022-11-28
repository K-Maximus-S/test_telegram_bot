from telegram.ext import ConversationHandler
from business_logic.expenses import add_expense
from business_logic.work_user import verification_user, add_user
from business_logic.creating_plan import new_purposes, editing_purposes
from business_logic.statek_plan import Purposes

GOAL, AMOUNT, DATAA, ALIASES_EDITING, CATEGORY_EDITING, CODENAME_EDITING = range(6)
STATISTICS_PLAN, CHECK_PLAN = range(2)


def start(update, context):

    """Определяем пользователя по id ->bool.
      (Логика: Если пользователь запускал бота(/start) и ставил цели (/add_goal), то он будет в БД)
      True:  ->text_result = (
                            "Я тебя знаю:)\n\n"
                            "У тебя есть цели. Хотите изменить? /goal_edit\n"
                             "Нужна помощь? /help\n"
                             "Работа с расходами: /expenses\n")
      False: ->text_result = (
                             'Привет. Я бот, который поможет тебе рассчитать твой бюджет\n\n'
                             'При нажатии команды "/add_goal", готов к общению.\n'
                             'При нажатии команды "/cancel", распрощаемся.\n' TODO: не добавил(/cancel)
                              'Если возникнут вопросы, то ты всегда можешь нажать "/help".\n')"""
    verification_id = verification_user(update.effective_user.id)
    update.message.reply_text(verification_id)



# Через FSM опрашиваем пользователя и ставим цели
def add_goal(update, context):
    update.message.reply_text(
        "Давай добавим цель\n"
        "Я буду задавать вопросы на которые надо будет ответить. \n"
        "Команда /cancel_goal, чтобы прекратить разговор.\n\n"
        "1) Какая у тебя цель? (формат записи-> Купить машина или Накопить на машину)")
    return GOAL


def goal(update, context):
    context.user_data['key_goal'] = update.message.text
    user = update.message.from_user
    user = update.message.reply_text(
        "2) Какая сумма цели? (формат записи-> 200000) \n"
        "Команда /cancel_goal, чтобы прекратить разговор.")
    return AMOUNT


def amount(update, context):
    context.user_data['key_amount'] = update.message.text
    user = update.message.from_user
    update.message.reply_text(
        "3) Какая дата цели? (формат записи-> 12.12.23)\n"
        "Команда /cancel_goal, чтобы прекратить разговор.")
    return DATAA


def dataa(update, context):
    """Инициализируем цель.
      (Логика: Если в БД есть похожая цель, то True иначе False)"""
    context.user_data['key_dataa'] = update.message.text
    user = update.message.from_user

    plann = new_purposes(context.user_data)

    if plann.codename_category_aliases_plan[0].r_logic == True:
        codename = plann.codename_category_aliases_plan[0].get_codename[0]
        category = plann.codename_category_aliases_plan[0].get_category[0]
        aliases = plann.codename_category_aliases_plan[0].get_alias
        # Добавляем в БД, таблица с целями "Purposes"
        editing_purposes(context.user_data, update.effective_user.id, codename, category, aliases)
        command_purposes = ConversationHandler.END
        text_result = ('Вау! Цель поставлена! \n\n'
                       'Есть ещё цели? Нажми /add_goal \n'
                       'Если нет. Нажми /statistics_plan')
    else:
        command_purposes = ALIASES_EDITING
        text_result = (f"Ой, я не распознал цель: {context.user_data['key_goal']}\n"
                       "Помоги определить.\n\n"
                       "Смотри подсказку\n"
                       "Структура|___Раздел___|__Категория_|____Цель_____|\n"
                       "Пример:  |Инвестиции_|__Машина___|Купить машину|\n"
                       "Пример:  |Инвестиции_|__Квартира_|___Ипотека___|\n\n"
                       "Как будет называться Цель? (формат записи-> Купить машина или Ипотека)\n\n"
                       "Команда /cancel_goal, чтобы прекратить разговор.")
    update.message.reply_text(text_result)
    return command_purposes

# цель не понятна, просим помочь
def aliases_editing(update, context):
    context.user_data['aliases_editing'] = update.message.text
    update.message.reply_text(
        "Смотри подсказку\n"
        "Структура|___Раздел___|__Категория_|____Цель_____|\n"
        "Пример:  |Инвестиции_|__Машина___|Купить машину|\n"
        "Пример:  |Инвестиции_|__Квартира_|___Ипотека___|\n\n"
        f"Какой категории будет относиться цель: {update.message.text}? "
        "(формат записи-> Машина или Квартира)\n"
        "Команда /cancel_goal, чтобы прекратить разговор.\n")
    return CATEGORY_EDITING


def category_editing(update, context):
    context.user_data['category_editing'] = update.message.text
    user = update.message.from_user
    user = update.message.reply_text(
        "Смотри подсказку\n"
        "Структура|___Раздел___|__Категория_|____Цель_____|\n"
        "Пример:  |Инвестиции_|__Машина___|Купить машину|\n"
        "Пример:  |Инвестиции_|__Квартира_|___Ипотека___|\n\n"
        f"Какому разделу будет относиться категория: {update.message.text}? "
        "(формат записи-> Инвестиции или ...)\n"
        "Команда /cancel_goal, чтобы прекратить разговор.\n")
    return CODENAME_EDITING


def codename_editing(update, context):
    context.user_data['codename_editing'] = update.message.text
    user = update.message.from_user
    codename = context.user_data['codename_editing']
    category = context.user_data['category_editing']
    aliases = context.user_data['aliases_editing']
    editing_purposes(context.user_data, update.effective_user.id, codename, category, aliases)
    update.message.reply_text('Спасибо\n\n'
                              'Есть ещё цели? Нажми /add_goal\n'
                              'Если нет. Нажми  /statistics_plan\n')
    return ConversationHandler.END


# Обработка статистики
def statistics_plan(update, context):
    user = update.message.from_user
    update.message.reply_text('Какой у тебя доход?')
    return CHECK_PLAN

def check_plan(update, context):
    """Здесь начинается работа со статистикой. Через класс Purposes()"""
    user = update.message.from_user
    context.user_data['income'] = update.message.text
    statistics = Purposes()
    statistics.load_purposes()
    statistics.check_purposes(update.effective_user.id, context.user_data)
    update.message.reply_text("...........")
    return ConversationHandler.END


def cancel_goal(update, context):
    user = update.message.from_user
    update.message.reply_text("Мое дело предложить - Ваше отказаться")
    return ConversationHandler.END


def text_message(update, context):
    """Добавление новых расходов"""
    expense = add_expense(update.message.text)  # обработка смс
    update.message.reply_text(expense)