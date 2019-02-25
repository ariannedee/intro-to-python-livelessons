from flask import Flask, render_template
app = Flask(__name__)

num_clicks = 0


@app.route('/')
def index():
    print(num_clicks)
    return render_template('index.html', num_clicks=num_clicks)


@app.route('/click', methods=['POST'])
def click():
    global num_clicks
    num_clicks += 1
    return f"I was clicked"
