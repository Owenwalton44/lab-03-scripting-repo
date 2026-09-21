
#!(owenw\ds2022-fall-26\lab-03-scripting-repo\.venv\Scripts\python.ex)

import os
import requests
import json

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'
#print(GHUSER)
#print(url)

def retrieve_events(url):
	"""returns list of dictionaries containing event information"""
	url_json=requests.get(url).text
	return (json.loads(url_json))
#print(retrieve_events("https://api.github.com/users/owenwalton44/events"))

def print_events(events,n=5):
	"""prints the event and the repo its nested in, format type :: repo """
	for x in events[:n]:
		event = x['type'] + ' :: ' + x['repo']['name']
		print(event)
#print_events(retrieve_events('https://api.github.com/users/owenwalton44/events'),5)

def main():
	"""prints github user, github url, and the events that occur on the account"""
	print(GHUSER)
	print(url)
	temp=retrieve_events(url)
	print_events(temp)

if __name__ == "__main__":
	main()
