from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    # Добавляем индекс GIN на поле JSON
    op.create_index(
        'ix_students_extra_data_gin',  # Имя индекса
        'students',  # Таблица
        ['extra_data'],  # Поле JSON
        postgresql_using='gin',  # Тип индекса
        postgresql_ops={'extra_data': 'jsonb_ops'}  # Используем GIN для jsonb
    )

def downgrade():
    op.drop_index('ix_students_extra_data_gin', table_name='students')
