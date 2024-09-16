from flask import Flask, jsonify
from math_operations import add_numbers

app = Flask(__name__)

#Define the prices and quantities of individual items
item_prices = []
item_quantities = []

@app.route('/calculate_total', method=['GET'])
def calculate_total():
    #Calculate the total value os items
    total_items = sum(price*quantity for price, quantity in zip(item_prices, item_quantities))
    #Define the delivery fee
    delivery_fee = 5.99

    #Calculate the total cost of the checkout
    result = add_numbers(total_items, delivery_fee)

    return jsonify({'total_cost': result})

