# Imports
from bs4 import BeautifulSoup
import requests
import json
import time
import random
import sys


# Constants

# URL beginning and end to access pages with shot charts
URL_START = "https://www.nba.com/game/002"
URL_END = "/game-charts"

# Base number for game URLs (2022-2023 season) and total games for the season
# Note: Each game URL increments by 1 from `22200001` to `22201230`
GAME_NUM_BASE = 22400001
TOTAL_GAMES = 1230

# Request headers
HEADERS = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

# Export directory path
EXPORT_PATH = "../../data/raw/S2425/"

def get_urls(season):
  """
  Fucntion to get all game URLs for a given season

  Args:
    season (str): Season to get game URLs for. Format: "YY" of season start. Example: "24" for 2024-2025 season

  Returns:
    url_list (list): List of all game URLs for the season
  """
  try:
    # Base number for game URLs and total games for the season
    # Note: Each game URL increments by 1 from `22200001` to `22201230`
    game_num_base = int(season + "00001")
    total_games = 1230

    # All game URLs for the season
    url_list = []
    for game in range(total_games):
      req_url = URL_START + str(game_num_base + game) + URL_END
      url_list.append(req_url)
    return url_list
  except:
    print("Error: Could not get game URLs for the season")
    return None


def get_soup(url):
  """
  Function to get the soup object from a given URL

  Args:
    url (str): URL to scrape

  Returns:
    soup (BeautifulSoup): Soup object of the URL

  """
  try:
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup
  except:
    print("Error: Could not get soup object from URL")
    return None


def get_json(soup):
  """
  Function to get the JSON object from a given soup object.
  Note: The JSON object is stored in a script tag with the id "__NEXT_DATA__"

  Args:
    soup (BeautifulSoup): Soup object of the URL

  Returns:
    json_obj (dict): JSON object of the URL's play-by-play data

  """
  try:
    script = soup.find(id="__NEXT_DATA__")
    json_obj = json.loads(script.text)
    return json_obj['props']['pageProps']['playByPlay']['actions']
  except:
    print("Error: Could not get play-by-play JSON object from soup object")
    return None


def save_json(json_obj, game_num):
  """
  Function to save the JSON object to a file

  Args:
    json_obj (dict): JSON object to save
    game_num (int): Game number to save the JSON object as

  """
  try:
    fp = EXPORT_PATH + "S2425-G" + "{0:0=4d}".format(game_num) + ".json"
    with open(fp, 'w') as f:
      json.dump(json_obj, f, indent=4)
  except:
    print(f"Error: Could not save JSON object to file with code {game_num}")
    return None


def export_game(game_num):
  """
  Function to export the JSON object of a game to a file

  Args:
    game_num (int): Game number to export

  """
  try:
    url = URL_LIST[game_num - 1]
    soup = get_soup(url)
    json_obj = get_json(soup)
    save_json(json_obj, game_num)
    print(f"Exported game {game_num}")
  except:
    print(f"Error: Could not export game {game_num}")
    return None


def export_all_games():
  """
  Function to export all games from the 2023-2024 season

  """
  try:
    for game_num in range(1, TOTAL_GAMES + 1):
      export_game(game_num)
      time.sleep(random.randint(1, 2))
  except:
    print("Error: Could not export all games")
    return None


def export_games(start, end):
  """
  Function to export a range of games from the 2023-2024 season

  Args:
    start (int): Starting game number
    end (int): Ending game number

  """
  try:
    for game_num in range(start, end + 1):
      export_game(game_num)
      time.sleep(random.randint(1, 2))
  except:
    print(f"Error: Could not export games from {start} to {end}")
    return None

# Main
if __name__ == "__main__":

  # Default season
  season = "24"

  # Check if an argument is provided
  if len(sys.argv) > 1:
    season = sys.argv[1]

  # Get all game URLs for the specified season
  URL_LIST = get_urls(season)