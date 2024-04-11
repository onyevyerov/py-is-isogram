from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_is_isogram_function_returns_desire_result(
        word: str,
        result: bool
) -> None:
    assert is_isogram(word) == result
