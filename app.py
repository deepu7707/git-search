from flask import render_template

from config import app, APP_PORT

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return (render_template('404.html'), 404)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search",methods=['POST'])
def search():
	search_result = [{"owner_url":"","respository_name":"ABV","avatar_url":"//",
							   "created_at":"456789","owner_login":"gdshj",
							   "commit_message":"dfghj","commit_author_name":"9765"}]
	return render_template('index.html', search_results=search_result)


def get_last_commit(userid):
	return {'commit_message':"sds","commit_author_name":"sdf"}

def search_github(query, max_results):
	return search_result = [{"owner_url":"","respository_name":"ABV","avatar_url":"//",
							   "created_at":"456789","owner_login":"gdshj",
							   "commit_message":"dfghj","commit_author_name":"9765"}]

def prepare_error_response():
	return {"Error":False,"Message":"Error encountered.Please try after sometime"}

def prepare_success_response():
	return {"Success":"True","Message":"Retrieved github results with keyword","Data":{}}

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=APP_PORT)
