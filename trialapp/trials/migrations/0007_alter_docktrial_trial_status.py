# Generated by Django 4.1.2 on 2022-12-07 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trials", "0006_alter_docktrial_table"),
    ]

    operations = [
        migrations.AlterField(
            model_name="docktrial",
            name="trial_status",
            field=models.IntegerField(
                choices=[
                    (0, "Not Started"),
                    (1, "Accepted with Comments"),
                    (2, "Accepted"),
                    (3, "Not accepted"),
                    ("aa", "aa"),
                ],
                default=0,
            ),
        ),
    ]