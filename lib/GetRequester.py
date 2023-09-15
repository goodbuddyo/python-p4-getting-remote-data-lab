import requests
import json


class GetRequester:

    def __init__(self, url: str):
        self.url = url

    def get_response_body(self):
        URL = self.url
        # URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

        response = requests.get(URL)
        return response.content

    def load_json(self):
        myresult_list = []
        myresults = json.loads(self.get_response_body())
        for myresult in myresults:
            myresult_list.append(myresult)

        return myresult_list
