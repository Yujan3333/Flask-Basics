from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")
    # return 'Hello, World!'

@app.route('/products')
def products():
    return "This is a products page"

# for the app to run in debug mode in browser it runs
if __name__ == "__main__":
    app.run(debug=True) 