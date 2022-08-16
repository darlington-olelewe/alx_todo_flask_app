"""empty message

Revision ID: 123c1af1d7f4
Revises: db374284d5c6
Create Date: 2022-08-13 10:53:53.815627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '123c1af1d7f4'
down_revision = 'db374284d5c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('list_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'task', 'todolist', ['list_id'], ['id'])

    
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.drop_column('task', 'list_id')
    # ### end Alembic commands ###