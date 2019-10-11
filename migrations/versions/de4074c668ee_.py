"""empty message

Revision ID: de4074c668ee
Revises: 
Create Date: 2019-10-08 16:57:46.109656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de4074c668ee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('demande_creacompte',
    sa.Column('id_compte', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=120), nullable=True),
    sa.Column('nom', sa.String(length=50), nullable=True),
    sa.Column('prenom', sa.String(length=50), nullable=True),
    sa.Column('mail', sa.String(length=50), nullable=True),
    sa.Column('tel', sa.String(length=20), nullable=True),
    sa.Column('adresse', sa.String(length=140), nullable=True),
    sa.Column('justificatif', sa.String(length=20), nullable=True),
    sa.Column('affect', sa.String(length=50), nullable=True),
    sa.Column('valide', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id_compte')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('password_hash', sa.String(length=150), nullable=True),
    sa.Column('nom', sa.String(length=50), nullable=True),
    sa.Column('prenom', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('type', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('agent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tel', sa.String(length=20), nullable=True),
    sa.Column('debut_contrat', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tel', sa.String(length=20), nullable=True),
    sa.Column('adresse', sa.String(length=140), nullable=True),
    sa.Column('justificatif', sa.String(length=20), nullable=True),
    sa.Column('id_agent', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['id_agent'], ['agent.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comptes',
    sa.Column('id_compte', sa.String(length=50), nullable=False),
    sa.Column('id_client', sa.String(length=50), nullable=True),
    sa.Column('type_compte', sa.Enum('COURANT', 'DECOUVERT', 'INTERET', name='typecompte'), nullable=True),
    sa.Column('rib', sa.String(length=50), nullable=True),
    sa.Column('solde', sa.Float(precision=20), nullable=True),
    sa.Column('date_creation', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['id_client'], ['client.id'], ),
    sa.PrimaryKeyConstraint('id_compte')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comptes')
    op.drop_table('client')
    op.drop_table('agent')
    op.drop_table('admin')
    op.drop_table('user')
    op.drop_table('demande_creacompte')
    # ### end Alembic commands ###