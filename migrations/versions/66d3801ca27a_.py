"""empty message

Revision ID: 66d3801ca27a
Revises: c62d1bcbf8e7
Create Date: 2021-01-06 17:23:09.262776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66d3801ca27a'
down_revision = 'c62d1bcbf8e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('delete__booking_ibfk_1', 'delete__booking', type_='foreignkey')
    op.drop_constraint('delete__price__list_ibfk_1', 'delete__price__list', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('delete__price__list_ibfk_1', 'delete__price__list', 'booking', ['booking_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key('delete__booking_ibfk_1', 'delete__booking', 'customer', ['customer_id'], ['id'])
    # ### end Alembic commands ###
