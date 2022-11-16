from django.core.management.base import BaseCommand

from bot.bot_work.core import run_bot
# from bot.bot_work.keyboard import keyboard_with_options


class Command(BaseCommand):

    help = 'Запускает пулинг телеграмм бота'

    def handle(self, *args, **options):
        print('Бот запущен')
        run_bot()