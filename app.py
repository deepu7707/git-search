import json
import urllib2
from flask import render_template, request

from config import app, APP_PORT, SEARCH_API
from helpers.utils import get_last_commit, search_github

@app.errorhandler(404)
def not_found(error):
    return (render_template('404.html'), 404)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search",methods=['POST'])
def search():
	try:
		search_term = request.form.get("search")
	except Exception,e:
		return render_template('index.html', search_results=[],error=["Sorry.Something went wrong"])
	git_search_api = SEARCH_API.format(search_term.replace(" ","+"))
	search_result = search_github(git_search_api, 5)
	return render_template('index.html', search_results=search_result,error=[])

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=APP_PORT)
