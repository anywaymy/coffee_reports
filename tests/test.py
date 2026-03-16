import pytest

from reports import calculate_median_coffee


@pytest.fixture
def sample_csv_path(tmp_path):
    file = tmp_path / "my_test_data.csv"
    csv_content = (
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Ivan,2024-06-01,100,8,2,ok,Math\n"
        "Ivan,2024-06-02,200,8,2,ok,Math\n"
        "Ivan,2024-06-03,300,8,2,ok,Math\n"
        "Maria,2024-06-01,50,8,2,ok,Math\n"
        "Maria,2024-06-02,150,8,2,ok,Math\n"
    )

    file.write_text(csv_content, encoding='utf-8')
    return str(file)


def test_median(sample_csv_path):
    result = calculate_median_coffee([sample_csv_path])

    assert result[0] == ["Ivan", 200.0]
    assert result[1] == ["Maria", 100.0]
    assert result[0][1] > result[1][1]
