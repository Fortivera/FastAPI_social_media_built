from fastapi.testclient import TestClient
from app.main import app
import pytest
from app import schemas
from app.config import settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from app.database import get_db, Base

# initializing our database parameters
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test"
# engine is the lowest level object used by SQLAlchemy. It maintains a pool of connections available for use whenever the application needs to talk to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# Session is an interface for SELECT and other queries
TestingSessionlocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


# pytest fixtures predefine what should be expected after the function call
@pytest.fixture
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionlocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client(session):
    def override_get_db():

    try:
        yield session
    finally:
        session.close()
    app.dependency_overrides[get_db] = override_get_db  # as per FastaAPI docs
    yield TestClient(app)


def test_root(client):
    response = client.get('/')
    print(response.json().get("status"))
    assert response.json().get("status") == 'mainkek.py'
    assert response.status_code == 200


def test_create_user(client):
    response = client.post(
        '/users/', json={'email': '1wpba9pp@gmail.com', 'password': 'asdf'})

    new_user = schemas.ShowUser(**response.json())
    assert new_user.email == '1wpba9pp@gmail.com'
    assert response.status_code == 201


# you can also perform the test this way, without schemas and pydantic
# def test_create_user():
#     response = client.post(
#         '/users/', json={'email': 'pp9pp@gmail.com', 'password': 'asdf'})

#     print(response.json())
#     assert response.json().get('email') == 'pp9pp@gmail.com'
#     assert response.status_code == 201
