A small uWSGI application called GitHub navigator.
Search GitHub repositories by given search term and present them as html page. 
1) The tool takes one parameter "search_term" as input
2) It queries GitHub API with this search_term to look for repositories
3) It takes first page of search result and sorts items by the creation date in descending order
4) The info about first 5 (newest) repositories is rendered into html template together with some information about latest commit in this repository.

Usage
pip install -r requirements.txt
python app.py
Open a browser and do GET request to e.g. http://localhost:8000/navigator?search_term=arrow
