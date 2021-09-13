"""initial_schema

Revision ID: b04f457dac77
Revises: 
Create Date: 2021-09-13 22:46:45.863217

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import DATE, TIMESTAMP, UUID

# revision identifiers, used by Alembic.
revision = 'b04f457dac77'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'branch',
        sa.Column('b_id', UUID),
        sa.Column('b_short_name', sa.String(10), nullable=False),
        sa.Column('b_name', sa.String(100), nullable=False),
        sa.Column('b_created_at', TIMESTAMP, nullable=False),
        sa.Column('b_updated_at', TIMESTAMP)
    )

    op.create_primary_key('branch_pk', 'branch', ['b_id'])
    op.create_index('branch_short_name_unique_key', 'branch', ['b_short_name'], unique=True)

    op.create_table(
        'student',
        sa.Column('s_id', UUID),
        sa.Column('s_name', sa.String(100), nullable=False),
        sa.Column('s_branch', UUID, nullable=False),
        sa.Column('s_year', sa.Integer, nullable=False),
        sa.Column('s_dob', DATE, nullable=False),
        sa.Column('s_email', sa.String(100), nullable=False),
        sa.Column('s_phone', sa.String(20), nullable=False),
        sa.Column('s_created_at', TIMESTAMP, nullable=False),
        sa.Column('s_updated_at', TIMESTAMP)
    )

    op.create_primary_key('student_pk', 'student', ['s_id'])
    op.create_check_constraint('student_year_check', 'student', 's_year IN (1, 2, 3, 4)')
    op.create_foreign_key(
        'student_branch_fk',
        'student',
        'branch',
        ['s_branch'],
        ['b_id'],
        onupdate='CASCADE',
        ondelete='CASCADE'
    )
    op.create_index('ix__student__branch__year', 'student', ['s_branch', 's_year'])


def downgrade():
    op.drop_table('student')
    op.drop_table('branch')
