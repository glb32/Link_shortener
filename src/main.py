import flask,url,db

app = flask.Flask(__name__)

@app.route('/a/<query>')
def redirectFromShortenedURL(query):
    try:
        result = db.redirectURL(query)
        return flask.redirect(result['URL'])
    except:
        return flask.render_template('404.html')
@app.route('/')
def form():
    return flask.render_template('form.html')

@app.route('/',methods=['POST'])
def makeShortenedURL():
    text = flask.request.form['text']
    result = url.Link(text)
    try:
        db.addURL(result.Shorten())
        return "URL:{}".format(result.ShortURL)
    except:
        return flask.render_template('invalid.html')
    
    
    
    
    
if __name__ == "__main__":
    app.run()