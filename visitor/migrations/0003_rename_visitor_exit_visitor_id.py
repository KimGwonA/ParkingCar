# Generated by Django 4.2.1 on 2023-10-17 01:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("visitor", "0002_alter_exit_id_alter_exit_visitor"),
    ]

    operations = [
        migrations.RenameField(
            model_name="exit",
            old_name="visitor",
            new_name="visitor_id",
        ),
    ]
