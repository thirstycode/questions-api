import flask
from flask import request, jsonify
from config import endpoint
import sqlite3
from config import problems_db, authfile

app = flask.Flask(__name__)
app.config["DEBUG"] = True

not_auth = [
    {'msg' : 'not authorized'
    }
]

@app.route('/', methods=['GET'])
def home():
    return '''Welcome to API</h1>
<p>API endpoint is at /api/v1/.</p>'''


@app.route(endpoint + 'get_questions_by_difficulty/', methods=['GET'])
def api_all():
    try:
        with open(authfile) as f:
            content = f.readlines()
        authkeys = [x.strip() for x in content] 
        if request.args.get('authkey') in authkeys:
            ans = []
            lang = request.args.get('lang')
            difficulty = request.args.get('diff')
            conn = sqlite3.connect(problems_db)
            c = conn.cursor()
            c.execute('''SELECT * FROM %s WHERE difficulty = '%s' '''%(lang,difficulty))
            rows = c.fetchall()
            for row in rows:
                ans.append({'question':row[1],'choice1':row[2],'choice2':row[3],'choice3':row[4],'choice4':row[5],'ans':row[6],'category':row[7]})
            conn.commit()
            conn.close()
            return jsonify(ans)
        else:
            return jsonify(not_auth)
    except Exception as e:
        return jsonify([{'msg':'some internal issue or wrong data provided','Exception':str(e)}])

@app.route(endpoint + 'get_questions_by_category/', methods=['GET'])
def api_category():
    try:
        with open(authfile) as f:
            content = f.readlines()
        authkeys = [x.strip() for x in content] 
        if request.args.get('authkey') in authkeys:
            ans = []
            lang = request.args.get('lang')
            category = request.args.get('category')
            conn = sqlite3.connect(problems_db)
            c = conn.cursor()
            c.execute('''SELECT * FROM %s WHERE category = '%s' '''%(lang,category))
            rows = c.fetchall()
            for row in rows:
                ans.append({'question':row[1],'choice1':row[2],'choice2':row[3],'choice3':row[4],'choice4':row[5],'ans':row[6],'category':row[7]})
            conn.commit()
            conn.close()
            return jsonify(ans)
        else:
            return jsonify(not_auth)
    except Exception as e:
        return jsonify([{'msg':'some internal issue or wrong data provided','Exception':str(e)}])

#app.run()