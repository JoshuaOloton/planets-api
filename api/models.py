from api import db, ma

class Planet(db.Model):
    __tablename__ = "planets"
    planet_id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String)
    planet_type = db.Column(db.String)
    home_star = db.Column(db.String)
    mass = db.Column(db.Float)
    radius = db.Column(db.Float)
    distance = db.Column(db.Float)

    def __repr__(self) -> str:
        return f'Planet {self.planet_id}'


class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

    def __repr__(self) -> str:
        return f'User {self.user_id}'

class PlanetSchema(ma.Schema):
    class Meta:
        fields = (
            'planet_id', 'planet_name', 'planet_type', 'home_star', 'mass', 'radius', 'distance'
            )

class UserSchema(ma.Schema):
    class Meta:
        fields = (
            'user_id', 'first_name', 'last_name', 'email', 'password'
        )

planet_schema = PlanetSchema()
planets_schema = PlanetSchema(many=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)
    