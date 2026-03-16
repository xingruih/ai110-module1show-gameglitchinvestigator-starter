from logic_utils import check_guess, get_range_for_difficulty


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


def test_difficulty_ranges_scale_with_difficulty():
    """Harder difficulties should have wider ranges."""
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert easy_high < normal_high < hard_high


def test_easy_range_is_not_trivial():
    """Easy range should be reasonable, not just 1-20."""
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high >= 50
