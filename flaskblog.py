from flask import Flask, render_template, url_for
# from markupsafe import escape

app = Flask(__name__)

posts = [
    {
        'author': 'Farbod',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'July 25, 2022'
    },
    {
        'author': 'Jane',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 24, 2022'
    }
]

@app.route('/')
@app.route('/home')
def home():
    # name = request.args.get("name", "World")
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=1)
