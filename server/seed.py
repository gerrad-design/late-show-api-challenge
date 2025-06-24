from server.models import db
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.models.user import User
from server.app import app

with app.app_context():
    print("🌱 Seeding data...")

    db.drop_all()
    db.create_all()

    u = User(username="admin")
    u.set_password("password")
    db.session.add(u)

    g1 = Guest(name="Zendaya", occupation="Actress")
    g2 = Guest(name="Elon Musk", occupation="Entrepreneur")

    e1 = Episode(date="2025-01-10", number=1)
    e2 = Episode(date="2025-01-11", number=2)

    db.session.add_all([g1, g2, e1, e2])
    db.session.commit()

    a1 = Appearance(rating=4, guest_id=g1.id, episode_id=e1.id)
    a2 = Appearance(rating=5, guest_id=g2.id, episode_id=e2.id)

    db.session.add_all([a1, a2])
    db.session.commit()

    print("✅ Seeding complete.")
