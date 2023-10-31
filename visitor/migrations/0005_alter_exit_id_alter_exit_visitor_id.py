# Generated by Django 4.2.1 on 2023-10-17 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("visitor", "0004_alter_exit_visitor_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exit",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="exit",
            name="visitor_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="visitor.visitor"
            ),
        ),
    ]