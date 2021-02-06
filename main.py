from flask import Flask, render_template, request

Flask_App = Flask(__name__)


@Flask_App.route("/", methods=["GET"])
def index():

    return render_template("index.html")


@Flask_App.route("/risk_management", methods=["POST"])
def risk_management():
    total_capital = float(request.form["TradeCapital"])
    buy_price = float(request.form["BuyPrice"])
    sl_price = float(request.form["StopLossPrice"])
    risk = float(request.form["Risk_Percentage"])

    sl_risk = (buy_price - sl_price)/buy_price * 100
    risk_size = (risk/100)*total_capital
    shares = risk_size/(buy_price-sl_price)
    shares_value = shares * buy_price

    return render_template(
        "index.html",
        sl_risk=round(sl_risk, 2),
        risk_size=risk_size,
        shares=round(shares, 2),
        shares_value=round(shares_value, 2),
        calculation_success=True
    )


if __name__ == "__main__":
    Flask_App.run(host="0.0.0.0", port=5050, debug=True)
