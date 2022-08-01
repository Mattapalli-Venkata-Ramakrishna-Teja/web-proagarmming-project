"""addstock table

Revision ID: 03084704847d
Revises: 
Create Date: 2022-08-01 08:43:59.227773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03084704847d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('addbuyer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=140), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_addbuyer_amount'), 'addbuyer', ['amount'], unique=False)
    op.create_index(op.f('ix_addbuyer_status'), 'addbuyer', ['status'], unique=False)
    op.create_table('addstock',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tabname', sa.String(length=64), nullable=True),
    sa.Column('company', sa.String(length=120), nullable=True),
    sa.Column('doe', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_addstock_company'), 'addstock', ['company'], unique=True)
    op.create_index(op.f('ix_addstock_tabname'), 'addstock', ['tabname'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_addstock_tabname'), table_name='addstock')
    op.drop_index(op.f('ix_addstock_company'), table_name='addstock')
    op.drop_table('addstock')
    op.drop_index(op.f('ix_addbuyer_status'), table_name='addbuyer')
    op.drop_index(op.f('ix_addbuyer_amount'), table_name='addbuyer')
    op.drop_table('addbuyer')
    # ### end Alembic commands ###
