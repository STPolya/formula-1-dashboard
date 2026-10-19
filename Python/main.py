from pathlib import Path
import pandas as pd
import sqlite3
import plotly.express as px

PARENT_FOLDER = Path(__file__).parent.parent
BD_PATH = PARENT_FOLDER / 'Database' / 'f1.db'


try:
    connection = sqlite3.connect(BD_PATH)

except Exception as e:
    print(e)

finally:
    connection.close()

