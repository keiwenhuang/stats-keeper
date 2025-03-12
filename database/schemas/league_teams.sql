CREATE TABLE league_teams (
    league_id INTEGER NOT NULL,
    team_id INTEGER NOT NULL,
    PRIMARY KEY (league_id, team_id),
    FOREIGN KEY (league_id) REFERENCES leagues(league_id),
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
);