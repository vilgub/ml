from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/v1/models/use:predict', methods=['POST'])
def get_data():
    r = list(np.random.rand(512))
    return jsonify(outputs=[r])

if __name__ == "__main__":
    app.run()