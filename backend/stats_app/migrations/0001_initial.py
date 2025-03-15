# Generated by Django 5.1.7 on 2025-03-15 00:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leagues',
            fields=[
                ('league_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('season', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'leagues',
            },
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('player_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('jersey_number', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'players',
            },
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'teams',
            },
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('game_id', models.AutoField(primary_key=True, serialize=False)),
                ('youtube_url', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(choices=[('scheduled', 'Scheduled'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='scheduled', max_length=20)),
                ('home_score', models.IntegerField(blank=True, default=0, null=True)),
                ('away_score', models.IntegerField(blank=True, default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats_app.leagues')),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_games', to='stats_app.teams')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_games', to='stats_app.teams')),
            ],
            options={
                'db_table': 'games',
            },
        ),
        migrations.CreateModel(
            name='PlayerStats',
            fields=[
                ('stat_id', models.AutoField(primary_key=True, serialize=False)),
                ('pts', models.IntegerField(blank=True, default=0, null=True)),
                ('rebs', models.IntegerField(blank=True, default=0, null=True)),
                ('asts', models.IntegerField(blank=True, default=0, null=True)),
                ('stls', models.IntegerField(blank=True, default=0, null=True)),
                ('blks', models.IntegerField(blank=True, default=0, null=True)),
                ('turnovers', models.IntegerField(blank=True, default=0, null=True)),
                ('fouls', models.IntegerField(blank=True, default=0, null=True)),
                ('fg2m', models.IntegerField(blank=True, default=0, null=True)),
                ('fg2a', models.IntegerField(blank=True, default=0, null=True)),
                ('fg3m', models.IntegerField(blank=True, default=0, null=True)),
                ('fg3a', models.IntegerField(blank=True, default=0, null=True)),
                ('fgm', models.IntegerField(blank=True, default=0, null=True)),
                ('fga', models.IntegerField(blank=True, default=0, null=True)),
                ('ftm', models.IntegerField(blank=True, default=0, null=True)),
                ('fta', models.IntegerField(blank=True, default=0, null=True)),
                ('dnp', models.BooleanField(blank=True, default=False, null=True)),
                ('fp', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_stats', to='stats_app.games')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stats', to='stats_app.players')),
            ],
            options={
                'db_table': 'player_stats',
            },
        ),
        migrations.AddField(
            model_name='players',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='stats_app.teams'),
        ),
        migrations.AlterUniqueTogether(
            name='players',
            unique_together={('team', 'jersey_number')},
        ),
        migrations.CreateModel(
            name='LeagueTeams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats_app.leagues')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats_app.teams')),
            ],
            options={
                'db_table': 'league_teams',
                'unique_together': {('league', 'team')},
            },
        ),
    ]
