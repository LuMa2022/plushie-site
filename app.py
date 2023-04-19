from flask import Flask

#import flask and create app var
app = Flask(__name__)

#what route is required/registered for app
@app.route("/")
def helloWorld():
  return "Hello World"





#this IF will check route and execute prog
if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug=True)