from requests import get

website = get('https://www.google.com')

print('Current status code of google site is:')

print(website.status_code)
