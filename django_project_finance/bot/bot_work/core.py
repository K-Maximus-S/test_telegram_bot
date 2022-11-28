from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from bot.bot_work.start_command import start, text_message, add_goal, GOAL, AMOUNT, DATAA, goal, amount, \
    dataa, cancel_goal, aliases_editing, ALIASES_EDITING, CATEGORY_EDITING, CODENAME_EDITING, STATISTICS_PLAN, \
    CHECK_PLAN, category_editing, \
    codename_editing, statistics_plan, check_plan
from django_project_finance.settings import TOKEN_TELEGRAM_BOT_API


def run_bot():
    """Основа бота: прокинули токен, подкючили команду старт, создали пулинг"""

    updater = Updater(TOKEN_TELEGRAM_BOT_API)
    dp = updater.dispatcher


    # start
    dp.add_handler(CommandHandler('start', start))
    # Обработка цели
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('add_goal', add_goal)],
        states={
            GOAL: [CommandHandler('cancel_goal', cancel_goal), MessageHandler(Filters.text, goal)],
            AMOUNT: [CommandHandler('cancel_goal', cancel_goal), MessageHandler(Filters.text, amount)],
            DATAA: [CommandHandler('cancel_goal', cancel_goal), MessageHandler(Filters.text, dataa)],
            ALIASES_EDITING: [CommandHandler('cancel_goal', cancel_goal), MessageHandler(Filters.text, aliases_editing)],
            CATEGORY_EDITING: [CommandHandler('cancel_goal', cancel_goal), MessageHandler(Filters.text, category_editing)],
            CODENAME_EDITING: [CommandHandler('cancel_goal', cancel_goal), MessageHandler(Filters.text, codename_editing)]
        },
        fallbacks=[CommandHandler('cancel_goal', cancel_goal)],
    )
    dp.add_handler(conv_handler)

    # Обработка статистики
    plan_handler = ConversationHandler(
        entry_points=[CommandHandler('statistics_plan', statistics_plan)],
        states={
            STATISTICS_PLAN: [CommandHandler('cancel_goal', cancel_goal), MessageHandler(Filters.text, statistics_plan)],
            CHECK_PLAN: [CommandHandler('cancel_goal', cancel_goal), MessageHandler(Filters.text, check_plan)]
        },
        fallbacks=[CommandHandler('cancel_goal', cancel_goal)],
    )
    dp.add_handler(plan_handler)

    # Обработка добавления расходов
    dp.add_handler(MessageHandler(Filters.text, callback=text_message))

    updater.start_polling()
    updater.idle()
