from flask import Flask, request
import docker

app = Flask(__name__)

client = docker.from_env()


@app.route("/remediate", methods=["POST"])
def remediate():
    data = request.get_json(silent=True) or {}

    print("Received alert from Alertmanager")

    alerts = data.get("alerts", [])

    for alert in alerts:
        status = alert.get("status")
        name = alert.get("labels", {}).get("alertname")

        print(f"Alert: {name}, Status: {status}")

        if status == "firing" and name == "ApplicationDown":
            try:
                container = client.containers.get("my-app")

                print("Application is down.")
                print("Starting automated remediation...")

                container.restart()

                print("Remediation completed: my-app restarted.")

            except Exception as e:
                print(f"Remediation failed: {e}")

    return {"status": "remediation processed"}, 200


@app.route("/health")
def health():
    return "remediation service healthy", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)