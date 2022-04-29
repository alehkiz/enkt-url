from random import choice
import string, requests
from urllib.parse import urlparse

def generate_random_string(length : int) -> str:
    """ Generate a random string with ´size´ of param length, the generated string can be a number, letter (lower or upper) and the chars _ + - .

    Args:
        length (int): The length of generated string.

    Returns:
        str: Generated string
    """    
    return ''.join(choice(string.ascii_letters+string.digits+'+-_.') for _ in range(length))
    


def validate_url(url: str):
    parsed = urlparse(url)
    if all([parsed.scheme, parsed.netloc]):
        return parsed
    return False

def url_exist(url: str):
    session = requests.Session()
    return session.head(url, allow_redirects=True)