from flask import Flask, request, jsonify

app = Flask(__name__)

user_records = dict()

@app.route("/send_user_data", methods=["POST"])
def handle_send_user_data():
    data = request.get_json()
    if not data:
        return jsonify({"error": "POST body could not be parsed as json"}), 400
    if "key" not in data:
        return jsonify({"error": "request has no key"}), 400
    if "data" not in data:
        return jsonify({"error": "request has no data"}), 400

    user_records[data["key"]] = data["data"]

    return jsonify({"message": "Data sent successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
