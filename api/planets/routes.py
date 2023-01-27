from . import planets
from .. import db
from ..models import Planet, planet_schema, planets_schema
from flask import jsonify, request
from flask_jwt_extended import jwt_required
from operator import itemgetter


@planets.route('/')
def home():
    return 'Planets HOME'

@planets.route('/planets/', methods=['GET'])
def get_planets():
    planets = Planet.query.all()
    results = planets_schema.dump(planets)
    return jsonify(results), 200


@planets.route('/planets/<int:id>', methods=['GET'])
def get_planet(id):
    planet = Planet.query.get(id)
    result = planet_schema.dump(planet)
    return jsonify(result), 200

@planets.route('/planets', methods=['POST'])
@jwt_required()
def add_planets():
    # python dictionary destructuring
    planet_name, planet_type, home_star, mass, radius, distance = \
    itemgetter('planet_name', 'planet_type', 'home_star', 'mass', 'radius', 'distance')(request.form)

    # convert mass, radius, distance to float
    [mass, radius, distance] = [float(i) for i in [mass, radius, distance]]
    planet = Planet.query.filter_by(planet_name=planet_name).first()
    if planet:  # if planet already exists, return conflict error
        return jsonify(message='Planet already exists'), 409
    planet = Planet(
        planet_name=planet_name,
        planet_type=planet_type,
        home_star=home_star,
        mass=mass,
        radius=radius,
        distance=distance
        )
    db.session.add(planet)
    db.session.commit()
    return jsonify(message='Planet added successfully'), 201    

@planets.route('/planets/<int:id>', methods=['PUT', 'POST'])
@jwt_required()
def update_planets(id):
    planet = Planet.query.get_or_404(id)
    # python dictionary destructuring
    planet_name, planet_type, home_star, mass, radius, distance = \
    itemgetter('planet_name', 'planet_type', 'home_star', 'mass', 'radius', 'distance')(request.form)

    # convert mass, radius, distance to float
    [mass, radius, distance] = [float(i) for i in [mass, radius, distance]]

    planet.planet_name = planet_name
    planet.planet_type = planet_type
    planet.home_star = home_star
    planet.mass = mass
    planet.radius = radius
    planet.distance = distance
    db.session.commit()
    return jsonify(message='Planet updated successfully'), 200   


@planets.route('/planets/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_planet(id):
    planet = Planet.query.get_or_404(id)
    db.session.delete(planet)
    db.session.commit()
    return jsonify(message='Planet deleted successfully!'), 200
