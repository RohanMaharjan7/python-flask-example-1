from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__, template_folder='template')


# @app.route("/<usr>")
# def user(usr):
#     return f"<h1>{usr}</h1>"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/light/index-video")
def index_video():
    return render_template('light/index-video.html')

@app.route("/portfolio-single-1")
def portfolio_single_1():
    return render_template('portfolio-single-1.html')

@app.route("/light/index-hero-slider")
def indexhero_slider():
    return render_template('light/index-hero-slider.html')

if __name__ == "__main__":
    app.run(debug=True)
