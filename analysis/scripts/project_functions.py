{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_and_process(address):\n",
    "    \n",
    "    #Method Chain #1: Load Data, clean out missing \n",
    "    df1 = (\n",
    "        pd.read_csv(address)\n",
    "        .rename(columns={\"team1\" : \"home_team\",\n",
    "                         \"team2\" : \"away_team\",\n",
    "                         \"elo1_pre\" : \"home_pre\", \n",
    "                         \"elo2_pre\" : \"away_pre\", \n",
    "                         \"elo_prob1\" : \"home_prob\", \n",
    "                         \"elo_prob2\" : \"away_prob\", \n",
    "                         \"elo1_post\" : \"home_post\", \n",
    "                         \"elo2_post\" : \"away_post\",\n",
    "                         \"score1\" : \"home_score\",\n",
    "                         \"score2\" : \"away_score\"}) # Creates a more readable dataframe\n",
    "        .round(3) #Round all values to three decimals\n",
    "        .fillna(\"s\")  #The only NaN values are if they are playoffs so we can change them to s for regular season\n",
    "    )\n",
    "    \n",
    "    \n",
    "    #Method Chain #2:  Removing undesired rows and columns and create new columns]\n",
    "    df2 = (\n",
    "        df1.drop([\"rating1_pre\", \n",
    "                  \"rating2_pre\", \n",
    "                  \"rating_prob1\", \n",
    "                  \"rating_prob2\", \n",
    "                  \"rating1_post\", \n",
    "                  \"rating2_post\", \n",
    "                  \"pitcher1\", \n",
    "                  \"pitcher2\",\n",
    "                  \"pitcher1_rgs\", \n",
    "                  \"pitcher2_rgs\", \n",
    "                  \"pitcher1_adj\", \n",
    "                  \"pitcher2_adj\"], axis=\"columns\") #We will only be worrying about elo ratings for this project\n",
    "    )\n",
    "    \n",
    "    #Returned DataFrame\n",
    "    return df2"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
