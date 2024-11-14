import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd





def most_wins(df):
    count_wins = df['WinningTeam'].value_counts()
    temp = pd.DataFrame(count_wins)
    temp.reset_index(inplace = True)
    return temp

def player_of_match(df):
    player_of_match = df['Player_of_Match'].value_counts()
    player_of_match

    temp1 = pd.DataFrame(player_of_match)
    temp1.reset_index(inplace = True)
    top_ten = temp1.head(15)

    return top_ten

def toss_dicion(df):
    # TOSS DECISIONS
    teams = df['TossWinner'].unique()
    decision_rows = []

    for element in teams:

        temp_bat = df[(df['TossWinner'] == element) & (df['TossDecision'] == 'bat')]
        temp_bowl = df[(df['TossWinner'] == element) & (df['TossDecision'] == 'field')]

        # Create dictionaries for 'Bat' and 'Field' decisions
        bat_rows = {'Toss Winner': element, 'Decision': 'Bat', 'Count': temp_bat['TossWinner'].count()}
        field_rows = {'Toss Winner': element, 'Decision': 'Field', 'Count': temp_bowl['TossWinner'].count()}

        # Append the dictionaries to the list
        decision_rows.append(bat_rows)
        decision_rows.append(field_rows)

        # Create DataFrame from the list of dictionaries
        decision_making = pd.DataFrame(decision_rows)

    return decision_making

def season_wise_winnig(df , years):
    season_grp = df.groupby('Season')
    alll = season_grp['WinningTeam'].value_counts().loc[years]
    wins = pd.DataFrame(alll)
    wins.reset_index(inplace = True)
    return wins


def battiing(players_df , whatUWant):
    filt = players_df.sort_values(whatUWant , ascending=False)
    top_order = filt[['player' , whatUWant]]
    top_ten = top_order.head(10)
    return top_ten

def bowling(players_df , whatUWant):
    if whatUWant != 'bowling_economy':
        filt = players_df.sort_values(whatUWant , ascending=False)
        top_order = filt[['player' , whatUWant]]
        top_ten = top_order.head(10)
        top_ten[whatUWant] = top_ten[whatUWant].astype(int)
    else:
        filt = players_df.sort_values(whatUWant , ascending=True)
        top_order = filt[['player' , whatUWant]]
        filt = top_order['bowling_economy'] > 1.0
        economy = top_order.loc[filt , ['player' , 'bowling_economy']]
        top_ten = economy.head(10)
    return top_ten


def qualifiers(df):
    # Functionality Team winning Predication
    filtt = df['MatchNumber'].str.contains('Qualifier' , na=False)


    team_qualifier_df = df.loc[filtt , ['Team1' , 'Team2']]
    team_qualifier_list1 = list(team_qualifier_df['Team1'])
    team_qualifier_list2 = list(team_qualifier_df['Team2'])
    team_qualifier_list1.extend(team_qualifier_list2)


    # print(team_qualifier_list1)
    qualifier_df = pd.DataFrame(team_qualifier_list1)
    qualifier_df.rename(columns={0 : 'Team Name'} , inplace=True)
    last_df = pd.DataFrame(qualifier_df.value_counts())
    last_df.reset_index(inplace=True)
    # last_df.rename(columns={'Team Name' : 'Team_name'} , inplace=True)
    return last_df

def final_match(df):
    # Same For Finalist Teams
    # Functionality Team winning Predication

    filtt = df['MatchNumber'] == 'Final'


    team_final_df = df.loc[filtt , ['Team1' , 'Team2']]

    team_final_list1 = list(team_final_df['Team1'])
    team_final_list2 = list(team_final_df['Team2'])
    team_final_list1.extend(team_final_list2)




    # print(team_qualifier_list1)
    qualifier_df_final = pd.DataFrame(team_final_list1)
    qualifier_df_final.rename(columns={0 : 'Team Name'} , inplace=True)
    last_df_final = pd.DataFrame(qualifier_df_final.value_counts())
    last_df_final.reset_index(inplace=True)
    # last_df.rename(columns={'Team Name' : 'Team_name'} , inplace=True)
    return last_df_final
