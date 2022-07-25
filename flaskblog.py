from flask import Flask, render_template
# from markupsafe import escape

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    # name = request.args.get("name", "World")
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=1)
