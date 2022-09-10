#!/usr/bin/python3
"""12-model_state_update_id_2 Module"""

import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    mod_state = None
    for state in session.query(State):
        if state.id == 2:
            mod_state = state

    if mod_state is not None:
        mod_state.name = 'New Mexico'
        session.commit()
