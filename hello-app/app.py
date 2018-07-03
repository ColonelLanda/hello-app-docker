from flask import Flask, jsonify
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host=os.getenv('REDIS_HOST', 'redis'),
              password=os.getenv('REDIS_PASSWORD'),
              socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route('/healthz')
def health_check():
    return 'OK'

@app.route('/')
def hello():
    try:
        visits = redis.incr('counter')
    except RedisError as ex:
        app.logger.error('Could not connect to redis: %s', ex)
        visits = '<i>cannot connect to Redis, counter disabled</i>'

    html = """
<h3>Hello {name}!</h3>
<b>Hostname:</b> {hostname}<br/>
<b>Visits:</b> {visits}
"""
    return html.format(name=os.getenv('NAME', 'world'),
                       hostname=socket.gethostname(),
                       visits=visits)
@app.route("/env")
def env():
    return jsonify(dict(os.environ))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)),
            debug=os.getenv('DEBUG', '0') == '1')
