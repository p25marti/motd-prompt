import requests
import json
import html
from pathlib import Path
from termcolor import colored

# check if quote has already been displayed today
flag_file = Path("/home/pingu/.config/daily-design-quotes/displayed-already.flag")
already_displayed_today = flag_file.is_file()

if not already_displayed_today:

    # Make request to api with quotes
    url = 'http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1'

    try: 
        response = requests.get(url)
        response.raise_for_status()

    except requests.exceptions.RequestException as exception:
        print('Error: There was an error getting the quote of the day :(')
        exit()

    # Show Quote
    json = response.json()
    author = json[0]['title']
    content = json[0]['content']

    # unescape HTML 5 named character references (HTML entities)
    author = html.unescape(author)
    content = html.unescape(content)

    # trim leading and trailing <p> tags.
    content = content.replace('<p>', '')
    content = content.replace('</p>', '')

    # Print the quotes coloured
    content_colour = 'yellow'
    author_colour = 'red'
    print(colored('{}'.format(content), content_colour))
    print(colored('\t\t\t\t\t\t - {}'.format(author), author_colour))

    # *touch* file so that we know if a quote has already been displayed today
    flag_file.touch()
