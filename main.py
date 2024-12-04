from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Load products from JSON
def load_products():
    with open('data/products.json', 'r') as file:
        return json.load(file)

@app.route('/')
def index():
    products = load_products()
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    products = load_products()
    product = next((p for p in products if p['id'] == product_id), None)
    return render_template('product.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    with open('data/products.json') as f:
        products = json.load(f)
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return render_template('product.html', product=product)
    else:
        return "Product not found", 404
