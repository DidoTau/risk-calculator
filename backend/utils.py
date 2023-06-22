import string
import random

def random_string(length=6, chars=None, include_spaces=True):
    """
    Create a random string of given length.
    """
    if chars is None:
        chars = string.ascii_uppercase + string.digits

    if include_spaces:
        chars += ' '

    return ''.join(random.choice(chars) for x in range(length))


def get_new_id():
    """
    Get random string to be used as id
    """
    return random_string(length=8, include_spaces=False)