from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask
app = Flask(__name__)

engine = create_engine('sqlite:///characters.db')
Session = sessionmaker(bind=engine)

@app.route('/')
@app.route('/home')
def home():
    return 'This is a test!'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
