from datetime import datetime, date
from flask import Blueprint, request, jsonify, Response
from app.database import db
from app.models import WeightEntry

app_routes = Blueprint('app_routes', __name__)


def parse_date(date_str: str) -> date:
    """
        Convert a string in the format 'dd.mm.yyyy' to a date object.
        Either it will return a formatted date object or the actual day as date object.
    """
    try:
        return datetime.strptime(date_str, "%d.%m.%Y").date()
    except ValueError:
        return date.today()


@app_routes.route('/add-weight', methods=['POST'])
def add_weight() -> tuple[Response, int]:
    # Get all the json data
    data = request.get_json()

    # Check and parse the date
    date_obj = parse_date(data.get('date', ''))

    # Get the weight value, store in variable and check if empty
    weight = data.get('weight')
    if not weight:
        return jsonify({'message': 'Bad Request: Weight is missing'}), 400

    # Create the new entry
    new_entry = WeightEntry(date=date_obj, weight=weight)

    # Add the new entry to the database
    db.session.add(new_entry)
    db.session.commit()

    # Get the result / response
    return jsonify({'message': 'Created: New entry created.'}), 201


@app_routes.route('/get-weights', methods=['GET'])
def get_weights() -> tuple[Response, int]:
    # Get all the entries
    entries = WeightEntry.query.all()

    # Check if there were no entries
    if not entries:
        return jsonify({'message': 'Not Found: No content found.'}), 404

    # If not empty, return all of them
    return jsonify([{
        'id': entry.id,
        'date': entry.date.strftime("%d.%m.%Y"),
        'weight': entry.weight
    } for entry in entries]), 200


@app_routes.route('/get-weight-by-date', methods=['GET'])
def get_weight_by_date() -> tuple[Response, int]:
    # Get all the json data
    data = request.get_json()

    # Get the date value, try to parse, using the parse function
    try:
        date_obj = parse_date(data.get('date'))
    except ValueError:
        return jsonify({'message': 'Bad Request: False date or no string given.'}), 400

    # Run the query and get all entries with the specific date
    entries = WeightEntry.query.filter_by(date=date_obj).all()

    # If empty, return 404, otherwise return the entry/entries
    if not entries:
        return jsonify({'message': 'Not Found: No entry found.'}), 404

    return jsonify([{
        'id': entry.id,
        'date': entry.date.strftime("%d.%m.%Y"),
        'weight': entry.weight
    } for entry in entries]), 200


@app_routes.route('/update-weight-entry', methods=['PUT'])
def update_weight() -> tuple[Response, int]:
    # Get all json data, especially the entity id
    data = request.get_json()
    entry_id = data.get('id')
    entry_date = data.get('date')
    entry_weight = data.get('weight')

    # Check if an id is given, otherwise return 400 Bad Request
    if not entry_id:
        return jsonify({'message': 'Bad Request: ID is missing'}), 400

    # Run the query, using the entry ID
    entry = WeightEntry.query.get(data.get('id'))

    # If there is no entry with this id, return 404
    if not entry:
        return jsonify({'message': 'Not Found: No entry found.'}), 404

    # Check if there is a new value for date given, if so, update the entry date value
    if entry_date:
        entry.date = parse_date(data.get('date', entry.date.strftime("%d.%m.%Y")))

    # Check if there is a new value for weight given, if so, update the entry weight value
    if entry_weight:
        entry.weight = data.get('weight', entry.weight)

    if not entry_date and not entry_weight:
        return jsonify({'message': 'Bad Request: At least one new value is needed to update the entry.'}), 400

    # Commit the changes to the database
    db.session.commit()

    # If successful, return 200
    return jsonify({'message': 'OK: Successfully updated the entry.'}), 200


@app_routes.route('/remove-weight-entry', methods=['DELETE'])
def delete_weight() -> tuple[Response, int]:
    # Get all json data, especially the entity id
    data = request.get_json()
    entry_id = data.get('id')

    # Check if an id is given, otherwise return 400 Bad Request
    if not entry_id:
        return jsonify({'message': 'Bad Request: ID is missing'}), 400

    # Run the query with the given id
    entry = WeightEntry.query.get(data.get('id'))

    # Check the query data, if empty, return 404
    if not entry:
        return jsonify({'message': 'Not Found: No entry found.'}), 404

    # If not empty, delete the entry and commit to the database
    db.session.delete(entry)
    db.session.commit()

    # If successful, return 200
    return jsonify({'message': 'OK: Successfully deleted the entry.'}), 200
