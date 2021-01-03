"""empty message

Revision ID: 2e8131157fad
Revises: 2e357ecc219a
Create Date: 2020-12-26 18:08:52.980851

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e8131157fad'
down_revision = '2e357ecc219a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('booking', sa.Column('dog_price', sa.Numeric(precision=10, scale=2), nullable=True))
    op.add_column('booking', sa.Column('stay_price', sa.Numeric(precision=10, scale=2), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('booking', 'stay_price')
    op.drop_column('booking', 'dog_price')
    # ### end Alembic commands ###