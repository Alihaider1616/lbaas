from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        backends = request.form.get("backends").split(",")
        config = "\n".join([f"    server {ip.strip()};" for ip in backends])
        with open("/etc/nginx/conf.d/lb.conf", "w") as f:
            f.write(f"upstream backend {{\n{config}\n}}\n")
            f.write("""server {\n    listen 80;\n    location / {\n        proxy_pass http://backend;\n    }\n}""")
        subprocess.run(["nginx", "-s", "reload"])
        return "Updated!"
    return '''
        <form method="POST">
            Backend IPs (comma separated): <input name="backends">
            <input type="submit">
        </form>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

