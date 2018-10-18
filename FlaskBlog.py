from flask import Flask,render_template
app = Flask(__name__)


posts = [
    {
        'author': 'Rahul Kathuria',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date': 'September 20, 2018'
    },
    {
        'author': 'Chitkara',
        'title': 'Blog Post 2',
        'content': 'Second Post content',
        'date': 'September 21, 2018'
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
   app.debug = True
   app.run()
   app.run(debug = True)