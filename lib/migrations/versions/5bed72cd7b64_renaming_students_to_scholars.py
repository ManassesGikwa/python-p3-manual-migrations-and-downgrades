"""Renaming students to scholars

Revision ID: 5bed72cd7b64
Revises: 791279dd0760
Create Date: 2024-03-25 18:09:12.704298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5bed72cd7b64'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')

def downgrade() -> None:
    op.rename_table('scholars', 'students')
