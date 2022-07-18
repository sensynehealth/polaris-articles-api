"""empty message

Revision ID: 8bec8821bb03
Revises: 704b337fe8ee
Create Date: 2018-02-07 14:00:03.363748

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8bec8821bb03'
down_revision = '704b337fe8ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tag', 'deleted')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tag', sa.Column('deleted', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###