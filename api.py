from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    1: {
        "name": "Alex",
        "age": 25
    },
    2: {
        "name": "Max",
        "age": 28
    },
    3: {
        "name": "Egor",
        "age": 15
    },
}

@app.route('/hello_world', methods=['GET'])
def sayhelloworld():
    data = {
        1: "Hello World"
    }
    return jsonify(data)

@app.route('/users/<int:idu>', methods=['GET'])
def returnUserInfo(idu):
    user_info = users.get(idu)
    if user_info:
        return jsonify(user_info)
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
