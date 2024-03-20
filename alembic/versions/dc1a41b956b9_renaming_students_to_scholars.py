"""Renaming students to scholars

Revision ID: dc1a41b956b9
Revises: 7142df128486
Create Date: 2024-03-20 17:23:29.641510

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc1a41b956b9'
down_revision: Union[str, None] = '7142df128486'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
