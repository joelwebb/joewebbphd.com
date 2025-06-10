
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', page_title='Home', current_page='index')

@app.route('/about')
def about():
    return render_template('about.html', page_title='About', current_page='about')

@app.route('/projects')
def projects():
    return render_template('projects.html', page_title='Projects', current_page='projects')

@app.route('/resume')
def resume():
    return render_template('resume.html', page_title='Resume', current_page='resume')

@app.route('/post')
def post():
    return render_template('post.html', page_title='Post', current_page='index')

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html', page_title='Subscribe', current_page='subscribe')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
