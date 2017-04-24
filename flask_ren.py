from sklearn.externals import joblib
import flask
import os

app = flask.Flask(__name__)


@app.route("/survey")
def survey():

    weight = flask.request.args.get("weight", default=None, type=int) / 100
    height = flask.request.args.get("height", default=None, type=float) / 200
    if weight is None or height is None:
        return flask.jsonify({
            "code": 400,
            "msg": "Bad Request"
        })
    pkl = os.getcwd() + "/data/bmi.pkl"
    clf = joblib.load(pkl)

    wh = [[weight, height]]
    bmi = clf.predict(wh)
    pre = bmi[0]
    return flask.jsonify({
        "code": 200,
        "msg": "OK",
        "result": "{0}".format(pre)
    })

if __name__ == "__main__":
    app.run()