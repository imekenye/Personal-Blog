import urllib.request,json
from .models import Quote

# Getting api key
# Getting the movie base url
base_url = None

def configure_request(app):
    global base_url

    base_url = app.config['QUOTE_API_BASE_URL']

def get_quotes():
    '''
    Function that gets the json response to our url request
    '''
    get_quotes_url = base_url.format()

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quote_results = None

        if get_quotes_response['results']:
            quote_results_list = get_quotes_response['results']
            quote_results = process_results(quote_results_list)


    return quote_results

def process_results(quote_list):

    quote_results = []
    for quote_item in quote_list:
        id = quote_item.get('id')
        quote = quote_item.get('quote')
        author = quote_item.get('author')

        quote_object = Quote(id,quote,author)
        quote_results.append(quote_object)

    return quote_results
