from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask, render_template, url_for
from database_setup import Character, Deity, Guild, Race, Skill

app = Flask(__name__)

engine = create_engine('sqlite:///characters.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')


@app.route('/characters/')
def characters():
    c = session.query(Character).all()
    return render_template('characters.html', characters=c)


@app.route('/deities/')
def deities():
    d = session.query(Deity).all()
    return render_template('deities.html', deities=d)


@app.route('/guilds/')
def guilds():
    g = session.query(Guild).all()
    return render_template('guilds.html', guilds=g)


@app.route('/races/')
def races():
    r = session.query(Race).all()
    return render_template('races.html', races=r)


@app.route('/skills/')
def skills():
    s = session.query(Skill).all()
    return render_template('skills.html', skills=s)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
