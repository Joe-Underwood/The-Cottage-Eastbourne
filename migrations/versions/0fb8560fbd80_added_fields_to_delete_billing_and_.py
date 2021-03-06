"""added fields to delete_billing and delete_price_list models

Revision ID: 0fb8560fbd80
Revises: 85d8798f5346
Create Date: 2021-04-30 13:54:01.288362

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0fb8560fbd80'
down_revision = '85d8798f5346'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('delete__billing', sa.Column('credit_note_reference', sa.Integer(), nullable=True))
    op.add_column('delete__billing', sa.Column('debit_note_reference', sa.Integer(), nullable=True))
    op.add_column('delete__billing', sa.Column('invoice_due_date', sa.Date(), nullable=True))
    op.add_column('delete__billing', sa.Column('invoice_reference', sa.Integer(), nullable=True))
    op.add_column('delete__billing', sa.Column('invoice_status', sa.Enum('NOT_SENT', 'ACTIVE', 'OVERDUE', 'PAID', 'INACTIVE', name='invoice_status'), nullable=True))
    op.add_column('delete__billing', sa.Column('linked_invoice_id', sa.Integer(), nullable=True))
    op.add_column('delete__billing', sa.Column('payment_reference', sa.Integer(), nullable=True))
    op.add_column('delete__billing', sa.Column('transaction_type', sa.Enum('INVOICE', 'PAYMENT', 'DEBIT_NOTE', 'CREDIT_NOTE', name='transaction_type'), nullable=False))
    op.create_unique_constraint(None, 'delete__billing', ['credit_note_reference'])
    op.create_unique_constraint(None, 'delete__billing', ['payment_reference'])
    op.create_unique_constraint(None, 'delete__billing', ['invoice_reference'])
    op.create_unique_constraint(None, 'delete__billing', ['debit_note_reference'])
    op.create_foreign_key(None, 'delete__billing', 'billing', ['linked_invoice_id'], ['id'])
    op.drop_column('delete__billing', 'is_credit')
    op.drop_column('delete__billing', 'is_payment')
    op.drop_column('delete__billing', 'is_invoice')
    op.drop_column('delete__billing', 'is_debit')
    op.add_column('delete__price__list', sa.Column('no_discount_price_2_weeks', sa.Numeric(precision=10, scale=2), nullable=True))
    op.add_column('delete__price__list', sa.Column('no_discount_price_3_weeks', sa.Numeric(precision=10, scale=2), nullable=True))
    op.add_column('delete__price__list', sa.Column('no_discount_price_4_weeks', sa.Numeric(precision=10, scale=2), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('delete__price__list', 'no_discount_price_4_weeks')
    op.drop_column('delete__price__list', 'no_discount_price_3_weeks')
    op.drop_column('delete__price__list', 'no_discount_price_2_weeks')
    op.add_column('delete__billing', sa.Column('is_debit', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('delete__billing', sa.Column('is_invoice', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('delete__billing', sa.Column('is_payment', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('delete__billing', sa.Column('is_credit', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'delete__billing', type_='foreignkey')
    op.drop_constraint(None, 'delete__billing', type_='unique')
    op.drop_constraint(None, 'delete__billing', type_='unique')
    op.drop_constraint(None, 'delete__billing', type_='unique')
    op.drop_constraint(None, 'delete__billing', type_='unique')
    op.drop_column('delete__billing', 'transaction_type')
    op.drop_column('delete__billing', 'payment_reference')
    op.drop_column('delete__billing', 'linked_invoice_id')
    op.drop_column('delete__billing', 'invoice_status')
    op.drop_column('delete__billing', 'invoice_reference')
    op.drop_column('delete__billing', 'invoice_due_date')
    op.drop_column('delete__billing', 'debit_note_reference')
    op.drop_column('delete__billing', 'credit_note_reference')
    # ### end Alembic commands ###
