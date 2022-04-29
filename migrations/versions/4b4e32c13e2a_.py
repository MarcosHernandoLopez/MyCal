"""empty message

Revision ID: 4b4e32c13e2a
Revises: 
Create Date: 2022-04-29 11:18:45.533888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b4e32c13e2a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('GruposTEMP',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('owner', sa.String(), nullable=False),
    sa.Column('members', sa.ARRAY(sa.String()), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('GruposTEMP')
    # ### end Alembic commands ###