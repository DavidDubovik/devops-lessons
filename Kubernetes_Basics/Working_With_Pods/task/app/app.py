from flask import Flask, Response, send_file
import os
import time
start_time = time.time()
start_period = 40

app = Flask(__name__)

@app.route('/')
def hello():
   return f'''
   Docker is Awesome!
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
   return send_file('docker-logo.png', mimetype='#')

@app.route('/health')
def health_check():
   Response("Healthy", status=200)

@app.route('/ready')
def readiness_check():
   if time.time() < start_time + start_period:
      return Response("Not Ready", status=503)
   else:
      return Response("ready", status=200)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080)

