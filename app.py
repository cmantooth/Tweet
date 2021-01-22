from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('index.html',my_arg='I like instagram better')

    # if request has args (?tweet=some_tweet)
    if request.args:
        
        # get the value of the arg
        tweet = request.args.get('tweet')   
        
        return tweet
    
    return 'Hello World!'

@app.route('/about')
def about():

    about_text = """
    This is a text analyzer
    """
    
    return about_text

if __name__=='__main__':

    app.run(debug=True)
    

