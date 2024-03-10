from src.app.calculator import add, subtract
import pytest


def test_invalid_add() -> None:
    with pytest.raises(TypeError):
        add(1.1, 1)


@pytest.mark.parametrize(
    "test_input1, test_input2, expected",
    [
        (0, 0, 0),
        (1, 2, 3),
        (-1, -2, -3),
        (1, -2, -1)
    ]
)
def test_add(test_input1, test_input2, expected) -> None:
    assert add(test_input1, test_input2) == expected


@pytest.mark.xfail()
def test_fail():
    assert add(1, 2) == 4


@pytest.mark.skip(reason="String input not yet supported.")
def test_add_string() -> None:
    assert add('1', 2) == 3


def test_invalid_subtract() -> None:
    with pytest.raises(TypeError):
        subtract(1, 1.1)


@pytest.mark.parametrize(
    "test_input1, test_input2, expected",
    [
        (0, 0, 0),
        (1, 2, -1),
        (-1, -2, 1),
        (-1, 2, -3)
    ]
)
def test_subtract(test_input1, test_input2, expected) -> None:
    assert subtract(test_input1, test_input2) == expected


@pytest.mark.skip(reason="String input not yet supported.")
def test_subtract_string() -> None:
    assert add('1', 2) == -1


# @pytest.fixture(scope="session")
# def db_conn():
#     db = ...
#     url = ...
#     with db.connection(url) as conn:
#         yield conn


# def test_db_add(db_conn):
#     db_conn.read_data()
#     assert ...
