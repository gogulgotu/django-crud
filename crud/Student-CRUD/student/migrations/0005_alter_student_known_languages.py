# Generated by Django 5.0 on 2023-12-29 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_student_known_languages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='known_languages',
            field=models.BooleanField(choices=[('1', 'Tamil'), ('2', 'English'), ('3', 'Hindi')], default=True, max_length=1),
        ),
    ]