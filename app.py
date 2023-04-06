import streamlit as st

import sqlalchemy as sa

# relationship and backref will be used in a future push

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    backref,
    declarative_base,
)

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

# create local sqlite db
engine = sa.create_engine("sqlite:///data.db", echo=True)
session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()

# declare modules


class User(Base):
    __tablename__ = "users"
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)

    def __repr__(self):
        return "<User(name={self.name!r})>".format(self=self)


# create tables ( strange error if already exists - so this is caught in a try except )
try:
    Base.metadata.create_all(engine)
except:
    print("database already created")


# generate marshmallow schemas


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True


# create simple streamlit form


def form():
    st.write("Form Template")
    with st.form(key="Information form"):
        name = st.text_input("Enter user name: ")

        submission = st.form_submit_button(label="Submit")
        if submission == True:
            add_data(name)


# add data function drives the SQL insert and commit


def add_data(name):
    user = User(name=name)
    user_schema = UserSchema()
    session.add(user)
    session.commit()
    st.success("Saved")
    dump_data = user_schema.dump(user)
    st.markdown(dump_data)  # dump the serialized json to the screen

    return


# run the form
if __name__ == "__main__":
    form()
