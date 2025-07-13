from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy.orm import joinedload, selectinload, load_only

Base = declarative_base()

# ---------------------------------------------
# ORM MODELS
# ---------------------------------------------
class Experiment(Base):
    __tablename__ = "experiments"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    measurements = relationship("Measurement", back_populates="experiment")


class Measurement(Base):
    __tablename__ = "measurements"
    id = Column(Integer, primary_key=True)
    experiment_id = Column(Integer, ForeignKey("experiments.id"))
    value = Column(Float)
    flagged = Column(Boolean, default=False)
    experiment = relationship("Experiment", back_populates="measurements")

