# NBA import
from espn_api.basketball import League
from espn_api.basketball import Team
from espn_api.basketball import Player
# importing datetime to automatically save year
import datetime
# instantiating datetime
today = datetime.date.today()
current_year = today.year # using datetime to save current year

def league_info():
    """Collect the user's league ID"""
    global id, league_year, espn_s2, swid, team_name
    id = input("Enter your league ID: ") # save league id
    league_year = input("Enter your league's year: ") # save league year
    espn_s2 = input("Enter your s2: ") # save s2 number
    swid = input("Enter your SWID: ") # save swid
    team_name = input("Enter your team name: ") # save team name


# league_info()
stripped_team_list = [] # empty list to save names of all teams in league
stripped_roster = [] # empty list to save names of all players on team
league = League(league_id=615950672, year=2024, espn_s2='AEChhl1bNn4KR%2FK87QmuCAnSte8qDJABjRwVAG9XArI8CcGAAOFBaHq1wZRG636NJ6J6sJ7FbM8j8vQqlPzLBneKITGeD20sxjyCgF6aDaVtEt%2FY7amfktNrbVOTNxzmsoC8EUNZGEzath%2Fa58T9cXPYeZyyLx3LLJPEEnz02UihkR13sZ8WDZHgbp7pYQF%2BcgUZYzwAdaA3r5kTUPPy092QLM1twGU8cxvBfyh7zZybfMPm9qFbKB8StoAQi2xtB9S5UXld1x7mk4OctGUc7v2M2DhHUknHUg39RLAJw1Yj%2BOwdQilnOV9%2BpESSRCqS8ds%3D', swid='{2FB4CA91-2307-4A13-B3A8-AF75F61F0448}')
team_list = league.teams # saves a list of all teams in the league
# iterate through list to find your team
team_name = "K.D.'s Nuts" # hardcoded name in
# my_team = team_list.index(team_name)
# print(my_team)

# iterating through list to find team index 
for team in team_list:
    if str(team) == f"Team({team_name})":
        team_index = team_list.index(team)

# stores the name of your team
my_team = league.teams[team_index]
str_my_team = str(league.teams[team_index]) # <Team(name)>
stripped_team = str_my_team[5:-1] # removing the "Team(" prefix and end bracket
print(stripped_team)

for team in team_list:
   str_team = str(team)
   stripped_team_list.append(str_team[5:-1])

# saving list of players on team
for player in my_team.roster:
    str_player = str(player)
    stripped_roster.append(str_player[7:-1])

