"""empty message

Revision ID: 79806ff4bae2
Revises: 
Create Date: 2021-10-18 14:07:11.866543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79806ff4bae2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('author', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('picture', sa.String(length=255), nullable=False),
    sa.Column('category', sa.String(length=255), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.Column('likes', sa.Integer(), nullable=False),
    sa.Column('price', sa.BigInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###
