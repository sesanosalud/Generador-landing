from flask import Flask, render_template, redirect
import os

app = Flask(__name__)

WOMPI_URL = os.getenv("WOMPI_URL", "https://checkout.wompi.co/l/ir6F3Y")

@app.route("/")
def landing():
    return render_template("index.html")

@app.route("/comprar")
def comprar():
    return redirect(WOMPI_URL)

if __name__ == "__main__":
    app.run()
