import pytest
from main import Hello

def test_hello_world():
    assert Hello.hello_world() == "Hello world"

if __name__ == '__main__':
    pytest.main()
