# Generated by Django 4.1.2 on 2022-12-07 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("trials", "0005_alter_docktrial_table"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="docktrial",
            table="docktrials",
        ),
    ]