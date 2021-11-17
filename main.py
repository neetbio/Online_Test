
from flask import Flask, render_template, request

questions = None# 7 done

with open ("questions.txt", "r") as myfile:
    data = myfile.read().splitlines()
    questions = data
index = 0
last_question = len(questions) - 1

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def hello_world():
    global index
    if request.method == "POST":
        if index == last_question:
            return "<p>You have completed the test. </p>"
        index += 1
        return render_template("index.html", question=questions[index])
    return render_template("index.html", question=questions[index])


if __name__ == "__main__":
    app.run(debug=True)
