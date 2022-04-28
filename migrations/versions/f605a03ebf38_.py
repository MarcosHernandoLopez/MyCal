"""empty message

Revision ID: f605a03ebf38
Revises: 22650f69abe1
Create Date: 2022-04-28 08:13:54.538090

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f605a03ebf38'
down_revision = '22650f69abe1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('GruposTEMP',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('GruposTEMP')
    # ### end Alembic commands ###
