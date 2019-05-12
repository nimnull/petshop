from sqlalchemy import (
    Table, Integer, Column, String, ARRAY, ForeignKeyConstraint, PrimaryKeyConstraint
)

# from sqlalchemy.dialects import postgresql
from extensions import db

metadata = db.metadata


maker = Table(
    'maker', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255), nullable=False),
    Column('normalized_name', String(255), nullable=False),
    Column('url', String(255), nullable=False),
    Column('parser_cls', String(255))
)

component = Table(
    'component', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255), nullable=False),
    Column('name_variants', ARRAY(String(255)))
)

product = Table(
    'product', metadata,
    Column('id', Integer, primary_key=True),
    Column('maker_id', Integer),
    Column('sku', String(255), index=True),
    Column('name', String(255)),
    Column('name_variants', ARRAY(String(255))),
    ForeignKeyConstraint(('maker_id',), ['maker.id'])
)

product_variant = Table(
    'product_variant', metadata,
    Column('id', Integer, primary_key=True),
    Column('product_id', Integer),
    ForeignKeyConstraint(('product_id',), ['product.id'])
)

product_component = Table(
    'product_component', metadata,
    Column('product_id', Integer, nullable=False),
    Column('component_id', Integer, nullable=False),
    PrimaryKeyConstraint('product_id', 'component_id', name='product_component_pk'),
    ForeignKeyConstraint(('product_id',), ['product.id']),
    ForeignKeyConstraint(('component_id',), ['component.id']),
)
