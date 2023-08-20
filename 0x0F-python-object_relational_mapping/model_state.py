#!/usr/bin/python3
# Defines State model
# Inherits from SQLAlchemy Base and links to MySQL table states

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
	"""Represent state for MySQL database

	__tablename__ (str): name of MySQL table to store States
	id (sqlalchemy.Integer): state's id
	name (sqlalchemy.String): state's name
	"""
	__tablename__ = "states"
	id = Column(Integer, primary_key=True)
	name = Column(String(128), nullable=False)
