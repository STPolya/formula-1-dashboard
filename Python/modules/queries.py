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
    return {
        'team_champions': """
            SELECT constructors.name, constructor_standings.points
            FROM races
            JOIN constructor_standings ON races.raceId = constructor_standings.raceId
            JOIN constructors ON constructor_standings.constructorId = constructors.constructorId
            WHERE races.year = 2021 AND races.round = (SELECT MAX(round) FROM races WHERE year = 2021)
            ORDER BY constructor_standings.points DESC
        """,

        'driver_champions': """
            SELECT drivers.surname, driver_standings.points
            FROM races
            JOIN driver_standings ON races.raceId = driver_standings.raceId
            JOIN drivers ON driver_standings.driverId = drivers.driverId
            WHERE races.year = 2021 AND races.round = (SELECT MAX(round) FROM races WHERE year = 2021)
            ORDER BY driver_standings.points DESC
        """,

        'drivers_points_dynamic': """
            SELECT drivers.surname, driver_standings.points, races.date || ', ' || circuits.name AS date_place
            FROM races
            JOIN driver_standings ON races.raceId = driver_standings.raceId
            JOIN drivers ON driver_standings.driverId = drivers.driverId AND drivers.surname IN ('Verstappen', 'Hamilton', 'Bottas')
            JOIN circuits ON races.circuitId = circuits.circuitId
            where year = 2021
            ORDER BY date ASC
        """,

        'teams_points_dynamic': """
            SELECT constructors.name, constructor_standings.points, races.date || ', ' || circuits.name AS date_place
            FROM races
            JOIN constructor_standings ON races.raceId = constructor_standings.raceId
            JOIN constructors ON constructor_standings.constructorId = constructors.constructorId AND constructors.name IN ('Ferrari', 'Mercedes', 'Red Bull')
            JOIN circuits ON races.circuitId = circuits.circuitId
            where year = 2021
            ORDER BY date ASC
        """,

        'geography': """
            SELECT circuits.country
            FROM circuits
            JOIN races ON circuits.circuitId = races.circuitId AND races.year = 2021
        """,

        'drivers_count_wins': """
            WITH list_drivers AS (
                SELECT DISTINCT drivers.surname, drivers.driverId
                FROM drivers
                JOIN driver_standings ON drivers.driverId = driver_standings.driverId
                JOIN races ON driver_standings.raceId = races.raceId
                WHERE races.year = 2021
            ),
            season_results AS (
                    SELECT results.driverId, results.position
                    FROM results
                    JOIN races ON results.raceId = races.raceId
                    WHERE races.year = 2021
                    AND results.position BETWEEN 1 AND 3
            )
            SELECT list_drivers.surname, COUNT(season_results.position) AS podiums
            FROM list_drivers
            LEFT JOIN season_results ON list_drivers.driverId = season_results.driverId
            GROUP BY list_drivers.driverId, list_drivers.surname
            ORDER BY podiums DESC
        """,

        'teams_count_wins': """
            WITH list_team AS (
                SELECT DISTINCT constructors.name, constructors.constructorId
                FROM constructors
                JOIN constructor_standings ON constructors.constructorId = constructor_standings.constructorId
                JOIN races ON constructor_standings.raceId = races.raceId
                WHERE races.year = 2021
            ),
            season_results AS (
                SELECT results.constructorId, results.position
                FROM results
                JOIN races ON results.raceId = races.raceId
                WHERE races.year = 2021 AND results.position BETWEEN 1 AND 3
            )
            SELECT list_team.name, COUNT(season_results.position) AS podiums
            FROM list_team
            LEFT JOIN season_results ON list_team.constructorId = season_results.constructorId
            GROUP BY list_team.constructorId, list_team.name
            ORDER BY podiums DESC
        """,
    }

def drivers_sql_queries():
    pass

def teams_sql_queries():
    pass






