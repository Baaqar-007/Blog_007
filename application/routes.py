from flask import  render_template , flash, redirect , url_for 
from application.forms import RegistrationForm, LoginForm
from application.models import User, Post
from application import app


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
def home():
    return render_template('home.html', posts=posts)

# define about route
@app.route('/about')
def about():
    return render_template('about.html', title = "About")

@app.route('/register', methods =["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for('home'))
    return render_template('register.html', title = "Register", form = form)

@app.route('/login', methods =["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f"You have been logged in!", "success")
            return redirect(url_for('home'))
        else:
            flash("Login failed. Please check username and password.", "danger")
    return render_template('login.html', title = "Login", form = form)

