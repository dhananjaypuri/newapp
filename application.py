from flask import Flask, render_template

application = Flask(__name__);

application.secret_key = "secretkey";

@application.route('/', methods=['GET', 'POST'])
def home():
    return "<h1>Welcome to flask app !!!! Subcribe my channel !!!! </h1>";

if __name__ == "__main__":

    application.run();