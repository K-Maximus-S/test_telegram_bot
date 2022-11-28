from django.db import models


class Expenses_needs(models.Model):
    """Таблица расходов раздела"""

    id = models.BigAutoField(primary_key=True)
    codename = models.CharField(max_length=50, verbose_name='Название раздела (Потребности|Инвестиции|Желания')
    category = models.CharField(max_length=50, verbose_name='Название категории (еда,жилье,тс, итд')
    aliases = models.CharField(max_length=50, verbose_name='Название алиаса (магазин:продукты:итд')
    price = models.IntegerField(verbose_name='Цена')
    quantity = models.IntegerField(null=True, blank=True, verbose_name='Количество') # TODO нужно будет сделать поле необязательным
    data_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')
    raw_text = models.TextField(verbose_name='Полный текст сообщения')

    # def __str__(self):
    #     return self.raw_text


class Aliases(models.Model):
    """Таблица алиасов """

    id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=50, db_index=True, verbose_name='Название категории (еда,жилье,тс, итд')
    codename = models.CharField(max_length=50, db_index=True, verbose_name='Название раздела (Потребности|Инвестиции|Желания')
    aliases_list = models.TextField(verbose_name='Список алиасов передается через -> : ')

    # def __str__(self):
    #     return self.list_of_words

class User_verification(models.Model):
    """Таблица Аутентификации пользователя"""

    id = models.BigAutoField(primary_key=True)
    user_id = models.CharField(max_length=50, verbose_name='ID пользователя из телеграма')
    activating_bot = models.CharField(max_length=50, verbose_name='Активация бота: True - есть цели, False - нет целей')

class Purposes(models.Model):
    """Таблица целей"""
    id = models.BigAutoField(primary_key=True)
    id_user_tg = models.CharField(max_length=15, verbose_name='id пользователя телеграм')
    codename = models.CharField(max_length=50, verbose_name='Название раздела (Потребности|Инвестиции|Желания')
    category = models.CharField(max_length=50, verbose_name='Название категории (еда,жилье,тс, итд')
    aliases = models.CharField(max_length=50, verbose_name='Название алиаса (магазин:продукты:итд')
    price = models.IntegerField(verbose_name='Цена')
    data = models.CharField(max_length=15, verbose_name='Дата')