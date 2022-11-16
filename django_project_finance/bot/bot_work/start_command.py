from business_logic.expenses import add_expense

def start(update, context):
    update.message.reply_text(
        text='Привет! Я бот финансист:)\n\n'
             'Выбери:\n'
             "Добавить расход: Формат -> 250 1 такси\n"
             "Сегодняшняя статистика: /today\n"
             "За текущий месяц: /month\n"
             "Последние внесённые расходы: /expenses\n"
             "Категории трат: /categories",
        # reply_markup=keyboard_with_options()
    )


def text_message(update, context):
    """Добавление новых расходов"""
    expense = add_expense(update.message.text) # обработка смс
    update.message.reply_text(expense)





