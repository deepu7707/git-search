import json
import urllib2

from config import SEARCH_COMMIT_API

def get_last_commit(user_login, repo_name):
	commit_details = {}
	latest_commit_formatted_api = SEARCH_COMMIT_API.format(user_login, repo_name)
	req = urllib2.Request(latest_commit_formatted_api)
	response = urllib2.urlopen(req)
	commit_response = json.loads(response.read())
	commit_details['sha'] = commit_response['sha']
	commit_details['commit_message'] = commit_response['commit']['message']
	commit_details['commit_author_name'] = commit_response['commit']['author']['name']
	return commit_details

def search_github(query_url, max_results):
	try:
		final_response = []
		req = urllib2.Request(query_url)
		response = urllib2.urlopen(req)
		search_response = json.loads(response.read())
		if search_response:
			results = sorted(search_response['items'], key=lambda x: x['created_at'], 
						reverse=True)[:max_results]
			for each in results:
				commit_details = get_last_commit(each["owner"]["login"],each['name'])
				temp = {'respository_name':each['name'],
					'owner_url':each['owner']['url'],
					"created_at":each['created_at'],
					"owner_login":each["owner"]["login"],
					"commit_message":commit_details['commit_message'],
					"commit_author_name":commit_details['commit_author_name'],
					"avatar_url":each['owner']['avatar_url'], "sha":commit_details['sha']}
				final_response.append(temp)
		return final_response
	except Exception, e:
		print e
		return []
