from main import calculate_average


def test_calculate_average():
    result = calculate_average([70, 80, 90])

    assert result == 90

test_calculate_average()