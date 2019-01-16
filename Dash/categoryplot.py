import plotly.graph_objs as go
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://jamal:jamaludin@localhost/titanic?host=localhost?port=3306")
conn = engine.connect()
result = conn.execute("SELECT * from titanic").fetchall()

dfPokemon = pd.DataFrame(result)

ListFunc = {
    "bar" : go.Bar,
    "box" : go.Box,
    "violin" : go.Violin
}


def getPlot(jenis):
    return[ListFunc[jenis](
                x=dfPokemon['fare'],
                y=dfPokemon['survived'],
                text=dfPokemon['fare'],
                opacity=0.7,
                name='Total'
            ),
                ListFunc[jenis](
                x=dfPokemon['fare'],
                y=dfPokemon['age'],
                text=dfPokemon['survived'],
                opacity=0.7,
                name='Attack'
            )]