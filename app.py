from flask import Flask, render_template, request, redirect, url_for
import random
import string

app = Flask(__name__)

# URLを保存するための簡単な辞書（データベースの代わり）
url_dict = {}

# ランダムな短縮URLを生成する関数
def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_url = generate_short_url()
        url_dict[short_url] = long_url
        return render_template('index.html', short_url=short_url, long_url=long_url)
    return render_template('index.html')

@app.route('/<short_url>')
def redirect_to_url(short_url):
    long_url = url_dict.get(short_url)
    if long_url:
        return redirect(long_url)
    return 'URL not found!', 404

if __name__ == '__main__':
    app.run(debug=True)
