# Generated by Django 4.1.2 on 2022-12-08 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trials", "0008_alter_docktrial_trial_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="docktrial",
            name="trial_status",
            field=models.CharField(
                choices=[
                    ("Not Started", "Not Started"),
                    (1, "Accepted with Comments"),
                    (2, "Accepted"),
                    (3, "Not accepted"),
                ],
                default="Not Started",
                max_length=155,
            ),
        ),
    ]
