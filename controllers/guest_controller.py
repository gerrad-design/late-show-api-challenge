from flask import Blueprint, jsonify
from server.models.guest import Guest
from server.models import db

guest_bp = Blueprint('guests', __name__, url_prefix='/guests')

@guest_bp.route('', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    result = [{"id": g.id, "name": g.name, "occupation": g.occupation} for g in guests]
    return jsonify(result), 200
