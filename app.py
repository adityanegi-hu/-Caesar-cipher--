from flask import Flask, render_template, request, jsonify

from Cipher import encrypt, decrypt

app = Flask(__name__)


@app.route("/")
def index():
    """Render the main Caesar cipher page."""
    return render_template("index.html")


@app.route("/api/cipher", methods=["POST"])
def api_cipher():
    """
    Simple JSON API for Caesar cipher operations.

    Expected JSON body:
    {
        "text": "hello",
        "shift": 3,
        "mode": "encrypt" | "decrypt"
    }
    """
    data = request.get_json(silent=True) or {}

    text = data.get("text", "")
    mode = data.get("mode", "encrypt")

    try:
        shift = int(data.get("shift", 0))
    except (TypeError, ValueError):
        return jsonify({"error": "Shift must be an integer."}), 400

    # Normalize shift to 0-25 range
    shift = shift % 26

    if mode == "encrypt":
        result = encrypt(text, shift)
    elif mode == "decrypt":
        result = decrypt(text, shift)
    else:
        return jsonify({"error": "Mode must be 'encrypt' or 'decrypt'."}), 400

    return jsonify(
        {
            "result": result,
            "mode": mode,
            "shift": shift,
        }
    )


if __name__ == "__main__":
    # Run in development mode
    app.run(debug=True)

