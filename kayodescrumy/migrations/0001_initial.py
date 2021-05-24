# Generated by Django 3.1.6 on 2021-05-23 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GoalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ScrumyGoals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_name', models.TextField()),
                ('goal_id', models.IntegerField()),
                ('created_by', models.TextField()),
                ('moved_by', models.TextField()),
                ('owner', models.TextField()),
                ('goal_status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kayodescrumy.goalstatus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ScrumyHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moved_by', models.TextField()),
                ('created_by', models.TextField()),
                ('moved_from', models.TextField()),
                ('moved_to', models.TextField()),
                ('time_of_action', models.TextField()),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kayodescrumy.scrumygoals')),
            ],
        ),
    ]