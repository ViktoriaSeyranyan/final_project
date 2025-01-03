from alembic import op
import sqlalchemy as sa

def upgrade():
       op.create_index('ix_students_email', 'students', ['email'])

def downgrade():
    
    op.drop_index('ix_students_email', 'students')
