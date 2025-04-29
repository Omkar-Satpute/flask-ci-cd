from app import app

@app.route('/')
def home():
    return "Hello, CI/CD with Kubernetes!"

@app.route('/health')
def health():
    return {"status": "healthy"}, 200 #Hello There