from flask import Flask, render_template

app = Flask(__name__)

# Route untuk dashboard
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
