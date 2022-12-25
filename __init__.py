from flask import Flask, render_template, request
from simplifier import simplifier
app = Flask(__name__)


@app.route('/')
def home():
    api_response = request.args.get('input_area')
    if api_response == None:
        send_data = ''
        api_response = ''
    else:
        send_data = simplifier(api_response)
    # print(api_response)
    # Pass the data to the template
    return render_template('index.html', data_input= api_response,data_output=send_data)


@app.route('/api/simplifier', methods=['GET'])
def api_string():
    # Get the request data
    api_response = request.args.get('input_string')
    if api_response == None:
        send_data = ''
    else:
        send_data = simplifier(api_response)
    # You can access the data in the request using the keys of the dictionary
    return send_data


if __name__ == '__main__':
    app.run()