# Generated by Django 3.2.6 on 2021-08-12 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('checked', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='todolist',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='TodoList',
        ),
    ]
