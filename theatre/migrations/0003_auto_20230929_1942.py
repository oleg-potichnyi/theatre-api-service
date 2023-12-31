# Generated by Django 4.2.5 on 2023-09-29 16:42

from django.db import migrations
from django.db.migrations import RunPython


def func(apps, schema_editor):
    from django.core.management import call_command

    call_command("loaddata", "fixture_data.json")


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("theatre", "0002_initial"),
    ]

    operations = [RunPython(func, reverse_func)]
