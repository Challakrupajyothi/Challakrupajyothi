from flask import Flask, render_template
import requests

app = Flask(__name__)
@app.route('/')
def home():
    blog = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_post = blog.json()
    return render_template("index.html",posts=all_post)
@app.route('/post/<int:index>')
def show_post(index):
    blog = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_post = blog.json()
    return render_template("post.html",posts=all_post,blog_id=index)


if __name__ == "__main__":
    app.run(debug=True)
