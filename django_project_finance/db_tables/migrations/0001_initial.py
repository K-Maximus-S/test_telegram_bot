# Generated by Django 4.1.2 on 2022-11-12 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Aliases",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "category",
                    models.CharField(
                        db_index=True,
                        max_length=50,
                        verbose_name="Название категории (еда,жилье,тс, итд",
                    ),
                ),
                (
                    "codename",
                    models.CharField(
                        db_index=True,
                        max_length=50,
                        verbose_name="Название раздела (Потребности|Инвестиции|Желания",
                    ),
                ),
                (
                    "aliases_list",
                    models.TextField(
                        verbose_name="Список алиасов передается через -> : "
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Expenses_needs",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "codename",
                    models.CharField(
                        max_length=50,
                        verbose_name="Название раздела (Потребности|Инвестиции|Желания",
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        max_length=50,
                        verbose_name="Название категории (еда,жилье,тс, итд",
                    ),
                ),
                (
                    "aliases",
                    models.CharField(
                        max_length=50,
                        verbose_name="Название алиаса (магазин:продукты:итд",
                    ),
                ),
                ("price", models.IntegerField(verbose_name="Цена")),
                (
                    "quantity",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Количество"
                    ),
                ),
                (
                    "data_time",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата и время"
                    ),
                ),
                ("raw_text", models.TextField(verbose_name="Полный текст сообщения")),
            ],
        ),
    ]
