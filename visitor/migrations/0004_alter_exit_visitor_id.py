# Generated by Django 4.2.1 on 2023-10-17 01:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("visitor", "0003_rename_visitor_exit_visitor_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exit",
            name="visitor_id",
            field=models.IntegerField(),
        ),
    ]