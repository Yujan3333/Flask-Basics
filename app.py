from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/products')
def products():
    return "This is a products page"

# for the app to run in debug mode in browser it runs
if __name__ == "__main__":
    app.run(debug=True) 