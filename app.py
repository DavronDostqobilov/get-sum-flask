from flask import Flask, request

app = Flask(__name__)


@app.route('/api/get-sum/', methods=['GET'])
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
    s=a+b
    return {"sum":s}

if __name__ == "__main__":
    app.run(debug=True,port='4080')