# Generated by Django 2.2.2 on 2019-07-13 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userman', '0003_answers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answers',
            old_name='question_id',
            new_name='question',
        ),
    ]
