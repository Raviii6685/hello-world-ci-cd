from flask import Flask, jsonify
app= Flask(__name__)

@app.get("/")
def hello():
    return jsonify(
        message="Just a dummy app created by RAVI",
        tip= "Built with the Flask ,shipped by jenkins,running in docker (first ci/cd deployment)"
    )

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
