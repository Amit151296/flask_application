from flask import Flask,render_template 
app = Flask(__name__)

@app.route('/product')
def product():
    return render_template("product.html")

@app.service('/service')
def service():
    return render_template("product.html")

@app.about('/about')
def service():
    print("Amit kumar is a best boy in the world")


if __name__=="__main__":
    app.run(debug=True, port=8000)
