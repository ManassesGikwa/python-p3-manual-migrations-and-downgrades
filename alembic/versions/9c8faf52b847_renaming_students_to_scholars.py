"""Renaming students to scholars

Revision ID: 9c8faf52b847
Revises: 8fd8aa05d0a8
Create Date: 2024-03-20 17:26:14.462774

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9c8faf52b847'
down_revision: Union[str, None] = '8fd8aa05d0a8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
