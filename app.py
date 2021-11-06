from flask import Flask
from flask import make_response
app = Flask(__name__)
@app.route('/')
def home():
    return "Hello World!"
@app.route('/<page_name>')
def other_page(page_name):
    response = make_response('The page named %s does not exist.' \
                             % page_name, 404)
    return response
if _name_ == '__main__':
    app.run('0.0.0.0',debug=True)
