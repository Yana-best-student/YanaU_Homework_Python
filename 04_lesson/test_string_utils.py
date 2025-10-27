import pytest
from string_utils import StringUtils


string_utils = StringUtils()

# Делает первую букву заглавной и возвращает этот же текст


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("yana", "Yana"),
    ("hello galaxy", "Hello galaxy"),
    ("яна", "Яна"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# Принимает на вход текст и удаляет пробелы в начале, если они есть


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" Yana", "Yana"),
    ("      123abc", "123abc"),
    ("  Яна", "Яна"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("Yana Uspenskaya", "Yana Uspenskaya"),
    ("123abc ", "123abc "),
    ("None", "None"),
    ("", "")

])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

# Возвращает искомый символ


@pytest.mark.positive
@pytest.mark.parametrize("input_str, simbol_str, expected", [
    ("Yana", "Y", True),
    ("November 05", "5", True),
    ("012345", "9", False),
    ("", "", True)
])
def test_contains_positive(input_str, simbol_str, expected):
    assert string_utils.contains(input_str, simbol_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, simbol_str, expected", [
    ("", "Y", False),
    (" ", "z", False),
    ("012345", "9", False),
])
def test_contains_negative(input_str, simbol_str, expected):
    assert string_utils.contains(input_str, simbol_str) == expected

# Удаляет все подстроки из переданной строки


@pytest.mark.positive
@pytest.mark.parametrize("input_str, simbol_str, expected", [
    ("Yana", "Y", "ana"),
    ("November 05", " 05", "November"),
    ("Yana.", ".", "Yana"),

])
def test_delete_symbol_positive(input_str, simbol_str, expected):
    assert string_utils.delete_symbol(input_str, simbol_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, simbol_str, expected", [
    ("012345", "23", "0145"),
    ("🍇🍑🍌", "🍌", "🍇🍑"),
    ("@#$%^&", "#$", "@%^&"),
])
def test_delete_symbol_negative(input_str, simbol_str, expected):
    assert string_utils.delete_symbol(input_str, simbol_str) == expected
