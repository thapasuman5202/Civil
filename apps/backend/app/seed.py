from .db.session import engine, SessionLocal
from .db.base import Base
from .models import User, SiteTwin, Variant, Constraint
from .core import security


def run() -> None:
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    if not db.query(User).filter(User.email == "demo@demo.com").first():
        user = User(email="demo@demo.com", password_hash=security.get_password_hash("password"))
        db.add(user)
        db.commit()
        db.refresh(user)
        st = SiteTwin(name="Kathmandu Site", region_code="NP", created_by=user.id)
        db.add(st)
        db.commit()
        db.refresh(st)
        constraint = Constraint(site_twin_id=st.id, kind="height", value="10m")
        db.add(constraint)
        variant1 = Variant(site_twin_id=st.id, name="Variant A", score_primary=70.0, scores_json={"energy":70,"cost":55,"speed":80}, status="scored")
        variant2 = Variant(site_twin_id=st.id, name="Variant B", score_primary=60.0, scores_json={"energy":60,"cost":50,"speed":75}, status="scored")
        db.add_all([variant1, variant2])
        db.commit()
    db.close()


if __name__ == "__main__":
    run()
