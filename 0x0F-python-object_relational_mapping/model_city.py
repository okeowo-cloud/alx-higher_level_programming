#!/usr/bin/python3
"""City Module"""

from model_state import Base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey


class City(Base):
    """state object representing a state model

       ___tablname__ - name of the table linked to.
       id (String) - id, primary_key, not null.
       name (String) - the state name (128 characters).
       state_id(Integer) - state id, not null, Foreign key.
    """
    __tablename__ = 'cities'
    id = Column(Integer, Sequence('states_id_seq'), primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
