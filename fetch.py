import sqlite3
import gradio as gr
import pandas as pd

#he wants... the names and cities of all the teams left in the playoffs rn.
def fetch_teams(): 
    conn = sqlite3.connect('football.db')

    cursor = conn.cursor()

    query = """
        SELECT * FROM playoffTeams;
    """

    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()

    #plot the number of characters in each word of the output
    points = []
    for team in results:
        points.append((len(team[1]),len(team[2])))

    df = pd.DataFrame(points,columns=['city','team'])

    return df

iface = gr.Interface(
    fn = fetch_teams,
    inputs = [],
    outputs = gr.ScatterPlot(x='city',y='team',x_lim=(0,15),y_lim=(0,15))
    )

iface.launch()