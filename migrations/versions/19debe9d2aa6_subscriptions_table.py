"""subscriptions table

Revision ID: 19debe9d2aa6
Revises: 
Create Date: 2020-07-27 21:34:50.256197

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19debe9d2aa6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscription',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('cost', sa.Float(), nullable=True),
    sa.Column('currency', sa.String(length=32), nullable=True),
    sa.Column('billing_date', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subscription_name'), 'subscription', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_subscription_name'), table_name='subscription')
    op.drop_table('subscription')
    # ### end Alembic commands ###
