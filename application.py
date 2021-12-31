from flask import Flask, app , render_template

application = Flask(__name__);

@application.route('/', methods=['GET', 'POST'])
def home():
    return "<h1>Welcome to flask app </h1>";

if __name__ == "__main__":

    application.run();