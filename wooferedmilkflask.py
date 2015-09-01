#all the imports----------------------------------------------------------------
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing

#configuration------------------------------------------------------------------
DATABASE = 'wooferedmilk.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

#create app
app = Flask(__name__)
app.config.from_object(__name__)
#database functions-------------------------------------------------------------
#string of all rows: id, name, status, commands, emotes, pcommands, dogfacts, dogs, multi, quote, speedrun, utility, youtube, faq, highlights, ignore, mods, nick, quotes, trigger
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv

#before and teardown request functions------------------------------------------
@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

#---------------------------------------------------------------
@app.route("/")
def dashboardNoUser():
    userlist = []
    for user in query_db('select * from users'):
        userlist.append(user['name'])
    return userlist[1]
#	return render_template("index.html")

#def dashboardNoUser():
#	cur = g.db.execute('select id, name from users order by id desc')
#	users = [dict(id=row[0], name=row[1], status=row[2], commands=row[3], emotes=row[4], pcommands=row[5], dogfacts=row[6], dogs=row[7], multi=row[8], quote=row[9], speedrun=row[10], utility=row[11], youtube=row[12], faq=row[13], highlights=row[14], ignore=row[15], mods=row[16], nick=row[17], quotes=row[18], trigger=row[19]) for row in cur.fetchall()]
#	return render_template("index.html")

#@app.route("/milkisaloser")
#def milkdumb():
#	return render_template("charts.html")
if __name__ == '__main__':
	connect_db()
	app.run(debug=True)
