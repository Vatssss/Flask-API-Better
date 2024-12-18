from flask import Flask
from routes.books import books_bp
from routes.members import members_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(books_bp, url_prefix="/api")
app.register_blueprint(members_bp, url_prefix="/api")

@app.route('/')
def home():
    return "Welcome to the Library Management System API! Navigate to `/api/members` or `/api/books` to use the endpoints.", 200

if __name__ == "__main__":
    app.run(debug=True)
