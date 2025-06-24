from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models.appearance import Appearance
from server.models import db

appearance_bp = Blueprint('appearances', __name__, url_prefix='/appearances')

@appearance_bp.route('', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    guest_id = data.get('guest_id')
    episode_id = data.get('episode_id')

    if not (1 <= rating <= 5):
        return jsonify({"error": "Rating must be between 1 and 5"}), 400

    appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
    db.session.add(appearance)
    db.session.commit()

    return jsonify({
        "id": appearance.id,
        "rating": appearance.rating,
        "guest_id": appearance.guest_id,
        "episode_id": appearance.episode_id
    }), 201
