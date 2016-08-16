from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/result', methods=['GET', 'POST'])
def result():
    calculations = {
        "+": lambda first_number, second_number: first_number + second_number,
        "-": lambda first_number, second_number: first_number - second_number,
        "*": lambda first_number, second_number: first_number * second_number,
        "/": lambda first_number, second_number: first_number / second_number
    }
    form = request.form

    try:
        first_number = float(form["first_number"])
        operation = form["operation"]
        second_number = float(form["second_number"])
        final_result = "Result: " + str(calculations[operation](first_number, second_number))
    except ValueError:
        final_result = "Invalid input!"
    except KeyError:
        final_result = "Invalid input! Put only +, -, * or /"
    except ZeroDivisionError:
        final_result = "Division by zero!"
    return render_template("result.html", form=form, result=final_result)


if __name__ == '__main__':
    app.run()
