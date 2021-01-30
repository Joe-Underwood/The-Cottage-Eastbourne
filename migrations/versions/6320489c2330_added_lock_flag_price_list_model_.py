"""added lock_flag Price_List model - prevents automatic calculation of prices/discounts etc.

Revision ID: 6320489c2330
Revises: 482c4970f2d5
Create Date: 2021-01-30 12:37:55.085601

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6320489c2330'
down_revision = '482c4970f2d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('price__list', sa.Column('lock_flag', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('price__list', 'lock_flag')
    # ### end Alembic commands ###
