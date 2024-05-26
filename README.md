# NFL Offense Stats Dashboard

![Dashboard preview](preview.png)

This project is a Dash application that visualizes NFL offense statistics. It includes interactive charts for player and team stats over multiple seasons, providing insights into various performance metrics.

## Features

- **Player Stats by Position**: View statistics for Running Backs, Wide Receivers, Tight Ends, and Quarterbacks.
- **Player Selection**: Filter and visualize statistics for any player.
- **Team Stats by Year**: Analyze team performance metrics over different seasons.
- **Interactive Visualizations**: Use dropdowns and tabs to customize the data displayed in charts.

## Installation

### Prerequisites

- Python 3

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Alfredomg7/NFLOffenseStatsDashboard.git
   cd NFLOffenseStatsDashboard
   ```

2. **Install the dependencies:**
   
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the dash web application:**

   ```bash
   python app.py
   ```

## Project Structure
- `app.py`: Main application module containing the Dash app setup and layout.
- `utilities.py`: Utility functions for data loading, formatting, and creating callbacks.
- `config.py`: Configuration module with lists of statistics and team colors.
- `data/offense_yearly_data.csv`: Dataset with NFL Offense Stats used for the dashboard.

## Usage
- Run the application and open your browser to `http://127.0.0.1:8050`.
- Use the tabs and dropdowns to explore different player and team statistics.

## Acknowledgements
- Dash by Plotly: https://dash.plotly.com/
- Bootstrap Components: https://dash-bootstrap-components.opensource.faculty.ai/
- Dataset: [NFL Stats 1999-2022](https://www.kaggle.com/datasets/philiphyde1/nfl-stats-1999-2022/code) by Funk Monarch on [Kaggle](https://www.kaggle.com/)

## License
This project is for personal portfolio use and is not intended for commercial distribution. Feel free to explore and learn from the code, but please contact me if you wish to use it for other purposes.

## Contributions
This project is part of my personal portfolio, and while I'm not actively seeking contributions, I welcome any feedback or suggestions. If you have ideas for improvements or encounter any issues, feel free to reach out to me. Your insights are greatly appreciated!