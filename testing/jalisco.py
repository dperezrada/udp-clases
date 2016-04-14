from flask import Flask, jsonify, request


# create our little application :)
app = Flask(__name__)

def calculate_jalisco_number(input_number):
    print(store_in_database(input_number))
    return input_number+1

def store_in_database(number):
    return "SAVED"

@app.route('/')
def index():
    try:
        input_number = int(request.args.get('number'))
    except Exception, e:
        return jsonify(**{'message': 'Error'})

    jalisco_number = calculate_jalisco_number(input_number)
    if jalisco_number > input_number:
        message_text = 'Yo gano con el %s' % jalisco_number
    else:
        message_text = 'Tu ganas con el %s' % input_number
    to_return = {
        'message': message_text
    }
    return jsonify(**to_return)

if __name__ == "__main__":
    app.run(debug=True)
