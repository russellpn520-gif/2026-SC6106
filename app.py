#blockchain application

from os import getenv

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return(render_template("index.html"))

@app.route("/main", methods=["GET", "POST"])
def main():
    return(render_template("main.html"))

@app.route("/transferMoney", methods=["GET", "POST"])
def transferMoney():
    return render_template(
        "transferMoney.html",
        contract_address=getenv(
            "PAYNOW_CONTRACT_ADDRESS",
            "0x80bf920288C42505888e764E03bD3566abf7E75c",
        ),
    )

if __name__ == "__main__":
    app.run()
