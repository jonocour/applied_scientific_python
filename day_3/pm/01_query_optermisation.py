"""
01_query_optimisation.py
==========================

Reference Guide: Choosing Efficient ORM Query Patterns
-------------------------------------------------------

| Use Case                         | Preferred Loading Strategy        |
|----------------------------------|----------------------------------|
| Few parents, lots of children    | joinedload()                      |
| Many parents, few children       | selectinload()                    |
| Deep nesting, conditional access | lazy (default) or conditional     |
| Streaming large result sets      | .yield_per() + .load_only()       |
| You don’t need ORM objects       | bulk_insert(), .values(), .update() |

Topics Covered:
---------------
- Avoiding N+1 queries
- Using joinedload vs selectinload
- Batched streaming with .yield_per()
- Efficient filtering using .in_() and subqueries
- Minimizing ORM overhead with bulk operations
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import joinedload, selectinload, load_only, Session
from day_3.pm.utility.model_for_optermisation import Experiment, Measurement, Base


# ---------------------------------------------
# EXAMPLES
# ---------------------------------------------

def use_joinedload(session):
    """
    Use Case: Few parent records, many related children per parent.

    Strategy: Use `joinedload()` to fetch parent + child rows in a single joined query.
    Benefit: Avoids N+1 query problem by eager-loading child relationships.

    Avoid on large result sets — joined rows can multiply quickly.
    """
    experiments = session.query(Experiment)\
                         .options(joinedload(Experiment.measurements))\
                         .all()
    for exp in experiments:
        print(f"{exp.name}: {len(exp.measurements)} measurements")


def use_selectinload(session):
    """
    Use Case: Many parent records, relatively small or no child records.

    Strategy: Use `selectinload()` to fetch parent rows in one query,
    then child rows for all parents in a second query using `WHERE IN (...)`.

    Benefit: Avoids N+1 problem without costly joins.
    """
    experiments = session.query(Experiment)\
                         .options(selectinload(Experiment.measurements))\
                         .all()
    for exp in experiments:
        print(f"{exp.name}: {len(exp.measurements)} measurements")


def stream_large_table(session, batch_size=1000):
    """
    Use Case: Large dataset that won't fit in memory.

    Strategy: Use `.yield_per()` to stream rows from the database in chunks,
    and `.load_only()` to fetch only the required columns.

    Benefit: Minimal memory footprint, scalable for long-running scripts.
    """
    for row in session.query(Measurement)\
                      .options(load_only(Measurement.id, Measurement.value))\
                      .yield_per(batch_size):
        _ = row.value  # Simulate light processing


def bulk_update_flags(session):
    """
    Use Case: Flag large number of rows based on a condition.

    Strategy: Use `.update()` directly on the query, bypassing ORM object hydration.

    Benefit: Massive speedup over looping through objects and setting attributes.

    Use `synchronize_session=False` unless you're also updating the session in memory.
    """
    session.query(Measurement)\
           .filter(Measurement.value < 0.1)\
           .update({Measurement.flagged: True}, synchronize_session=False)
    session.commit()


def bulk_insert_values(session, values):
    """
    Use Case: Insert a large number of rows efficiently.

    Strategy: Use `session.bulk_save_objects()` instead of adding one-by-one.

    Benefit: Skips identity map management, flushing, and unnecessary ORM tracking.
    """
    objects = [Measurement(value=v) for v in values]
    session.bulk_save_objects(objects)
    session.commit()


def join_with_subquery(session):
    """
    Use Case: Join child table with a subset of parent rows.

    Strategy: Use a subquery to restrict the join to relevant parent records only.

    Benefit: Faster than joining on the entire parent table, especially with filters.
    Useful when building dashboards or analytics from subsets.
    """
    subq = session.query(Experiment.id)\
                  .filter(Experiment.name.like("Exp%")).subquery()
    results = session.query(Measurement)\
                     .join(Experiment)\
                     .filter(Experiment.id.in_(subq))\
                     .all()
    print(f"Joined {len(results)} measurements")


# ---------------------------------------------
# SETUP & SEEDING
# ---------------------------------------------
def setup_demo_data(session):
    """Seed a small dataset with 10 experiments and variable-length measurements."""
    for i in range(10):
        exp = Experiment(name=f"Exp_{i}")
        exp.measurements = [Measurement(value=(i + j) / 10) for j in range(i % 5)]
        session.add(exp)
    session.commit()


# ---------------------------------------------
# MAIN (EXAMPLES IN ACTION)
# ---------------------------------------------
if __name__ == "__main__":
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    session = Session(engine)

    setup_demo_data(session)

    print("\n-- joinedload example --")
    use_joinedload(session)

    print("\n-- selectinload example --")
    use_selectinload(session)

    print("\n-- streaming with yield_per --")
    stream_large_table(session, batch_size=3)

    print("\n-- bulk update flags --")
    bulk_update_flags(session)

    print("\n-- subquery join --")
    join_with_subquery(session)
