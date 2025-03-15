from django.db import models


class Teams(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "teams"

    def __str__(self):
        return self.name


class Leagues(models.Model):
    league_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    season = models.CharField(max_length=50)

    class Meta:
        db_table = "leagues"

    def __str__(self):
        return f"{self.name} ({self.season})"


class LeagueTeams(models.Model):
    league = models.ForeignKey("Leagues", on_delete=models.CASCADE)
    team = models.ForeignKey("Teams", on_delete=models.CASCADE)

    class Meta:
        db_table = "league_teams"
        unique_together = (("league", "team"),)

    def __str__(self):
        return f"{self.team.name} in {self.league.name}"


class Games(models.Model):
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

    STATUS_CHOICES = [
        (SCHEDULED, "Scheduled"),
        (IN_PROGRESS, "In Progress"),
        (COMPLETED, "Completed"),
        (CANCELLED, "Cancelled"),
    ]

    game_id = models.AutoField(primary_key=True)
    league = models.ForeignKey("Leagues", on_delete=models.CASCADE)
    home_team = models.ForeignKey(
        "Teams", on_delete=models.CASCADE, related_name="home_games"
    )
    away_team = models.ForeignKey(
        "Teams", on_delete=models.CASCADE, related_name="away_games"
    )
    youtube_url = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=SCHEDULED)
    home_score = models.IntegerField(default=0, blank=True, null=True)
    away_score = models.IntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = "games"

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} ({self.league.name})"


class Players(models.Model):
    player_id = models.AutoField(primary_key=True)
    team = models.ForeignKey("Teams", on_delete=models.CASCADE, related_name="players")
    name = models.CharField(max_length=100)
    jersey_number = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "players"
        unique_together = (("team", "jersey_number"),)

    def __str__(self):
        return f"{self.name} (#{self.jersey_number}, {self.team.name})"


class PlayerStats(models.Model):
    stat_id = models.AutoField(primary_key=True)
    game = models.ForeignKey(
        Games, on_delete=models.CASCADE, related_name="player_stats"
    )
    player = models.ForeignKey(
        "Players", on_delete=models.CASCADE, related_name="stats"
    )
    pts = models.IntegerField(default=0, blank=True, null=True)
    rebs = models.IntegerField(default=0, blank=True, null=True)
    asts = models.IntegerField(default=0, blank=True, null=True)
    stls = models.IntegerField(default=0, blank=True, null=True)
    blks = models.IntegerField(default=0, blank=True, null=True)
    turnovers = models.IntegerField(default=0, blank=True, null=True)
    fouls = models.IntegerField(default=0, blank=True, null=True)
    fg2m = models.IntegerField(default=0, blank=True, null=True)
    fg2a = models.IntegerField(default=0, blank=True, null=True)
    fg3m = models.IntegerField(default=0, blank=True, null=True)
    fg3a = models.IntegerField(default=0, blank=True, null=True)
    fgm = models.IntegerField(default=0, blank=True, null=True)
    fga = models.IntegerField(default=0, blank=True, null=True)
    ftm = models.IntegerField(default=0, blank=True, null=True)
    fta = models.IntegerField(default=0, blank=True, null=True)
    dnp = models.BooleanField(default=False, blank=True, null=True)
    fp = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.0, blank=True, null=True
    )

    class Meta:
        db_table = "player_stats"

    def __str__(self):
        return f"Stats for {self.player.name} in {self.game}"
