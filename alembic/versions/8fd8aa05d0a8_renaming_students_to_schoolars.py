"""Renaming students to schoolars

Revision ID: 8fd8aa05d0a8
Revises: dc1a41b956b9
Create Date: 2024-03-20 17:25:08.536891

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8fd8aa05d0a8'
down_revision: Union[str, None] = 'dc1a41b956b9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
