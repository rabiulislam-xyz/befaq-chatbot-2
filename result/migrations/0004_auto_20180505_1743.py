# Generated by Django 2.0.4 on 2018-05-05 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0003_proxy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proxy',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='result',
            options={'ordering': ['-student_roll', 'student_marhala', '-exam_year']},
        ),
    ]