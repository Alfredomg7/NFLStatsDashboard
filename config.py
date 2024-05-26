"""
Configuration module for NFL Offense Stats Dashboard.
Contains the list of relevant statistics for each position and team-color mapping.
"""

# Select relevant stats for each position
rb_stats = [
    'carries', 'rushing_yards', 'rushing_tds', 'rushing_fumbles', 'rushing_fumbles_lost',
    'rushing_first_downs', 'rushing_2pt_conversions', 'receptions', 'targets',
    'receiving_yards', 'receiving_tds', 'receiving_fumbles', 'receiving_fumbles_lost',
    'receiving_air_yards', 'receiving_yards_after_catch', 'receiving_first_downs',
    'receiving_2pt_conversions', 'target_share', 'air_yards_share', 'fantasy_points',
    'fantasy_points_ppr', 'total_yards', 'games', 'offense_snaps', 'teams_offense_snaps',
    'ypc', 'ypr', 'touches', 'rush_td_percentage', 'rec_td_percentage',
    'total_tds', 'td_percentage', 'offense_pct', 'rush_ypg', 'rec_ypg', 'ppg',
    'ppr_ppg', 'yps', 'ypg'
]

wr_te_stats = [
    'receptions', 'targets', 'receiving_yards', 'receiving_tds', 'receiving_fumbles',
    'receiving_fumbles_lost', 'receiving_air_yards', 'receiving_yards_after_catch',
    'receiving_first_downs', 'receiving_2pt_conversions', 'target_share', 'air_yards_share',
    'fantasy_points', 'fantasy_points_ppr', 'total_yards', 'games', 'offense_snaps',
    'teams_offense_snaps', 'ypr', 'rec_td_percentage', 'total_tds',
    'td_percentage', 'offense_pct', 'rec_ypg', 'ppg', 'ppr_ppg', 'yps', 'ypg',
]

qb_stats = [
    'completions', 'attempts', 'passing_yards', 'passing_tds', 'interceptions', 'sacks',
    'sack_yards', 'sack_fumbles', 'sack_fumbles_lost', 'passing_air_yards',
    'passing_yards_after_catch', 'passing_first_downs', 'passing_2pt_conversions',
    'fantasy_points', 'fantasy_points_ppr', 'total_yards', 'games', 'offense_snaps',
    'teams_offense_snaps', 'ypa', 'comp_percentage', 'pass_td_percentage',
    'int_percentage', 'pass_ypg', 'ppg', 'ppr_ppg', 'yps', 'ypg',
]

team_stats = list(set(qb_stats + rb_stats + wr_te_stats))

# List to map the main color for each NFL team
teams_color = {
    'ARI': '#97233F', 
    'ATL': '#A71930',
    'BAL': '#241773', 
    'BUF': '#00338D', 
    'CAR': '#0085CA', 
    'CHI': '#C83803', 
    'CIN': '#FB4F14', 
    'CLE': '#FF3C00', 
    'DAL': '#003594', 
    'DEN': '#FB4F14', 
    'DET': '#0076B6', 
    'GB': '#FFB612', 
    'HOU': '#03202F', 
    'IND': '#002C5F', 
    'JAX': '#006778', 
    'KC': '#E31837', 
    'LA': '#003594', 
    'LAC': '#0080C6', 
    'LV': '#A5ACAF', 
    'MIA': '#008E97', 
    'MIN': '#4F2683', 
    'NE': '#002244', 
    'NO': '#D3BC8D', 
    'NYG': '#0B2265', 
    'NYJ': '#125740', 
    'PHI': '#004C54', 
    'PIT': '#FFB612', 
    'SEA': '#69BE28', 
    'SF': '#AA0000', 
    'TB': '#D50A0A', 
    'TEN': '#4B92DB', 
    'WAS': '#773141'
}