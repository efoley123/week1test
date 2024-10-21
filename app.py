from flask import Flask, render_template, request, render_template_string, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html") ##would need a template folder and then need index.html in there and then this works




# Define the route to handle POST requests
@app.route('/new-commit', methods=['POST'])
def handle_new_commit():
    # Extract the JSON payload sent in the POST request
    payload = request.json
    # Do something with the payload, for example, print it
    print("Received payload:", payload)
    
    # Process the data (you can add logic to handle specific commit details here)
    
    return jsonify({'status': 'success', 'message': 'POST request received'}), 200

if __name__ == '__main__':
    app.run(port=3000)