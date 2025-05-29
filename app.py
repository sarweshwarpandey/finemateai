from flask import Flask, render_template, jsonify
from update_tips import fetch_and_save_random_posts

app = Flask(__name__)

@app.route('/')
def home():
    tips = fetch_and_save_random_posts()  # Updates tips.json every refresh
    return render_template('index.html', tips=tips)

@app.route('/api/tips')
def api_tips():
    tips = fetch_and_save_random_posts()  # Also updates tips.json on API call
    return jsonify(tips)

if __name__ == '__main__':
    app.run(debug=True)
