from alembic import op
import sqlalchemy as sa

def upgrade():
      
  op.add_column('students', sa.Column('email', sa.String(), nullable=True))
    op.add_column('students', sa.Column('phone_number', sa.String(), nullable=True))

def downgrade():
    op.drop_column('students', 'phone_number')
    op.drop_column('students', 'email')
