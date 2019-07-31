"""account confirmation

Revision ID: 4165018bcd58
Revises: 9fabcf18d9c5
Create Date: 2019-07-29 16:53:15.489665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4165018bcd58'
down_revision = '9fabcf18d9c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###
