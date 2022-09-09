#!/usr/bin/python3
"""State Module"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence

Base = declarative_base()


class State(Base):
    """state object representing a state model

       ___tablname__ - name of the table linked to.
       id (String) - id, primary_key, not null.
       name (String) - the state name (128 characters).
    """
    __tablename__ = 'states'
    id = Column(Integer, Sequence('states_id_seq'), primary_key=True)
    name = Column(String(128), nullable=False)
