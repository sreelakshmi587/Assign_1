import sqlite3
con=sqlite3.connect('database.sqlite')
cur=con.cursor()

def ha_teams():
    con = sqlite3.connect('database.sqlite')
    cur = con.cursor()
    cur.execute("SELECT DISTINCT HomeTeam,AwayTeam FROM Matches where Season=2015 and FTHG=5")
    ha = cur.fetchall()
    HomeTeam, AwayTeam = 'HomeTeam', 'AwayTeam'
    print(f'\n{HomeTeam:<20}{AwayTeam:<20}\n')
    for i in ha:
        print(f'{i[0]:<20}{i[1]:<20}')

def arsenal():
    con = sqlite3.connect('database.sqlite')
    cur = con.cursor()
    cur.execute(" SELECT * FROM Matches where HomeTeam='Arsenal' and FTR='A'")
    d = cur.fetchall()
    Match_ID, Div, Season, Date, AwayTeam, FTHG, FTAG = 'Match_ID', 'Div', 'Season', 'Date', 'AwayTeam', 'FTHG', 'FTAG'
    print(f"{Match_ID:<20}{Div:<20}{Season:<20}{Date:<20}{AwayTeam:<20}{FTHG:<20}{FTAG:<20}\n")
    for x in d:
        print(f"{x[0]:<20}{x[1]:<20}{x[2]:<20}{x[3]:<20}{x[5]:<20}{x[6]:<20}{x[7]:<20}")

def season():
    con = sqlite3.connect('database.sqlite')
    cur = con.cursor()
    cur.execute("SELECT * FROM  Matches where Season BETWEEN 2012 AND 2015 AND AwayTeam='Bayern Munich' and FTHG>2")
    yr = cur.fetchall()
    Match_ID, Div, Season, Date, HomeTeam,FTHG, FTAG, FTR = 'Match_ID', 'Div', 'Season', 'Date', 'HomeTeam','FTHG','FTAG', 'FTR'
    print(f"{Match_ID:<20}{Div:<20}{Season:<20}{Date:<20}{HomeTeam:<20}{FTHG:<20}{FTAG:<20}{FTR:<20}\n")
    for y in yr:
        print(f"{y[0]:<20}{y[1]:<20}{y[2]:<20}{y[3]:<20}{y[4]:<20}{y[6]:<20}{y[7]:<20}{y[8]:<20}")

def beginner():
    con = sqlite3.connect('database.sqlite')
    cur = con.cursor()
    cur.execute("SELECT * FROM Matches where HomeTeam LIKE 'A%' AND AwayTeam LIKE 'M%'")
    begin = cur.fetchall()
    Match_ID, Div, Season, Date, HomeTeam, AwayTeam, FTHG, FTAG, FTR = 'Match_ID', 'Div', 'Season', 'Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR'
    print(f"{Match_ID:<20}{Div:<20}{Season:<20}{Date:<20}{HomeTeam:<20}{AwayTeam:<20}{FTHG:<20}{FTAG:<20}{FTR:<20}\n")
    for b in begin:
        print(f"{b[0]:<20}{b[1]:<20}{b[2]:<20}{b[3]:<20}{b[4]:<20}{b[5]:<20}{b[6]:<20}{b[7]:<20}{b[8]:<20}")

# Question_1
print('...HomeTeams and AwayTeams in each match played in 2015 and FTHG is 5...')
ha_teams()
print('\n...Details about Matches where HomeTeam is Arsenal and when FTR is A...\n')
arsenal()
print("\n...Match details of season 2012-2015 where Away Team is Bayern Munich and FTHG>2...\n")
season()
print("\n...Matches when HomeTeam name begins with A and that of Away Team begins with M...\n")
beginner()

def rows():
    con = sqlite3.connect('database.sqlite')
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM Teams")
    print(f'No. of rows in Teams : {cur.fetchone()[0]}')

def distinctseason():
    con = sqlite3.connect('database.sqlite')
    cur = con.cursor()
    cur.execute("SELECT DISTINCT Season FROM Teams")
    distinct = cur.fetchall()
    dis = []
    for d in distinct:
        dis.append(d[0])
    print('Distinct seasons include:', dis)

def minmax():
    con = sqlite3.connect('database.sqlite')
    cur = con.cursor()
    cur.execute("SELECT MAX(StadiumCapacity),MIN(StadiumCapacity) FROM Teams")
    maxmin = cur.fetchall()
    for m in maxmin:
        print(f"Largest Stadium Capacity= {m[0]} ,and\nSmallest Stadium Capacity= {m[1]}")

def squad():
    con = sqlite3.connect('database.sqlite')
    cur = con.cursor()
    cur.execute("SELECT SUM(KaderHome) FROM Teams where Season='2014'")
    print(f"Sum of squad players during 2014 is: {cur.fetchone()[0]}")

def goal_avg():
    con = sqlite3.connect('database.sqlite')
    cur = con.cursor()
    cur.execute("SELECT avg(FTHG) FROM Matches where HomeTeam='Man United'")
    print(f"No.of goals Man United score during home games on average: {format(cur.fetchone()[0], '.2f')}")

# Question_2
print('\n...Finding the No. of rows in the table Teams...')
rows()
print('\n...Accessing the different seasons in the table Teams...')
distinctseason()
print('\n...Finding the largest and Smallest Stadium Capacity...')
minmax()
print("\n...Sum of Squad players during 2014...")
squad()
print("\n...Average no.of goals by Man United on HomeGames...")
goal_avg()

def dec_order():
    con = sqlite3.connect('database.sqlite')
    cur = con.cursor()
    cur.execute("SELECT HomeTeam,FTHG,FTAG FROM Matches where Season ='2010' and HomeTeam='Aachen' ORDER BY FTHG DESC")
    dec = cur.fetchall()
    HomeTeam, FTHG, FTAG = 'HomeTeam', 'FTHG', 'FTAG'
    print(f"{HomeTeam:<20}{FTHG:<20}{FTAG:<20}\n")
    for c in dec:
        print(f"{c[0]:<20}{c[1]:<20}{c[2]:<20}")

def season16():
    con = sqlite3.connect('database.sqlite')
    cur = con.cursor()
    cur.execute("SELECT DISTINCT HomeTeam,COUNT(FTR) FROM Matches where Season ='2016' and FTR='H' GROUP BY HomeTeam ORDER BY COUNT(FTR) DESC")
    ftr=cur.fetchall()
    TeamName,FTRcount='TeamName','FTRcount'
    print(f"{TeamName:<20}{FTRcount:<20}")
    for f in ftr:
        print(f"{f[0]:<20}{f[1]:<20}")

def row10():
    con = sqlite3.connect('database.sqlite')
    cur = con.cursor()
    cur.execute("SELECT * FROM Unique_Teams LIMIT 10")
    unique = cur.fetchall()
    TeamName, Unique_Team_ID = 'TeamName', 'Unique_Team_ID'
    print(f"{TeamName:<20}{Unique_Team_ID:<15}")
    for u in unique:
        print(f"{u[0]:<20}{u[1]:<20}")

def team_match():
    con = sqlite3.connect('database.sqlite')
    cur = con.cursor()
    cur.execute("""SELECT Teams_in_Matches.Match_ID,Teams_in_Matches.Unique_Team_ID,Unique_Teams.TeamName
                        FROM Teams_in_Matches,Unique_Teams LIMIT 50""")
    tm=cur.fetchall()
    Match_ID,Unique_Team_ID,TeamName='Match_ID','Unique_Team_ID','TeamName'
    print(f"{Match_ID:<20}{Unique_Team_ID:<20}{TeamName:<20}")
    for m in tm:
        print(f"{m[0]:<20}{m[1]:<20}{m[2]:<20}")

def combo():
    con = sqlite3.connect('database.sqlite')
    cur = con.cursor()
    cur.execute("SELECT * FROM Unique_Teams INNER JOIN Teams LIMIT 10")
    cross = cur.fetchall()
    TeamName, Unique_Team_ID, Season, TeamName, KaderHome, AvgAgeHome, ForeignPlayersHome, OverallMarketValueHome, AvgMarketValueHome, StadiumCapacity = 'TeamName', 'Unique_Team_ID', 'Season', 'TeamName', 'KaderHome', 'AvgAgeHome', 'ForeignPlayersHome', 'OverallMarketValueHome', 'AvgMarketValueHome', 'StadiumCapacity'
    print(
        f"{TeamName:<20}{Unique_Team_ID:<20}{Season:<20}{TeamName:<20}{KaderHome:<20}{AvgAgeHome:<20}{ForeignPlayersHome:<20}{OverallMarketValueHome:<15}{AvgMarketValueHome:<20}{StadiumCapacity:<20}")
    for s in cross:
        print(f"{s[0]:<20}{s[1]:<20}{s[2]:<20}{s[3]:<20}{s[4]:<20}{s[5]:<20}{s[6]:<20}{s[7]:<20}{s[8]:<20}{s[9]:<20}")

def column_combo():
    con = sqlite3.connect('database.sqlite')
    cur = con.cursor()
    cur.execute("SELECT Unique_Teams.Unique_Team_ID,Unique_Teams.TeamName,Teams.AvgAgeHome,Teams.Season,Teams.ForeignPlayersHome FROM Unique_Teams,Teams LIMIT 5")
    tt = cur.fetchall()
    Unique_Team_ID, TeamName, AvgAgeHome, Season, ForeignPlayersHome = 'Unique_Team_ID', 'TeamName', 'AvgAgeHome', 'Season', 'ForeignPlayersHome'
    print(f"{Unique_Team_ID:<20}{TeamName:<20}{AvgAgeHome:<20}{Season:<20}{ForeignPlayersHome:<20}")
    for t in tt:
        print(f"{t[0]:<20}{t[1]:<20}{t[2]:<20}{t[3]:<20}{t[4]:<20}")

def high_id():
    con = sqlite3.connect('database.sqlite')
    cur = con.cursor()
    cur.execute("SELECT MAX(Match_ID),Teams_in_Matches.Unique_Team_ID,Unique_Teams.TeamName FROM Teams_in_Matches,Unique_Teams where (TeamName LIKE '%y')or (TeamName LIKE ' %r') GROUP BY Teams_in_Matches.Unique_Team_ID,TeamName ")
    high=cur.fetchall()
    Match_ID,Unique_Team_ID,TeamName='Match_ID','Unique_Team_ID','TeamName'
    print(f"{Match_ID:<20}{Unique_Team_ID:<20}{TeamName:<20}")
    for g in high:
        print(f"{g[0]:<20}{g[1]:<20}{g[2]:<20}")

#Question_3
print('\n...FTHG and FTAG details of matches from 2010 ordered in descending order of FTHG...')
dec_order()
print("\nThe total number of Home games each team won during 2016 ")
season16()
print('\nAccessing first 10 rows from Unique_Teams\n')
row10()
print('\nCombining tables when ID matches')
team_match()
print("\nCombining Two Tables")
combo()
print("\nCombining some columns from two tables")
column_combo()
print('\nHighest Match_ID for each team')
high_id()