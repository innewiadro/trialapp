# Generated by Django 4.1.2 on 2022-11-24 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="side",
            field=models.IntegerField(
                choices=[(0, "Shipowner"), (1, "Contractor")], default=1
            ),
        ),
    ]
