from flask import request, jsonify

# A mock dictionary to simulate user tokens
USER_TOKENS = {
    "user1": "token123",
    "user2": "token456"
}

def authenticate():
    """
    Middleware to verify the token sent in the Authorization header.
    Returns an error response if the token is invalid.
    """
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"message": "Authorization header missing or invalid"}), 401
    
    # Extract the token from the header
    token = auth_header.split(" ")[1]
    if token not in USER_TOKENS.values():
        return jsonify({"message": "Invalid or expired token"}), 403

    return None
