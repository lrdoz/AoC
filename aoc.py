import errno
import os
import sys
import requests

# URLS needed for our requests
payload = 'http://adventofcode.com/{year}/day/{day}/input'
payload_refer = 'http://adventofcode.com/{year}/day/{day}'
payload_submit = 'http://adventofcode.com/{year}/day/{day}/answer'

# Additional info needed
fname = 'input.txt'
module_path = os.path.dirname(__file__)
user_agent =  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
cookie = './cookie.txt'

#----- Helpers ------
def eprint(*args, **kwargs):
    print(*args, file = sys.stderr, **kwargs)

def user_session(cookie = cookie):
    try:
        with open(cookie) as cookie_key:
            secret = cookie_key.read().strip()
            #print(secret)
    except:
        raise ValueError("You did not provide your session cookie")
    return secret

class puzzle_data(object):
    def __init__(self, year, day, session = None):
        self.year = year
        self.day = day
        self.session = session
        if session is None:
            print("Getting a session for you")
            self.session = user_session()

        self.temp = None

    def dump_temp(self):
        """Shall you want the input to be saved in a file, note
        you will also need to uncomment self.dump_temp from
        get_data"""
        fname = ('./input{}.txt'.format(self.day))
        with open(fname, 'w') as f:
            f.write(self.temp)
            f.flush()

    def get_data(self):
        """get data for days 1-25 since this are user
        dependent"""

        URI = payload.format(year = self.year, day = self.day)

        if self.temp is None:
            response = requests.get(URI, cookies={'session': self.session},
                                    headers = {'User-Agent': user_agent})

            if response.status_code == requests.codes.ok:
                print('Got your input for Day {}. Hooray! Get working'.format(self.day))
                self.temp = response.text.strip()
            else:
                raise IOError("Ooops that did not work, got a {} code :{}".format(response.status_code,
                                                                                  response.content))
        # self.dump_temp()
        return self.temp

    def submit(self, part, answer):
        """ part is 1 or 2 and the answer is a string
        returned from the puzzle function"""

        URI = payload_submit.format(year =  self.year, day = self.day)
        URIR = payload_refer.format(year = self.year, day = self.day)
        response = requests.post(URI,
                                 data={'level': part, 'answer': answer},
                                 cookies={'session': self.session},
                                 headers={'User-Agent': user_agent,
                                          'Referer': URIR},
                                 )

        if response.status_code != 200:
            eprint("Submission status", response.status_code)
            eprint(response.content)
            raise AocdError('Unexpected response')

        content = response.content
        if "That's the right answer!" in content:
            print("Correct answer")
        elif "That's not the right answer" in content:
            print("Wrong answer: your answer is", content.split("your answer is ")[1].split(".", 1)[0])
        else:
            print("Unexpected response:")
            print(content)
