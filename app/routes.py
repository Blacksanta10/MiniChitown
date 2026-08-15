# Routes for the Flask application

import os

from flask import Blueprint, jsonify, render_template
from app.services.cta import get_stops
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

MAPBOX_API_KEY = os.getenv("MAPBOX_API_KEY")  # Get the Mapbox API key from environment variables



main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html", mapbox_api_key=MAPBOX_API_KEY)


@main.route("/api/stops") 
def stops():
    data = get_stops()


    # Return only the stop_id, stop_lat, and stop_lon columns as JSON
    return jsonify(
        data[
            ["stop_id", "stop_lat", "stop_lon"]
        ].to_dict(orient="records")
    )