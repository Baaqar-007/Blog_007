from application import create_app
# run the app in debug mode
app = create_app()

if __name__ == '__main__' :
    app.run(debug=True)
    
