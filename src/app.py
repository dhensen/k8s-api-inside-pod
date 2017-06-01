from flask import Flask
from flask_json import as_json, FlaskJSON
from kubernetes import client

app = Flask(__name__)
json = FlaskJSON(app)

client.configuration.host = 'http://127.0.0.1:8001'


@app.route("/")
@as_json
def hello():
    return {'message': 'hello world!'}


@app.route("/pods")
@as_json
def get_pods():
    v1 = client.CoreV1Api()
    pods = []
    ret = v1.list_pod_for_all_namespaces(watch=False)

    for i in ret.items:
        pods.append(
            {
                'pod_ip': i.status.pod_ip,
                'namespace': i.metadata.namespace,
                'name': i.metadata.name
            }
        )

    return {'pods': pods}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
