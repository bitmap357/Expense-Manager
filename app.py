from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def add():
    return render_template('add.html')

@app.route('/addexpense', methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)