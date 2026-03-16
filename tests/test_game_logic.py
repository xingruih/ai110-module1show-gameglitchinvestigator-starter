from logic_utils import check_guess, get_range_for_difficulty, parse_guess


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


# --- Edge Case Tests (Challenge 1) ---


def test_negative_number_parsed_and_compared():
    """A negative number like -5 should parse successfully and be 'Too Low'."""
    ok, value, err = parse_guess("-5")
    assert ok is True
    assert value == -5
    assert err is None
    outcome, message = check_guess(value, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_decimal_input_truncated_to_int():
    """A decimal like '3.7' should be truncated to 3 and compared correctly."""
    ok, value, err = parse_guess("3.7")
    assert ok is True
    assert value == 3
    assert err is None
    outcome, message = check_guess(value, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_extremely_large_number():
    """An extremely large guess should parse and return 'Too High'."""
    ok, value, err = parse_guess("999999999")
    assert ok is True
    assert value == 999999999
    assert err is None
    outcome, message = check_guess(value, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
