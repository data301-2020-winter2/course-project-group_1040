import pandas as pd
import numpy as np

def load_and_process(address):
    
    #Method Chain #1: Load Data, clean out missing 
    df1 = (
        pd.read_csv(address)
        .rename(columns={"team1" : "home_team",
                         "team2" : "away_team",
                         "elo1_pre" : "home_pre", 
                         "elo2_pre" : "away_pre", 
                         "elo_prob1" : "home_prob", 
                         "elo_prob2" : "away_prob", 
                         "elo1_post" : "home_post", 
                         "elo2_post" : "away_post",
                         "pitcher1_adj" : "home_pitcher_rating",
                         "pitcher2_adj" : "away_pitcher_rating",
                         "score1" : "home_score",
                         "score2" : "away_score"}) # Creates a more readable dataframe
        .round(3) #Round all values to three decimals
        .fillna("s")  #The only NaN values are if they are playoffs so we can change them to s for regular season
    )
    
    
    #Method Chain #2:  Removing undesired rows and columns and create new columns]
    df2 = (
        df1.drop(["rating1_pre", 
                  "rating2_pre", 
                  "rating_prob1", 
                  "rating_prob2", 
                  "rating1_post", 
                  "rating2_post", 
                  "pitcher1", 
                  "pitcher2",
                  "pitcher1_rgs", 
                  "pitcher2_rgs", ], axis="columns") #We will only be worrying about elo ratings for this project, and adjusted pitcher ratings
    )
    
    #Returned DataFrame
    return df2
