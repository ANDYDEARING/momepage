# Generated by Django 2.2.3 on 2019-07-12 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20190711_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='week_day_number',
            field=models.IntegerField(default=1, help_text='Enter the number of the day of the week here.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='day',
            name='week_number',
            field=models.IntegerField(default=1, help_text='Enter the number of the week here.'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='day',
            name='number',
            field=models.IntegerField(help_text='Enter the overall number of the day here.'),
        ),
    ]