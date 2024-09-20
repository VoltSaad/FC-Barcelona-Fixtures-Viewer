import requests
import pytz
from datetime import datetime
import pandas as pd

# The API URL for fetching Barcelona team fixtures from Football-Data.org
API_URL = "https://api.football-data.org/v4/teams/81/matches"

def fetch_fixtures(api_key):
    """
    Fetches FC Barcelona's match fixtures from the Football-Data API.
    
    Args:
        api_key (str): Your API key for authenticating with the Football-Data API.
    
    Returns:
        list: A list of match data if the request is successful.
        None: If the request fails or returns an error.
    """
    headers = {"X-Auth-Token": api_key}
    response = requests.get(API_URL, headers=headers)
    
    # Check if the request was successful (HTTP 200 OK)
    if response.status_code == 200:
        # Return the list of matches from the response
        return response.json()['matches']
    else:
        print("Failed to fetch data:", response.status_code)
        return None

def parse_matches(matches, timezone):
    """
    Parses the fetched match data and formats it for display, converting dates to the user's local timezone.

    Args:
        matches (list): A list of match data fetched from the API.
        timezone (str): The user's preferred timezone for date conversion.

    Returns:
        pd.DataFrame: A DataFrame containing formatted match details such as competition, 
                      matchday, local time, home/away status, opponent, match result, and status.
    """
    rows = []
    
    for match in matches:
        # Convert UTC date to local timezone date
        utc_date = match['utcDate']
        local_date = datetime.strptime(utc_date, "%Y-%m-%dT%H:%M:%SZ")
        local_date = local_date.replace(tzinfo=pytz.utc).astimezone(pytz.timezone(timezone))
        
        # Extract key match details
        home_team = match['homeTeam']['name']
        away_team = match['awayTeam']['name']
        matchday = match['matchday']
        status = match['status']
        
        # Check for full-time score or default to 0 if not available
        home_score = match['score']['fullTime']['home'] if match['score']['fullTime']['home'] else 0
        away_score = match['score']['fullTime']['away'] if match['score']['fullTime']['away'] else 0
        competition = match['competition']['name']
        
        # Determine if Barcelona is the home team and set opponent accordingly
        if home_team == "FC Barcelona":
            opponent = away_team
            barcelona_is_home = True
        else:
            opponent = home_team
            barcelona_is_home = False
        
        # Format the match result for display
        match_result = f"{home_team} {home_score} - {away_score} {away_team}"
        
        # Append the parsed match details to the list of rows
        rows.append([
            competition,
            matchday,
            local_date.strftime("%Y-%m-%d %I:%M %p"),  # Convert date to 12-hour format with AM/PM
            'Home' if barcelona_is_home else 'Away', 
            opponent, 
            status, 
            match_result
        ])
    
    # Create a DataFrame to hold all parsed match data
    df = pd.DataFrame(rows, columns=['Competition', 'Matchday', 'Local Date Time', 'Home/Away', 'Opponent', 'Status', 'Result'])
    
    # Sort the DataFrame by competition and date for better readability
    df.sort_values(by=['Competition', 'Local Date Time'], inplace=True)
    return df

def display_grouped_data(df):
    """
    Displays the match data grouped by competition for easier viewing.

    Args:
        df (pd.DataFrame): A DataFrame containing match details.
    """
    # Group the matches by competition
    competition_group = df.groupby('Competition')
    
    # Iterate through each group and display matches
    for name, group in competition_group:
        print(f"--- {name} ---")
        print(group.drop(columns='Competition'), "\n")  # Drop the Competition column for cleaner output

def list_continents():
    """
    Retrieves and returns a list of continents based on the available timezones.
    
    Returns:
        list: A sorted list of unique continent names from available timezones.
    """
    # Extract unique continents from the timezone list
    continents = sorted(set(x.split('/')[0] for x in pytz.all_timezones))
    return continents

def list_timezones(continent):
    """
    Retrieves the timezones for a specific continent.
    
    Args:
        continent (str): The name of the continent to list timezones for.

    Returns:
        list: A list of timezones within the specified continent.
    """
    # List timezones that belong to the selected continent
    timezones = [tz for tz in pytz.all_timezones if tz.startswith(continent + '/')]
    return timezones

def display_menu(options, prompt):
    """
    Displays a menu of options and prompts the user to make a selection.
    
    Args:
        options (list): A list of options to display.
        prompt (str): The prompt to show to the user for input.

    Returns:
        str: The selected option based on the user's choice.
    """
    # Print the options with numbers for selection
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    # Loop to ensure valid input is provided
    while True:
        try:
            choice = int(input(prompt)) - 1
            return options[choice]
        except (IndexError, ValueError):
            print("Invalid input, please try again.")

def main():
    """
    The main function orchestrates the flow of the program, allowing the user to select their 
    timezone and fetch and display FC Barcelona's match fixtures in their local time.
    """
    print("Select a continent to view its time zones:")
    
    # List continents and allow the user to select one
    continents = list_continents()
    selected_continent = display_menu(continents, "Enter your choice (number): ")
    
    # List timezones for the selected continent
    print(f"\nTime zones in {selected_continent}:")
    timezones = list_timezones(selected_continent)
    selected_timezone = display_menu(timezones, "Select your preferred time zone (number): ")
    
    # Prompt the user to enter their Football-Data API key
    api_key = input("Please enter your API key: ")
    
    # Fetch and display match data for FC Barcelona
    print(f"Fetching Barcelona fixtures for timezone: {selected_timezone}...")
    fixtures = fetch_fixtures(api_key)
    if fixtures:
        df = parse_matches(fixtures, selected_timezone)
        display_grouped_data(df)
    else:
        print("No data available to display.")

# Ensure the main function is only called when the script is run directly
if __name__ == "__main__":
    main()
