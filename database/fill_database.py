import csv
import io

def load_csv(archive_file, csv_file, connection, insert_sql, parameters_sql):
    with archive_file.open(csv_file) as binary_file:
        with io.TextIOWrapper(binary_file, encoding = 'utf-8-sig', newline = '') as text_file:
            reader = csv.DictReader(text_file)

            for row in reader:
                parameters = parameters_sql(row)
                connection.execute(insert_sql, parameters)


def fill_tables(connection, archive_file):
    load_csv(archive_file = archive_file, csv_file = 'seasons.csv', connection = connection,
            insert_sql = 'INSERT INTO seasons VALUES (?, ?)',
            parameters_sql = lambda row: (
                row['url'],
                int(row['year'])
            )
    )

    load_csv(archive_file = archive_file, csv_file = 'status.csv', connection = connection,
            insert_sql = 'INSERT INTO status VALUES (?, ?)',
            parameters_sql = lambda row: (
                int(row['statusId']),
                row['status']
            )
    )

    load_csv(archive_file = archive_file, csv_file = 'drivers.csv', connection = connection,
            insert_sql = 'INSERT INTO drivers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
            parameters_sql = lambda row: (
                int(row['driverId']),
                row['driverRef'],
                None if row['number'] == r'\N' else int(row['number']),
                None if row['code'] == r'\N' else row['code'],
                row['forename'],
                row['surname'],
                row['dob'],
                row['nationality'],
                row['url']
            )
    )

    load_csv(archive_file = archive_file, csv_file = 'circuits.csv', connection = connection,
            insert_sql = 'INSERT INTO circuits VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
            parameters_sql = lambda row: (
                int(row['circuitId']),
                row['circuitRef'],
                row['name'],
                row['location'],
                row['country'],
                float(row['lat']),
                float(row['lng']),
                int(row['alt']),
                row['url']
            )
    )

    load_csv(archive_file = archive_file, csv_file = 'constructors.csv', connection = connection,
            insert_sql = 'INSERT INTO constructors VALUES (?, ?, ?, ?, ?)',
            parameters_sql = lambda row: (
                int(row['constructorId']),
                row['constructorRef'],
                row['name'],
                row['nationality'],
                row['url']
            )
    )

    load_csv(archive_file = archive_file, csv_file = 'races.csv', connection = connection,
            insert_sql = 'INSERT INTO races VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            parameters_sql = lambda row: (
                int(row['raceId']),
                int(row['year']),
                int(row['round']),
                int(row['circuitId']),
                row['name'],
                row['date'],
                row['time'],
                row['url'],
                None if row['fp1_date'] == r'\N' else row['fp1_date'],
                None if row['fp1_time'] == r'\N' else row['fp1_time'],
                None if row['fp2_date'] == r'\N' else row['fp2_date'],
                None if row['fp2_time'] == r'\N' else row['fp2_time'],
                None if row['fp3_date'] == r'\N' else row['fp3_date'],
                None if row['fp3_time'] == r'\N' else row['fp3_time'],
                None if row['quali_date'] == r'\N' else row['quali_date'],
                None if row['quali_time'] == r'\N' else row['quali_time'],
                None if row['sprint_date'] == r'\N' else row['sprint_date'],
                None if row['sprint_time'] == r'\N' else row['sprint_time']
            )
    )

    load_csv(archive_file = archive_file, csv_file = 'sprint_results.csv', connection = connection,
            insert_sql = 'INSERT INTO sprint_results VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            parameters_sql = lambda row: (
                int(row['resultId']),
                int(row['raceId']),
                int(row['driverId']),
                int(row['constructorId']),

                int(row['number']),
                int(row['grid']),

                None if row['position'] == r'\N' else int(row['position']),
                row['positionText'],
                int(row['positionOrder']),

                float(row['points']),
                int(row['laps']),

                None if row['time'] == r'\N' else row['time'],
                None if row['milliseconds'] == r'\N' else int(row['milliseconds']),

                None if row['fastestLap'] == r'\N' else int(row['fastestLap']),
                None if row['fastestLapTime'] == r'\N' else row['fastestLapTime'],

                int(row['statusId'])
            )
    )

    load_csv(archive_file = archive_file, csv_file = 'results.csv', connection = connection,
            insert_sql = 'INSERT INTO results VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            parameters_sql = lambda row: (
                int(row['resultId']),
                int(row['raceId']),
                int(row['driverId']),
                int(row['constructorId']),

                None if row['number'] == r'\N' else int(row['number']),
                int(row['grid']),

                None if row['position'] == r'\N' else int(row['position']),
                row['positionText'],
                int(row['positionOrder']),

                float(row['points']),
                int(row['laps']),

                None if row['time'] == r'\N' else row['time'],
                None if row['milliseconds'] == r'\N' else int(row['milliseconds']),
                None if row['fastestLap'] == r'\N' else int(row['fastestLap']),
                None if row['rank'] == r'\N' else int(row['rank']),
                None if row['fastestLapTime'] == r'\N' else row['fastestLapTime'],
                None if row['fastestLapSpeed'] == r'\N' else float(row['fastestLapSpeed']),

                int(row['statusId'])
            )
    )

    load_csv(archive_file = archive_file, csv_file = 'qualifying.csv', connection = connection,
            insert_sql = 'INSERT INTO qualifying VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
            parameters_sql = lambda row: (
                int(row['qualifyId']),
                int(row['raceId']),
                int(row['driverId']),
                int(row['constructorId']),

                int(row['number']),
                int(row['position']),

                None if row['q1'] == r'\N' else row['q1'],
                None if row['q2'] == r'\N' else row['q2'],
                None if row['q3'] == r'\N' else row['q3']
            )
    )

    load_csv(archive_file = archive_file, csv_file = 'constructor_results.csv', connection = connection,
            insert_sql = 'INSERT INTO constructor_results VALUES (?, ?, ?, ?, ?)',
            parameters_sql = lambda row: (
                int(row['constructorResultsId']),
                int(row['raceId']),
                int(row['constructorId']),
                float(row['points']),
                None if row['status'] == r'\N' else row['status']
            )
    )

    load_csv(archive_file = archive_file, csv_file = 'constructor_standings.csv', connection = connection,
            insert_sql = 'INSERT INTO constructor_standings VALUES (?, ?, ?, ?, ?, ?, ?)',
            parameters_sql = lambda row: (
                int(row['constructorStandingsId']),
                int(row['raceId']),
                int(row['constructorId']),

                float(row['points']),

                int(row['position']),
                row['positionText'],
                int(row['wins'])
            )
    )

    load_csv(archive_file = archive_file, csv_file = 'driver_standings.csv', connection = connection,
            insert_sql = 'INSERT INTO driver_standings VALUES (?, ?, ?, ?, ?, ?, ?)',
            parameters_sql = lambda row: (
                int(row['driverStandingsId']),
                int(row['raceId']),
                int(row['driverId']),

                float(row['points']),

                int(row['position']),
                row['positionText'],
                int(row['wins'])
            )
    )
