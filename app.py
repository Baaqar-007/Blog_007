# import necessary libraries
from flask import Flask , render_template , flash, redirect , url_for 
from forms import RegistrationForm, LoginForm
# initialize flask app
app = Flask(__name__)

app.config['SECRET_KEY'] = '33754a16e180c8a45c1b1cdf867a2157' # protects against forgery attacks , generated from "secrets"

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



# run the app in debug mode
if __name__ == '__main__' :
    app.run(debug=True)