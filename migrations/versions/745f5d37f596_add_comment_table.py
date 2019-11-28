"""add comment table

Revision ID: 745f5d37f596
Revises: 
Create Date: 2019-11-26 22:47:25.868444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '745f5d37f596'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=500), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('pass_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey')
    )
    op.drop_table('Comments')
    # ### end Alembic commands ###