from flask import Flask, request, abort, redirect, render_template
app = Flask(__name__)

robotstxtContent = """User-agent: *
Allow: /
Allow: /docs

User-agent: *
Disallow: /api/calculate/add
Disallow: /api/calculate/subtract
Disallow: /api/calculate/multiply
Disallow: /api/calculate/divide
Disallow: /api/calculate/power"""

@app.errorhandler(400)
def badRequest(error):
    return "Error 400: bad request", 400

@app.errorhandler(403)
def forbidden(error):
    return "Error 403: forbidden", 404

@app.errorhandler(404)
def pageNotFound(error):
    return "Error 404: not found", 404

@app.errorhandler(422)
def unprocessableContent(error):
    return "Error 422: unprocessable content", 422

@app.route('/robots.txt')
def robotRules():
    return robotstxtContent

@app.route('/')
def mainPage():
    return redirect('/docs')

@app.route('/docs')
def docsPage():
    return render_template('index.html')

@app.route('/api/calculate/add')
def calculateAdd():
    try:
        return str(int(request.args.get('firstNumber', '')) + int(request.args.get('secondNumber', '')))
    except ValueError:
        return abort(400)
    except NameError:
        return abort(400)

@app.route('/api/calculate/subtract')
def calculateSubtract():
    try:
        return str(int(request.args.get('firstNumber', '')) - int(request.args.get('secondNumber', '')))
    except ValueError:
        return abort(400)
    except NameError:
        return abort(400)

@app.route('/api/calculate/multiply')
def calculateMultiply():
    try:
        return str(int(request.args.get('firstNumber', '')) * int(request.args.get('secondNumber', '')))
    except ValueError:
        return abort(400)
    except NameError:
        return abort(400)

@app.route('/api/calculate/divide')
def calculateDivide():
    try:
        return str(int(request.args.get('firstNumber', '')) / int(request.args.get('secondNumber', '')))
    except ValueError:
        return abort(400)
    except NameError:
        return abort(400)
    except ZeroDivisionError:
        return abort(422)

@app.route('/api/calculate/power')
def calculatePower():
    try:
        if int(request.args.get('secondNumber', '')) <= 1000:
            return str(pow(int(request.args.get('firstNumber', '')), int(request.args.get('secondNumber', ''))))
        else:
            return abort(403)
    except ValueError:
        return abort(400)
    except NameError:
        return abort(400)

if __name__ == '__main__':
    app.run(debug=False)
