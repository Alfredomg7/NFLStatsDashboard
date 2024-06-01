from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from utilities import load_data, format_stat_name, create_tab_content, create_player_callback
from config import rb_stats, wr_te_stats, qb_stats, team_stats, teams_color

# Load data with error handling
file_path = 'data/offense_yearly_data.csv'
df = load_data(file_path)

# Initialize dash app with bootstrap theme
load_figure_template('morph')
app = Dash(__name__, external_stylesheets=[dbc.themes.MORPH])

# Filter data for each position
df_rb = df[df['position'] == 'RB']
df_wr = df[df['position'] == 'WR']
df_te = df[df['position'] == 'TE']
df_qb = df[df['position'] == 'QB']

# Filter data for each position and select top 10 based on key stats
top_rb = df_rb.groupby('name').sum().reset_index().nlargest(10, 'rushing_yards')['name'].tolist()
top_wr = df_wr.groupby('name').sum().reset_index().nlargest(10, 'receiving_yards')['name'].tolist()
top_te = df_te.groupby('name').sum().reset_index().nlargest(10, 'receiving_yards')['name'].tolist()
top_qb = df_qb.groupby('name').sum().reset_index().nlargest(10, 'passing_yards')['name'].tolist()

# Calculate the min and max year values
min_year = df['season'].min()
max_year = df['season'].max()

# Pre-aggregate data by team and year
team_yearly_stats = df.groupby(['team', 'season']).sum().reset_index()

# Create HTML Components
app.layout = html.Div([
    html.H1(f'NFL Offense Stats {min_year}-{max_year}', className='text-center pb-3'),
    html.Div([
        html.Div([
            html.H2('Offense Players Stats by Position', className='text-center pb-3'),
            dcc.Tabs(id='position-tabs', value='RB', className='nav nav-pills', children=[
                dcc.Tab(
                    label='Running Backs',
                    value='RB',
                    className='nav-item',
                    children=create_tab_content('RB', rb_stats, top_rb, df_rb)
                ),
                dcc.Tab(
                    label='Wide Receivers',
                    value='WR',
                    className='nav-item',
                    children=create_tab_content('WR', wr_te_stats, top_wr, df_wr)
                ),
                dcc.Tab(
                    label='Tight Ends',
                    value='TE',
                    className='nav-item',
                    children=create_tab_content('TE', wr_te_stats, top_te, df_te)
                ),
                dcc.Tab(
                    label='Quarterbacks',
                    value='QB',
                    className='nav-item',
                    children=create_tab_content('QB', qb_stats, top_qb, df_qb)
                )
            ])
        ], className='col-12 col-xl-6 px-5'),
        html.Div([
            html.H2('Team Stats by Season', className='text-center pb-3'),
            dcc.Tabs(id='bar-chart-year-tabs', value=f'year-{max_year}', className='nav nav-pills', children=[
                dcc.Tab(label=str(year), value=f'year-{year}', className='nav-item') for year in range(min_year, max_year + 1)
            ]),
            html.Div([
                dcc.Graph(id='team-bar-chart'),
                dcc.Dropdown(
                    id='team-stat-dropdown',
                    options=[{'label': format_stat_name(stat), 'value': stat} for stat in team_stats],
                    value='total_yards',
                    className='btn w-50 mb-3')
            ], className='p-3')
        ], className='col-12 col-xl-6 px-5')
    ], className='row'),
    html.Div([
        html.Div([
            html.H2('Offense Stats Distribution', className='text-center pb-3'),
            dcc.Tabs(id='histogram-year-tabs', value=f'histogram-year-{max_year}', className='nav nav-pills', children=[
                dcc.Tab(label=str(year), value=f'histogram-year-{year}', className='nav-item') for year in range(min_year, max_year + 1)
            ]),
            html.Div([
                dcc.Graph(id='histogram-fantasy-points'),
                dcc.Dropdown(
                    id='histogram-stat-dropdown',
                    options=[{'label': format_stat_name(stat), 'value': stat} for stat in team_stats],
                    value='fantasy_points',
                    className='btn w-50 mb-3')
                ], className='p-3')
        ], className='col-12 col-xl-6 p-3'),
        html.Div([
            html.H2('Offense Stats Correlation', className='text-center pb-3'),
            dcc.Tabs(id='scatter-year-tabs', value=f'scatter-year-{max_year}', className='nav nav-pills', children=[
                dcc.Tab(label=str(year), value=f'scatter-year-{year}', className='nav-item') for year in range(min_year, max_year + 1)
            ]),
            html.Div([
                dcc.Graph(id='scatter-offensive-stats', className='w-100'),
                html.Div([
                    html.Div([
                        dcc.Dropdown(
                            id='scatter-x-stat-dropdown',
                            options=[{'label': format_stat_name(stat), 'value': stat} for stat in team_stats],
                            value='total_yards',
                            className='btn w-100'
                        ),
                    ], className='col-12 col-xl-6 p-2'),
                    html.Div([
                        dcc.Dropdown(
                            id='scatter-y-stat-dropdown',
                            options=[{'label': format_stat_name(stat), 'value': stat} for stat in team_stats],
                            value='total_tds',
                            className='btn w-100'
                        ),
                    ], className='col-12 col-xl-6 p-2'),
                ], className='row w-100')
            ], className='p-3')
        ], className='col-12 col-xl-6 p-3'),
    ], className='row')
], className='container-fluid')

# Player stats by position line charts callback
create_player_callback(app, 'RB', df_rb)
create_player_callback(app, 'WR', df_wr)
create_player_callback(app, 'TE', df_te)
create_player_callback(app, 'QB', df_qb)

# Team stats bar charts callback
@app.callback(
    Output('team-bar-chart', 'figure'),
    [Input('team-stat-dropdown', 'value'), Input('bar-chart-year-tabs', 'value')]
)
def update_team_bar_chart(selected_stat, selected_year):
    """
    Update the team bar chart based on the stat selected in the dropdown and the year tab.

    Args:
        selected_stat (str): The selected statistic to display.
        selected_year (str): The selected year tab.

    Returns:
        plotly.graph_objs._figure.Figure: The updated bar chart figure.
    """
    selected_year = int(selected_year.split('-')[1])
    filtered_df = team_yearly_stats[team_yearly_stats['season'] == selected_year].sort_values(by=selected_stat, ascending=False)
    fig = px.bar(filtered_df, x='team', y=selected_stat, title=f'{format_stat_name(selected_stat)} by Team {selected_year}', color='team', color_discrete_map=teams_color)
    fig.update_yaxes(title_text=format_stat_name(selected_stat))
    return fig

# Offense Stats Distribution Histogram callback
@app.callback(
    Output('histogram-fantasy-points', 'figure'),
    [Input('histogram-stat-dropdown', 'value'), Input('histogram-year-tabs', 'value')]
)
def update_histogram(selected_stat, selected_year):
    """
    Update the histogram based on the stat selected in the dropdown and the year tab.

    Args:
        selected_stat (str): The selected statistic to display.
        selected_year (str): The selected year tab.

    Returns:
        plotly.graph_objs._figure.Figure: The updated histogram figure.
    """
    selected_year = int(selected_year.split('-')[2])
    filtered_df = df[df['season'] == selected_year]
    filtered_df = filtered_df[filtered_df[selected_stat] > 0]
    fig = px.histogram(filtered_df, x=selected_stat, nbins=20, color_discrete_sequence=['#20c997'], title=f'{format_stat_name(selected_stat)} Distribution {selected_year}')
    fig.update_layout(xaxis_title=format_stat_name(selected_stat), yaxis_title='Frequency')
    return fig

# Offense Stats Correlation Scatter Plot callback
@app.callback(
    Output('scatter-offensive-stats', 'figure'),
    [Input('scatter-x-stat-dropdown', 'value'),
     Input('scatter-y-stat-dropdown', 'value'),
     Input('scatter-year-tabs', 'value')
    ]
)
def update_scatter_plot(x_stat, y_stat, selected_year):
    """
    Update the scatter plot based on the stats selected in the dropdowns and the year tab.

    Args:
        x_stat (str): The selected statistic for the x-axis.
        y_stat (str): The selected statistic for the y-axis.
        selected_year (str): The selected year tab.

    Returns:
        plotly.graph_objs._figure.Figure: The updated scatter plot figure.
    """
    selected_year = int(selected_year.split('-')[2])
    filtered_df = team_yearly_stats[team_yearly_stats['season'] == selected_year]
    filtered_df = filtered_df[(filtered_df[x_stat] > 0) & (filtered_df[y_stat] > 0)]
    fig = px.scatter(
        filtered_df,
        x=x_stat,
        y=y_stat,
        color='team',
        color_discrete_map=teams_color,
        title=f'{format_stat_name(x_stat)} vs. {format_stat_name(y_stat)} {selected_year}', 
        hover_data=['team']
    )
    fig.update_traces(marker_size=15)
    fig.update_layout(xaxis_title=format_stat_name(x_stat), yaxis_title=format_stat_name(y_stat))
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
