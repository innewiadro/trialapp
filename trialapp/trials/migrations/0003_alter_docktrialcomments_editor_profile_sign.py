# Generated by Django 4.1.2 on 2022-11-24 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trials", "0002_alter_docktrialcomments_editor_profile_sign"),
    ]

    operations = [
        migrations.AlterField(
            model_name="docktrialcomments",
            name="editor_profile_sign",
            field=models.TextField(blank=True),
        ),
    ]