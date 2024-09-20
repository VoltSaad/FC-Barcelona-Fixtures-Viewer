# FC-Barcelona-Fixtures-Viewer

This Python script fetches and displays FC Barcelona's upcoming match fixtures using the Football-Data.org API. It allows the user to select their time zone, showing the fixtures in the selected local time.

## Features

- Fetches FC Barcelona's fixtures.
- Displays match dates in your local timezone.
- Outputs match details such as competition, matchday, home/away status, opponent, match result, and status.
- Allows grouping of fixtures by competition.

## Prerequisites

Before you can run this script, you'll need to have the following dependencies installed:

- `requests`
- `pytz`
- `pandas`

You can install these packages using `pip`:

```bash
pip install requests pytz pandas
```
# FC Barcelona Fixtures Viewer

This Python application fetches and displays FC Barcelona's match fixtures in your local timezone using the Football-Data.org API. It handles time zone conversions, filters matches by home/away status, and displays results grouped by competition.

## Usage

### Get an API Key
- Sign up for an API key at [Football-Data.org](https://www.football-data.org/).

### Run the Script
1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/FC-Barcelona-Fixtures-Viewer.git
   ```
## Run The Python Script
```bash
python barcelona_fixtures.py
```

##User Input
You will be prompted to select a continent and timezone.
You can enter your Football-Data API key when prompted.
The script will fetch and display FC Barcelona's upcoming fixtures in your local time zone.

## Example
```bash
Select a continent to view its time zones:
1. Africa
2. America
3. Antarctica
4. Asia
5. Europe
Enter your choice (number): 5

Time zones in Europe:
1. Europe/Amsterdam
2. Europe/Andorra
...
Select your preferred time zone (number): 1

Please enter your API key: **********
Fetching Barcelona fixtures for timezone: Europe/Amsterdam...

--- La Liga ---
Matchday 1 2024-09-15 07:00 PM Home Real Madrid Scheduled Barcelona 2 - 1 Real Madrid
Matchday 2 2024-09-20 09:00 PM Away Atletico Madrid Finished Atletico Madrid 0 - 1 Barcelona
...

##Select a continent to view its time zones:
1. Africa
2. America
3. Antarctica
4. Asia
5. Europe
##Enter your choice (number): 5

##Time zones in Europe:
1. Europe/Amsterdam
2. Europe/Andorra
...
##Select your preferred time zone (number): 1

Please enter your API key: **********
Fetching Barcelona fixtures for the timezone: Europe/Amsterdam...

##--- La Liga ---
Matchday 1 2024-09-15 07:00 PM Home Real Madrid Scheduled Barcelona 2 - 1 Real Madrid
Matchday 2 2024-09-20 09:00 PM Away Atletico Madrid Finished Atletico Madrid 0 - 1 Barcelona
...
