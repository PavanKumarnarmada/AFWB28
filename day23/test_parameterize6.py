import pytest

#can we run a method automatically before every test method? Yes- using fixture
@pytest.fixture
def precontion():
    print("\nopen the browser and enter url")
    print("login to the app")

def test_create_customer(precontion):
    print("create customer")


def test_create_product(precontion):
    print("create product")