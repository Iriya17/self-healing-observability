from flask import Flask, Response

app = Flask(__name__)


@app.route("/")
def home():
    return "Self-Healing Application is running!"


@app.route("/health")
def health():
    return "healthy", 200


@app.route("/metrics")
def metrics():
    metrics_data = """# HELP app_up Application health status
# TYPE app_up gauge
app_up 1
"""
    return Response(metrics_data, mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)