from app import app

@app.route('/')
@app.route('/home')
def index():
    return "Hello, World!"

@app.route('/trial-flask')
def trial_flask():
    return "Yohana nyoba flask gais"