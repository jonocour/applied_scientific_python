# models.py
# =========
# Declarative ORM Models Only
# ---------------------------
# This module uses SQLAlchemy's declarative base to define Python classes
# that map directly to SQL database tables.
# Each class attribute corresponds to a table column.

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    TIMESTAMP,
    ForeignKey,
    UniqueConstraint
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# --------------------------------------------------
# WHAT IS declarative_base?
# --------------------------------------------------
# SQLAlchemy's `declarative_base()` returns a base class for our ORM models.
# When you subclass from Base, SQLAlchemy gathers metadata (table names,
# column definitions, constraints) automatically.
# This metadata drives the creation of SQL tables and the mapping between
# Python objects and database rows.

Base = declarative_base()

class Material(Base):
    """
    Represents an aerospace material.

    - `__tablename__` defines the actual SQL table name.
    - Column definitions map to SQL columns: name, type, and constraints.
    """
    __tablename__ = "materials"

    # Primary key column: auto-incrementing integer
    material_id = Column(Integer, primary_key=True, autoincrement=True)
    # Unique material name
    name = Column(String(100), nullable=False, unique=True)
    # Yield strength in MPa
    yield_strength = Column(Float, nullable=False)
    # Soft delete flag or active status
    is_active = Column(Boolean, default=True)

    # Timestamps controlled by the database server
    created_at = Column(
        TIMESTAMP,
        server_default="CURRENT_TIMESTAMP",
        nullable=False
    )
    updated_at = Column(
        TIMESTAMP,
        server_default="CURRENT_TIMESTAMP",
        nullable=False,
        onupdate="CURRENT_TIMESTAMP"
    )

    # One-to-many relationship: Material -> TestRun
    # `back_populates` defines a bi-directional link.
    # `cascade="all, delete"` ensures deleting a Material removes its TestRuns.
    test_runs = relationship(
        "TestRun",
        back_populates="material",
        cascade="all, delete"
    )

    def __repr__(self):
        return (
            f"<Material(name={self.name!r}, yield_strength={self.yield_strength} MPa, "
            f"is_active={self.is_active})>"
        )

class TestRun(Base):
    """
    Represents a single stress test run on a material.

    - Maps to `test_runs` SQL table.
    - Each TestRun references a Material via a foreign key.
    """
    __tablename__ = "test_runs"

    # Primary key for test runs
    run_id = Column(Integer, primary_key=True, autoincrement=True)
    # Foreign key linking back to `materials.material_id`
    material_id = Column(Integer, ForeignKey("materials.material_id"), nullable=False)
    # Measured stress result for this run
    result = Column(Float, nullable=False)

    # Timestamp when this run record was created
    created_at = Column(
        TIMESTAMP,
        server_default="CURRENT_TIMESTAMP",
        nullable=False
    )

    # ORM relationship: each TestRun is linked to one Material
    material = relationship("Material", back_populates="test_runs")

    def __repr__(self):
        return f"<TestRun(material_id={self.material_id}, result={self.result})>"
