import pandas as pd

# 1. Read the data
df = pd.read_csv("cfb.csv")

# 2. Ask the user for a season (repeat until valid)
valid = False
while not valid:
    try:
        season = int(input("Enter a season to analyze: "))
        season_df = df[df["Season"] == season]

        if season_df.empty:
            print("Season not found. Please try again.")
        else:
            valid = True  # loop condition now fails, so the loop ends
    except ValueError:
        print("Invalid input. Please enter a whole number like 2019.")

# 3. Dictionary with the four categories of wins and empty lists to hold the teams in each category
categories = {
    "10 or more wins": [],
    "8-9 wins": [],
    "6-7 wins": [],
    "Fewer than 6 wins": [],
}

# 4. Loop through the teams and sort them into categories based on their number of wins
for index, row in season_df.iterrows():
    team = row["Team"]
    wins = row["Win"]

    if wins >= 10:
        categories["10 or more wins"].append(team)
    elif wins >= 8:
        categories["8-9 wins"].append(team)
    elif wins >= 6:
        categories["6-7 wins"].append(team)
    else:
        categories["Fewer than 6 wins"].append(team)

# 5. Display the results of the search in database
print(f"College Football Results for {season}")
for category, teams in categories.items():
    print(f"\n{category}:")
    for team in teams:
        print(f"  {team}")