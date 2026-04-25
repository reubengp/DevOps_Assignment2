from flask import Blueprint, jsonify

from app.data import MEMBERS, PLANS, WORKOUTS

main_bp = Blueprint("main", __name__)


@main_bp.get("/")
def home():
    return (
        jsonify(
            {
                "app": "ACEest Fitness & Gym",
                "message": "Welcome to the ACEest Fitness API",
                "routes": ["/", "/workouts", "/members", "/plans"],
            }
        ),
        200,
    )


@main_bp.get("/workouts")
def workouts():
    return jsonify({"workouts": WORKOUTS}), 200


@main_bp.get("/members")
def members():
    return jsonify({"members": MEMBERS}), 200


@main_bp.get("/plans")
def plans():
    return jsonify({"plans": PLANS}), 200
