import flask
import Database
import datetime

app = flask.Flask(__name__)
db = Database.Database()

banned_ips = ['172.30.31.73']
admin_ip = ['127.0.0.1']

@app.route('/', methods=['GET', 'POST'])
def index():
    error = 0
    if flask.request.remote_addr in banned_ips:
        print('Amogus')
        return flask.render_template('banned.html')
    if flask.request.method == 'POST':
        if flask.request.form.get('message') != None:
            content = flask.request.form['message']
            if len(content) > 200:
                error = 1
            else:   
                now = datetime.datetime.now()
                db.write_message(msg=Database.Message(
                    content=content, 
                    time=now.strftime('%H:%M:%S'),
                    author=(flask.request.remote_addr),
                ))
    messages = [db.read_message(id=id_) for id_ in range(db.get_db_size())]
    return flask.render_template('index.html', messages=messages[::-1], error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=11699)
    db.save_db()
