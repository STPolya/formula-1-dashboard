def history_sql_queries():
    return {
        'drivers_titles': """
            WITH last_rounds AS (
                SELECT year, MAX(round) AS last_round
                FROM races
                WHERE year BETWEEN ? AND ?
                GROUP BY year
            ),
            champions AS (
                SELECT races.year, driver_standings.driverId
                FROM races
                      JOIN last_rounds ON races.year = last_rounds.year AND races.round = last_rounds.last_round
                      JOIN driver_standings ON driver_standings.raceId = races.raceId
                WHERE driver_standings.position = 1
            )
            SELECT drivers.driverId, drivers.forename || ' ' || drivers.surname AS driver_name, COUNT(DISTINCT champions.year) AS titles
            FROM champions
            JOIN drivers ON drivers.driverId = champions.driverId
            GROUP BY drivers.driverId, drivers.forename, drivers.surname
            ORDER BY titles DESC, driver_name
            LIMIT 10
        """,
        'constructors_titles': """
            WITH last_rounds AS (
                SELECT year, MAX(round) AS last_round
                FROM races
                WHERE year BETWEEN ? AND ?
                GROUP BY year
            ),
            champions AS (
                SELECT races.year, constructor_standings.constructorId
                FROM races
                JOIN last_rounds ON races.year = last_rounds.year AND races.round = last_rounds.last_round
                JOIN constructor_standings ON constructor_standings.raceId = races.raceId
                WHERE constructor_standings.position = 1
            )
            SELECT constructors.constructorId, constructors.name, COUNT(DISTINCT champions.year) AS titles
            FROM champions
            JOIN constructors ON constructors.constructorId = champions.constructorId
            GROUP BY constructors.constructorId, constructors.name
            ORDER BY titles DESC, constructors.name
            LIMIT 10
        """,

        'count_races': """
            SELECT count(races.raceId) AS count_races
            FROM races
            WHERE year BETWEEN ? AND ?
        """,
        'count_seasons': """
            SELECT count(distinct races.year) AS count_seasons
            FROM races
            WHERE year BETWEEN ? AND ?
        """,
        'count_teams': """
            SELECT count(distinct results.constructorId) AS count_teams
            FROM results
            JOIN races ON results.raceId = races.raceId
            WHERE year BETWEEN ? AND ?
        """,
        'count_drivers': """
            SELECT count(distinct results.driverId) AS count_drivers
            FROM results
            JOIN races ON results.raceId = races.raceId
            WHERE year BETWEEN ? AND ?
        """,
        'count_sprints': """
            SELECT count(distinct sprint_results.raceId) AS count_sprints
            FROM sprint_results
            JOIN races ON sprint_results.raceId = races.raceId
            WHERE year BETWEEN ? AND ?
        """,
    }

def season_21_sql_queries():
    pass

def drivers_sql_queries():
    pass

def teams_sql_queries():
    pass