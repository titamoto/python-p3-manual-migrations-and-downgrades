"""Renaming name to nem

Revision ID: 51e82fbcdc6b
Revises: 791279dd0760
Create Date: 2023-08-01 13:29:57.876517

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51e82fbcdc6b'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name='nem')


def downgrade() -> None:
    op.alter_column('students', 'nem', new_column_name='name')
