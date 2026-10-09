from unittest.mock import Mock, patch

from src.generator import generate_mission


def test_generate_mission_with_ollama():
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        "response": (
            "1. Walk slowly along a public path.\n"
            "2. Find three trees with different shapes.\n"
            "3. Notice their leaves, bark, and surroundings.\n"
            "4. Choose one detail you usually overlook.\n"
            "Now put your phone away."
        )
    }

    with patch(
        "src.generator.requests.post",
        return_value=mock_response,
    ):
        result = generate_mission(
            duration=15,
            environment="Urban park",
            interest="Trees",
            energy="Low",
            provider="ollama",
        )

    assert result
    assert "Now put your phone away." in result


def test_generate_mission_with_openrouter():
    mock_client = Mock()

    mock_response = Mock()
    mock_response.choices = [
        Mock(
            message=Mock(
                content=(
                    "1. Walk slowly along a public path.\n"
                    "2. Find three trees with different shapes.\n"
                    "3. Listen for natural sounds around you.\n"
                    "4. Notice one detail you usually miss.\n"
                    "Now put your phone away."
                )
            )
        )
    ]

    mock_client.chat.completions.create.return_value = mock_response

    with patch(
        "src.generator.OpenAI",
        return_value=mock_client,
    ):
        with patch.dict(
            "os.environ",
            {
                "OPENROUTER_API_KEY": "test-key",
                "OPENROUTER_MODEL": "openai/gpt-oss-20b",
            },
        ):
            result = generate_mission(
                duration=15,
                environment="Urban park",
                interest="Trees",
                energy="Low",
                provider="openrouter",
            )

    assert result
    assert "Now put your phone away." in result