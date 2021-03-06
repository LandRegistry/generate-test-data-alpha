from data_generator import DataGenerator
import json
import requests
import sys

def load_title(title):

    headers = { "Content-Type" : "application/json"}
    # I'm hardcoding the mint URL for the dev environment here for the moment.
    try:
        title_url =  "http://localhost:8001/titles/%s" % title.get('title_number')
        print "Loading %s" % title_url
        res = requests.post(title_url, data=json.dumps(title), headers=headers)
        print "Response status code %s" % res.status_code
    except requests.exceptions.RequestException as e:
        print "Error %s" % e
        raise RuntimeError


if __name__ == '__main__':
    quantity = 'all'
    if len(sys.argv) > 1:
        quantity = sys.argv[1]

    raw_data = DataGenerator.load_json()

    if quantity.isdigit():
        n = int(quantity)
        if n <= len(raw_data):
            raw_data = raw_data[:n]

    print "Loading", len(raw_data), "titles"
    
    titles = map(DataGenerator.convert_item, raw_data)
    map(load_title, titles)
    print "Done loading", len(titles), "titles"

