"""add Department

Revision ID: 8253b0140f86
Revises: 03d3bcd12fc8
Create Date: 2024-10-14 07:09:03.443603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8253b0140f86'
down_revision = '03d3bcd12fc8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
