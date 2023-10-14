import requests
import json

class GoogleSearchClient:
  def __init__(self, api_key, cse_id):
    self.api_key = api_key
    self.cse_id = cse_id

  def search_google(self, query):
    url = f"https://www.googleapis.com/customsearch/v1?key={self.api_key}&cx={self.cse_id}&q={query}"
    response = requests.get(url)

    if response.status_code == 200:
      data = response.json()
      return data.get("items", [])
    else:
      print("Error: Unable to fetch search results")
      return []