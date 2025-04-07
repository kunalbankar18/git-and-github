from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('todo.html')

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    itemName = request.form.get('itemName')
    itemDescription = request.form.get('itemDescription')
    return f"Received: {itemName}, {itemDescription}"

if __name__ == '__main__':
    app.run(debug=True)
