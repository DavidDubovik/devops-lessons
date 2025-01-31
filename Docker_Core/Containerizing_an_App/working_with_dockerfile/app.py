from flask import Flask, Response, send_file
import os

app = Flask(__name__)

ENV = os.environ.get("ENV", "Development")


@app.route('/')
def hello():
    return f'''
    Docker is Awesome! My Env var is: {ENV}
<pre>                   ##        .</pre>
<pre>             ## ## ##       ==</pre>
<pre>          ## ## ## ##      ===</pre>
<pre>      /""""""""""""""""\___/ ===</pre>
<pre> ~~~ (~~ ~~~~ ~~~ ~~~~ ~~ ~ /  ===-- ~~~</pre>
<pre>      \______ o          __/</pre>
<pre>        \    \        __/</pre>
<pre>         \____\______/</pre>
    '''


@app.route('/logo')
def docker_logo():
    return send_file('docker-logo.png', mimetype='image/png')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
