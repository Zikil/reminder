"""empty message

Revision ID: 100d8dcb798f
Revises: 5c3ba0549b40
Create Date: 2020-08-08 16:48:46.062754

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '100d8dcb798f'
down_revision = '5c3ba0549b40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
