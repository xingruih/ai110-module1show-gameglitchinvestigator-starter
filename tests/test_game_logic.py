from logic_utils import check_guess


def test_too_high_hint_says_lower():
    """When the guess is higher than the secret, the hint should say 'Go LOWER!'."""
    outcome, message = check_guess(75, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_too_low_hint_says_higher():
    """When the guess is lower than the secret, the hint should say 'Go HIGHER!'."""
    outcome, message = check_guess(25, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
