"""added progressive_payments table

Revision ID: 1cc33578c2ce
Revises: 8b1051d3f978
Create Date: 2021-05-08 20:37:29.676845

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1cc33578c2ce'
down_revision = '8b1051d3f978'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('progressive_payments',
    sa.Column('price_list_id', sa.Integer(), nullable=True),
    sa.Column('due_by', sa.Date(), nullable=True),
    sa.Column('amount_due', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('first_payment', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['price_list_id'], ['price__list.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('progressive_payments')
    # ### end Alembic commands ###
