from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


limit = 10
tennorkey = "W5KKJLL9VWOE"

@app.route('/search')
def index():
    """Return homepage."""    
    search = request.args.get('search')
    
    our_params = {
       "q" :"search",
        "tennorkey" : "W5KKJLL9VWOE",
       "limit" : 10
   }

    r = requests.get("https://api.tenor.com/v1/search?", our_params)

    if r.status_code == 200:
        top_10gifs = json.loads(r.content)
        print(top_10gifs)
    else:
        top_10gifs = None

    
    #gif_json = r.json() 
    # TODO: Extract the query term from url using request.args.get()
    
    # TODO: Make 'params' dictionary containing:
    # a) the query term, 'q'
    # b) your API key, 'key'
    # c) how many GIFs to return, 'limit'
    
    # TODO: Make an API call to Tenor using the 'requests' library. For 
    # reference on how to use Tenor, see: 
    # https://tenor.com/gifapi/documentation

    # TODO: Use the '.json()' function to get the JSON of the returned response
    # object

    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list

    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'


    return render_template("index.html")#,gifs=gifs

if __name__ == '__main__':
    app.run(debug=True)
