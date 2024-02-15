# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 12:20:02 2022

@author: david
"""

# Here we learn how to scrape tables in html format from a webpage
# using Pandas read_html(). 

# We'll direct the tables to dataframes, and after doing so we'll
# see that some work is often times needed to get the contents of 
# a table into a format such that we can perform arithmetic operations.

# For example, we may need to strip some of the contents of strings
# (e.g., '$' and '-') and strings will need to be converted to integers
# or floats.

# Below, we obtain the current contents of one of the Florida Lottery
# scratch-off games. It will be directed to a dataframe and then cleaned-up.
# We'll then calculate the unconditional mean/expected value of a ticket
# and the current conditional mean/expected value of a ticket. We'll also
# calculate the unconditional and conditional variance (and standard deviation).
import os
import numpy as np
import pandas as pd

##################################################
# Set Working Directory.
##################################################


# Find out the current directory.
os.getcwd()
# Change to a new directory.
git_path = 'C:\\Users\\jo585802\\OneDrive - University of Central Florida\\Documents\\GitHub\\ECO5445\\'
os.chdir(git_path + '\\13-IntroToWebScraping\\data')
# Check that the change was successful.
os.getcwd()


# First, we find the location of the information we want to scrape and then
# create a string identifying the location (URL). In the case below we are
# obtaining information on the scratch-off game '$500 Madness'.

url_1 = "https://www.flalottery.com/scratch-offsGameDetails?gameNumber=1454"


# Next, scrape the contents using Panda's read_html()

page_contents_1 = pd.read_html(url_1)

# Open what was just created so you see what we'll be working with.

# The page only contains a single table, so we can direct it to a
# dataframe if we specify the table number, remembering Python's 
# indexing structure.

df = page_contents_1[0]

# Let's save this so that we don't need to re-scrape after we work
# with it. We'll then re-open it.

df.to_csv('game_1.csv', index = False)
game_1 = pd.read_csv('game_1.csv')


# Ok, that was simple! But, we need to do a bit of work to get
# the dataframe in shape. Note:
# 1. Each of the variable names includes 2 words and a space is between
#    the words. Let's replace the spaces with underscores.
# 2. The contents of some of the variables are strings and include
#    non-numeric characters (e.g., '$' and '1-in-'). We need to strip
#    these characters and then convert the variables into numeric types.

# First, we replace the spaces with underscores in some variable names
 
game_1.columns = [c.replace(' ', '_') for c in game_1.columns]

# Second, we strip the '$' from one of the variables and replace the contents
# of another variable. See what happens if you use 'lstrip' instead of .replace().

for i in range(len(game_1.Prize_Amount)):
    game_1.Prize_Amount[i] = game_1.Prize_Amount[i].lstrip("$")
    game_1.Prize_Amount[i] = game_1.Prize_Amount[i].replace(',','' )
    game_1.Odds_of_Winning[i] = game_1.Odds_of_Winning[i].replace('1-in-','')
    game_1.Odds_of_Winning[i] = game_1.Odds_of_Winning[i].replace(',','' )

# Third, we convert the variables with string contents to numeric values.

game_1.Prize_Amount = pd.to_numeric(game_1.Prize_Amount, errors='raise', downcast=None)
game_1.Odds_of_Winning = pd.to_numeric(game_1.Odds_of_Winning, errors='raise', downcast=None)

# If you open the dataframe, you see that everything is in good shape.

# Ok, let's calculate the unconditional mean/expected value. By unconditional mean,
# we mean the mean before any tickets have been purchased and thus before anyone has
# lost or won.  Once tickets are purchased, there are losers and winners and the total
# number of tickets available declines. Thus, the mean value of a ticket changes.
# The conditional mean references the mean given the number of remaining tickets, some
# of which are 'losers' and some of which are 'winners'

# We could calculate the mean in one line, but let's spread the calculation out over
# a few for clarity.

# First, let's calculate the unconditional probability associated with each prize amount
# and the probability of losing an amount equal to the price.

game_1['Uncond_Prob'] = 1/(1+game_1.Odds_of_Winning)

lose_prob = 1 - sum(game_1.Uncond_Prob)

# Let's specify the the price
ticket_price = 10

# Next, weight each outcome (prize amount) by the unconditional probability
# and sum over the outcomes.

Unconditional_Mean = sum((game_1.Prize_Amount - ticket_price)*game_1.Uncond_Prob) - lose_prob*ticket_price



# The unconditional mean is about -$2.73. So, instead of the game being called
# '$500 Madness' it might instead be called '$500 Sadness'

# Next the unconditional variance. It is equal to the sum of probability-weighted
# squared deviations. The standard deviation is the square root of this.

Unconditional_Variance = sum(((game_1.Prize_Amount - Unconditional_Mean)**2)*game_1.Uncond_Prob)

Unconditional_Standard_Deviation = np.sqrt(Unconditional_Variance)

# We could also calculate the conditional mean, but when we look at the
# percentages of each prize, we see it has been distributed uniform

game_1["Percentage_Tickets_Remain"] = (game_1.Prizes_Remaining)/game_1.Total_Prizes