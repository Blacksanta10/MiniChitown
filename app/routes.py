# Routes for the Flask application

from flask import Blueprint, jsonify, render_template

from app.services.cta import get_stops

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html")


@main.route("/api/stops") 
def stops():
    data = get_stops()


    # Return only the stop_id, stop_lat, and stop_lon columns as JSON
    return jsonify(
        data[
            ["stop_id", "stop_lat", "stop_lon"]
        ].to_dict(orient="records")
    )