# Generated by Django 4.2.6 on 2023-10-09 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ray', '0003_alter_uslugi_body_alter_uslugi_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uslugi',
            name='name',
            field=models.TextField(max_length=20, verbose_name='заголовок'),
        ),
    ]