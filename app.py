from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():

    return render_template("index.html")


@app.route("/risk_management", methods=["POST"])
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
    app.run()
