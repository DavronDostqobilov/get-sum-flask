from flask import Flask, request

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def get_sum():
    """
    this function returns sum of two number from request data.

    Returns:
        json: sum of two number

    Note:
        request data will be like this:
            /api/get-sum/?a=1&b=2
            
        response data will be like this:
            https://github.com/DavronDostqobilov/get-sum-flask.git
                "sum": 3
            }
    """
    a=request.args.get('a')
    b=request.args.get('b')
    s=int(a)+int(b)
    return {"sum":s}
# @app.route('/')
# def value():
#    return "http://127.0.0.1:4080/product<br>http://127.0.0.1:4080/home<br>http://127.0.0.1:4080/contact<br>http://127.0.0.1:4080/about"
# @app.route('/home')
# def home():
#    return "Home Page"
# @app.route('/about')
# def about():
#    return "About Page"
# @app.route('/contact')
# def contact():
#    return "Contact Page"
# @app.route('/product')
# def product():
#    return "Product Page"

if __name__ == "__main__":
    app.run(debug=True,port='4080')