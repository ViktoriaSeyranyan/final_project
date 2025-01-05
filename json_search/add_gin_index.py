from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():

    op.create_index(
        'ix_students_extra_data_gin',  
        'students',  
        ['extra_data'],  
        postgresql_using='gin',  
        postgresql_ops={'extra_data': 'jsonb_ops'}  
    )

def downgrade():
    op.drop_index('ix_students_extra_data_gin', table_name='students')
