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


@app.route("/search",methods=['GET'])
def search():
    """
    Github Search API with query as url param
    """

    try:
        if request.method == 'GET' and 'query' in request.args:
            search_term =  request.args.get('query', '')
        else:
            render_template('index.html', search_results=[],
                            error=["Sorry.Search keyword is empty"])
    except Exception,e:
        return render_template('index.html', search_results=[],
                            error=["Sorry.Something went wrong"])
    git_search_api = SEARCH_API.format(search_term.replace(" ","+"))
    search_result = search_github(git_search_api, 5)
    if len(search_result):
        return render_template('index.html', search_results=search_result,
                            error=[])
    else:
        return render_template('index.html', search_results=[],
                            error=["Sorry.No results found"])

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=APP_PORT)
