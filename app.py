from flask import Flask, render_template, jsonify

#import flask and create app var
app = Flask(__name__)

#create list of items to sell
PRODUCTS = [
    {
      'id': 1, 
      'item': 'Stickers',
      'description': 'Easter',
      'cost': '£1'
    },
    {
      'id': 2, 
      'item': 'Plushie',
      'description': 'Octopus',
      'cost': '£5'
    },
    {
      'id': 3, 
      'item': 'Badge',
      'description': 'Coding',
    }
]

#what route is required/registered for app
@app.route("/")
def helloWorld():
  return render_template('home.html', 
                          products=PRODUCTS,
                          company_name = 'Plush'
                        )
  
#second page - as a json'd structure
@app.route("/api/products")
def list_products():
  return jsonify(PRODUCTS)


#this IF will check route and execute prog
if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug=True)