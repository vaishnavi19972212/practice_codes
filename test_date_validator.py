import pytest
from test_validate_date_function import \
    validate_date


# Positive scenarios
@pytest.mark.parametrize("data, previous_date, expected_output", [
    ({"DATE": "02/22", "STATEMENT_PERIOD": "2-2023", "DATE_RANGES": {"start_date": "02-01-2023", "end_date": "03-01-2023"}}, None, "2023-02-22"),
    ({"DATE": "01/15", "STATEMENT_PERIOD": "2-2023", "DATE_RANGES": {"start_date": "02-01-2023", "end_date": "03-01-2023"}}, "2023-01-25", "2023-01-15"),
 ])
def test_positive_scenarios(data, previous_date, expected_output):
    result = validate_date(data, previous_date)
    assert result == expected_output


 # Negative scenarios


@pytest.mark.parametrize("data, previous_date", [
    ({"DATE": "02/31", "STATEMENT_PERIOD": "2-2023", "DATE_RANGES": {"start_date": "02-01-2023", "end_date": "03-01-2023"}}, None),
    ({"DATE": "13/25", "STATEMENT_PERIOD": "2-2023", "DATE_RANGES": {"start_date": "02-01-2023", "end_date": "03-01-2023"}}, None),
])

def test_negative_scenarios(data, previous_date):
    with pytest.raises(Exception): validate_date(data, previous_date)

# Edge cases
@pytest.mark.parametrize("data, previous_date", [
    ({"DATE": "15/13", "STATEMENT_PERIOD": "8-2023", "DATE_RANGES": {"start_date": "08-01-2023", "end_date": "09-01-2023"}}, "2022-11-10"),
    ({"DATE": "15/13", "STATEMENT_PERIOD": "8-2023", "DATE_RANGES": {"start_date": "08-01-2023", "end_date": "09-01-2023"}}, "2024-11-10"),
 ])

def test_edge_cases(data, previous_date):
    with pytest.raises(Exception): validate_date(data, previous_date)
