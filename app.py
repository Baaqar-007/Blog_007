# import necessary libraries
from flask import Flask , render_template

# initialize flask app
app = Flask(__name__)

# list of sample blog posts
posts = [
    {
        'author' : 'Zain',
        'title' : 'Blog 1',
        'content' : '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a diam tellus''',
        'date_posted' : 'April 22 , 2023'
    }
    ,
    {
        'author' : 'Zain',
        'title' : 'Blog 2',
        'content' : '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a diam tellus''',
        'date_posted' : 'April 25 , 2023'
    }
]

# define home route
@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html', posts=posts)

# define about route
@app.route('/about')
def about():
    return render_template('about.html', title = "About")


# run the app in debug mode
if __name__ == '__main__' :
    app.run(debug=True)