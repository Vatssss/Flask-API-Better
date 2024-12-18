from flask import Blueprint, jsonify, request
from models import members

members_bp = Blueprint('members', __name__)

# GET: List all members
@members_bp.route('/members', methods=['GET'])
def get_members():
    return jsonify(members), 200

# POST: Add a new member
@members_bp.route('/members', methods=['POST'])
def add_member():
    data = request.get_json()
    new_member = {
        "id": len(members) + 1,
        "name": data['name'],
        "email": data['email']
    }
    members.append(new_member)
    return jsonify(new_member), 201

# PUT: Update a member
@members_bp.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    data = request.get_json()
    for member in members:
        if member['id'] == member_id:
            member['name'] = data['name']
            member['email'] = data['email']
            return jsonify(member), 200
    return jsonify({"message": "Member not found"}), 404

# DELETE: Remove a member
@members_bp.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    global members
    members = [member for member in members if member['id'] != member_id]
    return jsonify({"message": "Member deleted successfully"}), 200
