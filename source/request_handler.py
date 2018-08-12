"""Functions to handle HTTP requests"""

from requests import get
from requests.exceptions import RequestException
from contextlib import closing

def simple_get(url):
    # Attempt to get the content at the URL
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                log_error("Response could not be parsed.")
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    # Check if the response is HTML
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)

def log_error(e):
    print(e)
    print("Please try again." + "\n")
