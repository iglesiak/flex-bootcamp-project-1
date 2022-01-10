from flex_bootcamp_project_1 import app

@app.route("/")
def home():
    return "Test page!"