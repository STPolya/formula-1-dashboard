def create_tables(connection):
    connection.executescript("""
        DROP TABLE IF EXISTS sprint_results;
        DROP TABLE IF EXISTS results;
        DROP TABLE IF EXISTS qualifying;
        DROP TABLE IF EXISTS constructor_results;
        DROP TABLE IF EXISTS constructor_standings;
        DROP TABLE IF EXISTS driver_standings;
        DROP TABLE IF EXISTS races;
        DROP TABLE IF EXISTS drivers;
        DROP TABLE IF EXISTS constructors;
        DROP TABLE IF EXISTS circuits;
        DROP TABLE IF EXISTS seasons;
        DROP TABLE IF EXISTS status;
    
        CREATE TABLE seasons (
            url TEXT,
            year INTEGER
        );
    
        CREATE TABLE status (
            statusId INTEGER PRIMARY KEY,
            status TEXT
        );
    
        CREATE TABLE drivers (
            driverId INTEGER PRIMARY KEY,
            driverRef TEXT,
            number INTEGER,
            code TEXT CHECK (length(code) = 3),
            forename TEXT,
            surname TEXT,
            dob TEXT,
            nationality TEXT,
            url TEXT
        );
    
        CREATE TABLE circuits (
            circuitId INTEGER PRIMARY KEY,
            circuitRef TEXT,
            name TEXT,
            location TEXT,
            country TEXT,
            lat REAL,
            lng REAL,
            alt INTEGER,
            url TEXT
        );
    
        CREATE TABLE constructors (
            constructorId INTEGER PRIMARY KEY,
            constructorRef TEXT,
            name TEXT,
            nationality TEXT,
            url TEXT
        );
    
        CREATE TABLE races (
            raceId INTEGER PRIMARY KEY,
            year INTEGER,
            round INTEGER,
            circuitId INTEGER,
            name TEXT,
            date TEXT,
            time TEXT,
            url TEXT,
            fp1_date TEXT,
            fp1_time TEXT,
            fp2_date TEXT,
            fp2_time TEXT,
            fp3_date TEXT,
            fp3_time TEXT,
            quali_date TEXT,
            quali_time TEXT,
            sprint_date TEXT,
            sprint_time TEXT,
    
            CONSTRAINT FK_races_circuits FOREIGN KEY(circuitId) REFERENCES circuits(circuitId)
        );
    
        CREATE TABLE sprint_results (
            resultId INTEGER PRIMARY KEY,
            raceId INTEGER,
            driverId INTEGER,
            constructorId INTEGER,
    
            number INTEGER,
            grid INTEGER,
    
            position INTEGER,
            positionText TEXT,
            positionOrder INTEGER,
    
            points REAL,
            laps INTEGER,
    
            time TEXT,
            milliseconds INTEGER,
            fastestLap INTEGER,
            fastestLapTime TEXT,
    
            statusId INTEGER,
    
            CONSTRAINT FK_sprints_races FOREIGN KEY(raceId) REFERENCES races(raceId),
            CONSTRAINT FK_sprints_drivers FOREIGN KEY(driverId) REFERENCES drivers(driverId),
            CONSTRAINT FK_sprints_constructors FOREIGN KEY(constructorId) REFERENCES constructors(constructorId),
            CONSTRAINT FK_sprints_status FOREIGN KEY(statusId) REFERENCES status(statusId)
        );
    
        CREATE TABLE results (
            resultId INTEGER PRIMARY KEY,
            raceId INTEGER,
            driverId INTEGER,
            constructorId INTEGER,
    
            number INTEGER,
            grid INTEGER,
    
            position INTEGER,
            positionText TEXT,
            positionOrder INTEGER,
    
            points REAL,
            laps INTEGER,
    
            time TEXT,
            milliseconds INTEGER,
            fastestLap INTEGER,
            rank INTEGER,
            fastestLapTime TEXT,	
            fastestLapSpeed REAL,
    
            statusId INTEGER,
    
            CONSTRAINT FK_results_races FOREIGN KEY(raceId) REFERENCES races(raceId),    
            CONSTRAINT FK_results_drivers FOREIGN KEY(driverId) REFERENCES drivers(driverId),
            CONSTRAINT FK_results_constructors FOREIGN KEY(constructorId) REFERENCES constructors(constructorId),
            CONSTRAINT FK_results_status FOREIGN KEY(statusId) REFERENCES status(statusId)
        );
    
        CREATE TABLE qualifying (
            qualifyId INTEGER PRIMARY KEY,
            raceId INTEGER,
            driverId INTEGER,
            constructorId INTEGER,
    
            number INTEGER,
            position INTEGER,
            q1 TEXT,
            q2 TEXT,
            q3 TEXT,
    
            CONSTRAINT FK_qualifying_races FOREIGN KEY(raceId) REFERENCES races(raceId),
            CONSTRAINT FK_qualifying_drivers FOREIGN KEY(driverId) REFERENCES drivers(driverId),
            CONSTRAINT FK_qualifying_constructors FOREIGN KEY(constructorId) REFERENCES constructors(constructorId)
        );
    
        CREATE TABLE constructor_results (
            constructorResultsId INTEGER PRIMARY KEY,
            raceId INTEGER, 
            constructorId INTEGER, 
            points REAL,
            status TEXT,
    
            CONSTRAINT FK_constructor_results_races FOREIGN KEY(raceId) REFERENCES races(raceId),
            CONSTRAINT FK_constructor_results_constructors FOREIGN KEY(constructorId) REFERENCES constructors(constructorId)
        );
    
        CREATE TABLE constructor_standings (
            constructorStandingsId INTEGER PRIMARY KEY,
            raceId INTEGER,
            constructorId INTEGER,
    
            points REAL,
    
            position INTEGER,
            positionText TEXT,
            wins INTEGER,
    
            CONSTRAINT FK_constructor_standings_races FOREIGN KEY(raceId) REFERENCES races(raceId),
            CONSTRAINT FK_constructor_standings_constructors FOREIGN KEY(constructorId) REFERENCES constructors(constructorId)
        );
    
        CREATE TABLE driver_standings (
            driverStandingsId INTEGER PRIMARY KEY,
            raceId INTEGER,
            driverId INTEGER,
    
            points REAL,
    
            position INTEGER,
            positionText TEXT,
            wins INTEGER,
    
            CONSTRAINT FK_driver_standings_races FOREIGN KEY(raceId) REFERENCES races(raceId),
            CONSTRAINT FK_driver_standings_drivers FOREIGN KEY(driverId) REFERENCES drivers(driverId)
        )
    """)

