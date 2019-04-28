import requests

def get_quotes():
    '''
    Fetches and returns random quotes from api
    '''

    url = 'http://quotes.stormconsultancy.co.uk/random.json'
    response = requests.get(url)
    quote = response.json()

    return quote