import json
import os
import requests
from langchain.tools import tool

class SearchTools:
    @staticmethod
    @tool("Search the internet")
    def search_internet(query):
        """Search the internet for a specific query and return relevant results."""
        top_result_to_return = 4
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})  # Pass the exact query.
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'content-type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        if 'organic' not in response.json():
            return "Sorry, I couldn't find anything about that topic."
        results = response.json()['organic']
        output = []
        for result in results[:top_result_to_return]:
            try:
                output.append(f"Title: {result['title']}\nLink: {result['link']}\nSnippet: {result['snippet']}\n-----------------")
            except KeyError:
                continue
        return '\n'.join(output)
