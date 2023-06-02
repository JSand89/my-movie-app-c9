# import pytest
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# # Configuración de la base de datos de prueba
# DATABASE_URL = 'sqlite:///test.db'

# @pytest.fixture(scope='session')
# def db():
#     engine = create_engine(DATABASE_URL)
#     SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
#     # Proporcionar la sesión de la base de datos a las pruebas
#     yield SessionLocal

#     # Realizar la limpieza y cierre de la conexión
#     engine.dispose()
