# Generated by Django 3.1.6 on 2021-02-16 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20210216_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.CharField(choices=[('TC', 'Technology'), ('BG', 'Bugs'), ('MN', 'Money')], default='TC', max_length=2),
        ),
    ]