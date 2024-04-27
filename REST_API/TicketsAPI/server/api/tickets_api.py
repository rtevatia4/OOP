from flask import (request, jsonify, Blueprint, url_for, make_response)
from .ticket_data_store import tickets

tickets_blueprint = Blueprint('tickets_api', __name__, url_prefix='/api/')

@tickets_blueprint.route('/tickets', methods=['GET'])
def list_tickets():
    return jsonify(tickets)

@tickets_blueprint.route('/ticket/<id>', methods=["GET"])
def get_tickets(id):
    response = None
    for ticket in tickets:
        if ticket['id'] == id:
            response = ticket
            break
    return jsonify(response)