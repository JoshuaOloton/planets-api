from api import create_app, db
from api.models import Planet, User

app = create_app()


@app.cli.command("db_create")
def db_create():
    print('Database created!')
    db.create_all()


@app.cli.command("db_drop")
def db_drop():
    print('Database dropped!')
    db.drop_all()

@app.cli.command("db_seed")
def db_seed():
    print('Database seeded!')
    user = User(
        first_name='Joshua',
        last_name='Oloton',
        email='olotonjoshua@gmail.com'
    )

    db.session.add(user)

    mercury = Planet(
        planet_name='Mercury',
        planet_type='Class D',
        home_star='Sol',
        mass=3.528e23,
        radius=1516,
        distance=35.98e6
    )
    venus = Planet(
        planet_name='Venus',
        planet_type='Class K',
        home_star='Sol',
        mass=4.867e23,
        radius=3760,
        distance=67.24e6
    )
    earth = Planet(
        planet_name='Earth',
        planet_type='Class M',
        home_star='Moon',
        mass=5.972e24,
        radius=3959,
        distance=92.96e6
    )

    db.session.add_all([mercury, venus, earth])
    db.session.commit()


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Planet=Planet)

if __name__ == "__main__":
    app.run(debug=True)