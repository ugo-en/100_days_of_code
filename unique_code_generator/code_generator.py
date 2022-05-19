"""
This is just a file with a bunch of functions for generating unique codes.
These codes can be used as API keys, OTP codes, and so on
"""
import string as s

def gen_otp():
    return "".join([choice(s.ascii_lowercase+s.ascii_uppercase) for i in range(70)])



def gen_api_key():
    return "".join([choice(s.ascii_letters+s.digits) for i in range(70)])


def gen_default_password():
    """
    Generates a random password.
    Each password must meet the following requirements:

    1. At least one uppercase letter.
    2. At least one lowercase letter.
    3. At least one digit.
    4. At least one special character.
    5. 12 characters long.
    """
    upper_letter = choice(s.ascii_uppercase)
    lower_letter = choice(s.ascii_lowercase)
    digit = choice(s.digits)
    character = choice(s.punctuation)

    rest = "".join([choice(s.digits+s.ascii_letters+s.punctuation) for i in range(9)])

    password = f"{upper_letter}{lower_letter}{digit}{character}{rest}"
    password = list(password)

    shuffle(password)

    password = "".join(password)

    return password

    

def gen_slug(title:str=""):
    """
    Generates a slug from a given title. Can be used to create slugs
    for blog posts and articles
    """
    try:
        title = re.sub(fr"[{s.punctuation}]","",str(title).strip())
        return title.replace(" ","-").replace("\n","-").replace("\t","-").lower()
    except:
        return ""