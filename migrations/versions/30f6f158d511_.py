"""empty message

Revision ID: 30f6f158d511
Revises: b3e012808b04
Create Date: 2024-12-23 20:31:51.926234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30f6f158d511'
down_revision = 'b3e012808b04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('card', schema=None) as batch_op:
        batch_op.add_column(sa.Column('board_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'board', ['board_id'], ['board_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('card', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('board_id')

    # ### end Alembic commands ###
