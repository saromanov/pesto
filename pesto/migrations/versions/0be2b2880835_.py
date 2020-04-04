"""empty message

Revision ID: 0be2b2880835
Revises: 
Create Date: 2020-04-03 21:03:43.657436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0be2b2880835'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sources', sa.Column('title', sa.String(), nullable=True))
    op.add_column('sources', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'sources', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'sources', type_='foreignkey')
    op.drop_column('sources', 'user_id')
    op.drop_column('sources', 'title')
    # ### end Alembic commands ###