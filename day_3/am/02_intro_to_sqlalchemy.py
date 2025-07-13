"""
02_intro_to_orm_sqlalchemy.py
=============================

Intro to SQLAlchemy ORM for Scientific Data
-------------------------------------------

This script shows how to manage database sessions in SQLAlchemy,
comparing the older custom context manager approach (pre-v1.4)
to the built-in context-manager support introduced in v1.4.

"""

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# ----------------------------------------------------
# 1. SETUP
# ----------------------------------------------------

# Change to "sqlite:///:memory:" to use an in-memory database for testing
engine = create_engine("sqlite:///materials.db", echo=True)
Base = declarative_base()

class Material(Base):
    __tablename__ = "aero_materials"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    yield_strength = Column(Float)  # Measured in MPa

    def __repr__(self):
        return f"<Material(name={self.name!r}, yield_strength={self.yield_strength} MPa)>"

# Create table if it doesn't exist
Base.metadata.create_all(engine)

# ----------------------------------------------------
# 2. SESSION MANAGEMENT OPTIONS
# ----------------------------------------------------

Session = sessionmaker(bind=engine)

# --- Option A: Custom context manager (pre-SQLAlchemy 1.4) ---
#
# In versions before 1.4, Session did not support `with` directly.
# You needed to wrap session creation and teardown yourself:
#
# from contextlib import contextmanager
#
# @contextmanager
# def session_scope():
#     """Provide a transactional scope around a series of operations."""
#     session = Session()          # create a new Session
#     try:
#         yield session            # run work in this block
#         session.commit()         # commit if no errors
#     except:
#         session.rollback()       # rollback on error
#         raise
#     finally:
#         session.close()          # always close
#
# Starting in SQLAlchemy 1.4, the Session returned by sessionmaker()
# implements __enter__ and __exit__, so you can use `with` directly:
#
# - On normal exit: commits transaction and closes session
# - On exception: rolls back transaction and closes session

# ----------------------------------------------------
# 3. DEMO CRUD within the built-in context manager
# ----------------------------------------------------

with Session() as session:
    # CREATE
    session.add(Material(name="Inconel 718", yield_strength=1030))
    # No explicit session.commit() needed here; commit happens on block exit

    # READ
    print("\nStored Materials:")
    for mat in session.query(Material).all():
        print(mat)

    # UPDATE
    mat = session.query(Material).filter_by(name="Inconel 718").first()
    if mat:
        mat.yield_strength = 1050
        # change is tracked; committed automatically

    # DELETE
    mat = session.query(Material).filter_by(name="Inconel 718").first()
    if mat:
        session.delete(mat)
        # deletion is tracked; committed automatically

# After this block, session is closed even if an error occurred.
