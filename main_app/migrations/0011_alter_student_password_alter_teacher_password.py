# Generated by Django 4.1.2 on 2022-10-28 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_student_password_alter_student_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='password',
            field=models.TextField(null=True),
        ),
    ]
