import json
import requests
import urllib.parse



class request_poring:
    def __init__(self, itemToSearch):

        self.headers = {"Content-type": "application/json"}
        self.itemToSearch = itemToSearch

        # Transform itemToSearch to  urlencode
        self.itemToSearch = urllib.parse.quote(self.itemToSearch)
        self.request = requests.get("https://poring.world/api/search?order=popularity&rarity=&inStock=1&modified=&category=&endCategory=&q=" + self.itemToSearch, headers=self.headers)
        
        #Fill the first element of the list with a dictionary that contains all the data of the searched item
        self.data = self.request.json()
        
    # Returns the stock of the item that we are searching for
    def get_stock(self):
        return self.data[0]["lastRecord"]["stock"]
        


