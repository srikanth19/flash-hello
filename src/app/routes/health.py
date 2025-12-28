from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)


@health_bp.route("/healthz")
def health():
    return jsonify(status="ok"), 200


@health_bp.route("/readyz")
def ready():
    return jsonify(status="ready"), 200
