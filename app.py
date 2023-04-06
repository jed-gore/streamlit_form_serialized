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
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow_sqlalchemy.fields import Nested


class SmartNested(Nested):
    def serialize(self, attr, obj, accessor=None):
        if attr not in obj.__dict__:
            return {"id": int(getattr(obj, attr + "_id"))}
        return super(SmartNested, self).serialize(attr, obj, accessor)


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


class UserObject(Base):
    __tablename__ = "user_objects"
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    user = relationship("User", backref=backref("users"))


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


class UserObjectSchema(SQLAlchemySchema):
    id = auto_field()
    user = SmartNested(UserSchema)

    class Meta:
        model = UserObject
        sqla_session = session


# create simple streamlit form


def form():
    st.write("Form Template")
    with st.form(key="Information form"):
        name = st.text_input("Enter user name: ")
        object_name = st.text_input("Enter user object: ")
        submission = st.form_submit_button(label="Submit")
        if submission == True:
            add_data(name, object_name)


# add data function drives the SQL insert and commit


def add_data(name, object_name):
    user_object = UserObject(id=1)
    user_object.name = object_name
    user_object.user = User(name=name)
    session.add(user_object)
    session.commit()
    st.success("Saved")

    # st.markdown(dump_data)  # dump the serialized json to the screen

    return


if __name__ == "__main__":
    form()
