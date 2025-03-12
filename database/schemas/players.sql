CREATE TABLE players (
    player_id SERIAL PRIMARY KEY,
    team_id INTEGER NOT NULL,
    name VARCHAR(100) NOT NULL,
    jersey_number INTEGER,
    FOREIGN KEY (team_id) REFERENCES teams(team_id),
    UNIQUE (team_id, jersey_number)
);