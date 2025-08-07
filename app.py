from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hospital Appointment System API by JaHid"

if __name__ == '__main__':
    app.run(debug=True)
