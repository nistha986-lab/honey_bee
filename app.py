from flask import Flask, render_template, request

app = Flask(__name__)

categories = {}

types = [
    "lip balm",
    "skin tint",
    "lip gloss",
    "foundation",
    "powder",
    "perfume",
    "lipstick",
    "eye shade"
]

images = {

    "lip balm":
    "https://images.unsplash.com/photo-1586495777744-4413f21062fa",

    "skin tint":
    "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9",

    "lip gloss":
    "https://images.unsplash.com/photo-1596462502278-27bfdc403348",

    "foundation":
    "https://images.unsplash.com/photo-1612817288484-6f916006741a",

    "powder":
    "https://images.unsplash.com/photo-1625772452859-1c03d5bf1137",

    "perfume":
    "https://images.unsplash.com/photo-1541643600914-78b084683601",

    "lipstick":
    "https://images.unsplash.com/photo-1631730359585-38a4935cbec4",

    "eye shade":
    "https://images.unsplash.com/photo-1512496015851-a90fb38ba796"
}


for t in types:

    categories[t] = []

    for i in range(1, 21):

        categories[t].append({

            "name": f"{t.title()} {i}",

            "price": f"₹{299 + i * 40}",

            "desc":
            "Summer Glow • Long Lasting • Honey Bee",

            "image": images[t]

        })


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form["name"]

        category = request.form["category"]

        return render_template(
            "products.html",
            name=name,
            products=categories[category]
        )

    return render_template("home.html")


@app.route("/checkout", methods=["POST"])
def checkout():

    selected = request.form.getlist("product")

    return render_template(
        "checkout.html",
        selected=selected
    )


@app.route("/success", methods=["POST"])
def success():

    location = request.form["location"]

    phone = request.form["phone"]

    extra = request.form["extra"]

    return render_template(
        "success.html",
        location=location,
        phone=phone
    )


if __name__ == "__main__":

    app.run(
        debug=True,
        port=5001
    )