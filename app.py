from flask import Flask, render_template, redirect
import os

app = Flask(__name__)

# Wompi checkout URL from environment variable
WOMPI_URL = os.getenv("WOMPI_URL", "https://checkout.wompi.co/l/ir6F3Y")

@app.route("/")
def landing():
    return render_template(
        "index.html",
        wompi_url=WOMPI_URL
    )

@app.route("/comprar")
def comprar():
    return redirect(WOMPI_URL)

if __name__ == "__main__":
    app.run()

