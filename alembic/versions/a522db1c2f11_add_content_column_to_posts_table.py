"""add content column to posts table

Revision ID: a522db1c2f11
Revises: 3f550509e6f5
Create Date: 2021-11-30 21:21:23.696235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a522db1c2f11'
down_revision = '3f550509e6f5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
