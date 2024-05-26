from dash import html, dcc, Input, Output
import pandas as pd
import plotly.express as px
from config import teams_color

def load_data(file_path):
    """
    Load data from a CSV file with error handling.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The loaded DataFrame.

    Raises:
        Exception: If the file is not found, empty, or cannot be parsed.
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        raise Exception(f"The data file '{file_path}' was not found.")
    except pd.errors.EmptyDataError:
        raise Exception('The data file is empty.')
    except pd.errors.ParserError:
        raise Exception('Error parsing the data file.')
    return df

def format_stat_name(stat_name):
    """
    Format a statistic name to be more readable.

    Args:
        stat_name (str): The statistic name in snake_case.

    Returns:
        str: The formatted statistic name.
    """
    return ' '.join(word.capitalize() for word in stat_name.split('_'))

def create_tab_content(position, stats, top_players, df):
    """
    Create the HTML content for each position tab.

    Args:
        position (str): The position (e.g., 'RB', 'WR', 'TE', 'QB').
        stats (list): List of statistics to display.
        top_players (list): List of top players' names.
        df (pd.DataFrame): DataFrame containing the data for the position.

    Returns:
        html.Div: The HTML content for the position tab.
    """
    return html.Div([
        dcc.Graph(id=f'{position.lower()}-chart'),
        dcc.Dropdown(
            id=f'{position.lower()}-stat-dropdown',
            options=[{'label': format_stat_name(stat), 'value': stat} for stat in stats],
            value=stats[0],
            className='btn w-50 mb-4'
        ),
        dcc.Dropdown(
            id=f'{position.lower()}-player-dropdown',
            options=[{'label': player, 'value': player} for player in df['name'].unique()],
            value=top_players,
            multi=True,
            className='mb-3'
        )
    ], className='p-3')

def create_player_callback(app, position, df):
    """
    Create a callback for updating player charts based on the selected stat and player(s).

    Args:
        app (Dash): The Dash app instance.
        position (str): The position (e.g., 'RB', 'WR', 'TE', 'QB').
        df (pd.DataFrame): DataFrame containing the data for the position.

    Returns:
        function: The callback function for updating the chart.
    """
    @app.callback(
        Output(f'{position.lower()}-chart', 'figure'),
        [Input(f'{position.lower()}-stat-dropdown', 'value'),
         Input(f'{position.lower()}-player-dropdown', 'value')]
    )
    def update_chart(selected_stat, selected_players):
        """
        Update the player chart based on the selected stat and player(s).

        Args:
            selected_stat (str): The selected statistic to display.
            selected_players (list): The selected players' names.

        Returns:
            plotly.graph_objs._figure.Figure: The updated line chart figure.
        """
        filtered_df = df[df['name'].isin(selected_players)]
        fig = px.line(filtered_df, x='season', y=selected_stat, title=f'{position} {format_stat_name(selected_stat)} over Seasons', color='name', template='morph')
        for trace in fig.data:
            player_name = trace.name
            player_team = filtered_df[filtered_df['name'] == player_name]['team'].iloc[0]
            trace.line.color = teams_color[player_team]
        fig.update_traces(line=dict(width=3))
        fig.update_yaxes(title_text=format_stat_name(selected_stat))
        return fig
    return update_chart