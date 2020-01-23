"""create git_info table

Revision ID: 1897c14ee3b5
Revises: 
Create Date: 2020-01-21 22:29:08.800007

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1897c14ee3b5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'git_info',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('full_name', sa.String(500)),
        sa.Column('html_url', sa.String(500)),
        sa.Column('description', sa.Text),
        sa.Column('stargazers_count', sa.Integer),
        sa.Column('language', sa.String(50)),
    )


def downgrade():
    op.drop_table('git_info')

