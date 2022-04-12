"""empty message

Revision ID: 5b53b4eff741
Revises: 
Create Date: 2022-04-11 10:30:33.320573

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b53b4eff741'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Usuarios')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Usuarios',
    sa.Column('id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='Usuarios_pkey'),
    sa.UniqueConstraint('email', name='Usuarios_email_key'),
    sa.UniqueConstraint('name', name='Usuarios_name_key')
    )
    # ### end Alembic commands ###