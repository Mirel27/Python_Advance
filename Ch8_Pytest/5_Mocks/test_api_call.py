from main import api_call

def test_api_call(mocker):
    mock_get = mocker.patch("main.requests.get")

    mock_get.return_value.json.return_value = {
        "main": {"key": "value"}
    }

    url = "https://api.example.com/data"
    result = api_call(url)

    assert result == {
        "data": {"main": {"key": "value"}}
    }