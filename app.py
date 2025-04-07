from flask import Flask, render_template, request,json,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('todo.html')

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():

    itemName = request.form.get('itemName')

    itemDescription = request.form.get('itemDescription')

    return f"Received: {itemName}, {itemDescription}"


@app.route('/api', methods=['GET'])
def get_data():
    with open('info.txt', 'r') as file:
        data = file.read()
        data=data.split()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
