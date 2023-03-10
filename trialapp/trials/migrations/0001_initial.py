# Generated by Django 4.1.2 on 2022-11-24 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0002_profile_side"),
    ]

    operations = [
        migrations.CreateModel(
            name="DockTrial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("trial_name", models.CharField(max_length=200)),
                ("trial_number", models.CharField(max_length=5, null=True)),
                (
                    "trial_status",
                    models.IntegerField(
                        choices=[
                            (0, "Not Started"),
                            (1, "Accepted with Comments"),
                            (2, "Accepted"),
                            (3, "Not accepted"),
                        ],
                        default=0,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DockTrialComments",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("pub_date", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(max_length=255, null=True)),
                (
                    "status",
                    models.IntegerField(choices=[(0, "Open"), (1, "Close")], default=0),
                ),
                ("date_of_last_change", models.DateTimeField(auto_now=True)),
                (
                    "department",
                    models.IntegerField(
                        choices=[
                            (0, "HPD"),
                            (1, "PID"),
                            (2, "OD"),
                            (3, "ED"),
                            (4, "CD"),
                            (5, "QCD"),
                            (6, "P&L"),
                            (7, "PD"),
                            (8, "DO"),
                            (9, "S"),
                            (10, "CO"),
                        ],
                        default=10,
                    ),
                ),
                ("contractor_comment", models.TextField(blank=True)),
                ("design_comment", models.TextField(blank=True)),
                ("shipowner_comment", models.TextField(blank=True)),
                ("description", models.TextField(null=True)),
                (
                    "editor_profile_sign",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.profile",
                    ),
                ),
                (
                    "name_dock_trial",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="trials.docktrial",
                    ),
                ),
            ],
        ),
    ]
