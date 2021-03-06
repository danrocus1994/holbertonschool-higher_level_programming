#!/usr/bin/python3
"""
Lists all states in ascending order
"""


from sqlalchemy import *
import warnings
from sqlalchemy import exc as sa_exc
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


def main():
    engine = create_engine('mysql+mysqldb:' +
                           '//{}:{}@localhost/{}'.format(sys.argv[1],
                                                         sys.argv[2],
                                                         sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.contains('a')).all()
    for state in states:
        print(state)

if __name__ == '__main__':
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        main()
