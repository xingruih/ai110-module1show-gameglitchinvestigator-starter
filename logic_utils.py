"""Game logic utilities for the Glitchy Guesser number guessing game.

Contains core game functions refactored from app.py for testability
and separation of concerns. Docstrings added using Claude Code.
"""

from typing import Optional, Tuple


# FIX: Refactored from app.py and corrected ranges so harder difficulties have wider ranges using Claude Code
def get_range_for_difficulty(difficulty: str) -> Tuple[int, int]:
    """Return the inclusive guessing range for a given difficulty level.

    Harder difficulties have wider ranges, making it more difficult
    to guess the secret number.

    Args:
        difficulty: One of "Easy", "Normal", or "Hard".

    Returns:
        A tuple of (low, high) representing the inclusive range.
        Defaults to (1, 100) for unrecognized difficulty values.

    Examples:
        >>> get_range_for_difficulty("Easy")
        (1, 50)
        >>> get_range_for_difficulty("Hard")
        (1, 200)
    """
    if difficulty == "Easy":
        return 1, 50
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200
    return 1, 100


# FIX: Refactored from app.py into logic_utils.py using Claude Code
def parse_guess(raw: Optional[str]) -> Tuple[bool, Optional[int], Optional[str]]:
    """Parse raw user input into a validated integer guess.

    Handles None, empty strings, decimals (truncated to int), and
    non-numeric input gracefully.

    Args:
        raw: The raw string from the text input widget, or None.

    Returns:
        A tuple of (ok, guess_int, error_message) where:
        - ok: True if parsing succeeded, False otherwise.
        - guess_int: The parsed integer, or None on failure.
        - error_message: A user-facing error string, or None on success.

    Examples:
        >>> parse_guess("42")
        (True, 42, None)
        >>> parse_guess("3.7")
        (True, 3, None)
        >>> parse_guess("abc")
        (False, None, 'That is not a number.')
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except (ValueError, OverflowError):
        return False, None, "That is not a number."

    return True, value, None


# FIX: Refactored from app.py into logic_utils.py and corrected swapped higher/lower hints using Claude Code
def check_guess(guess: int, secret: int) -> Tuple[str, str]:
    """Compare the player's guess to the secret number.

    Returns an outcome label and a user-facing hint message.
    The hint directs the player toward the correct answer.

    Args:
        guess: The player's guessed number.
        secret: The target number to guess.

    Returns:
        A tuple of (outcome, message) where outcome is one of
        "Win", "Too High", or "Too Low", and message is an
        emoji-decorated hint string.

    Examples:
        >>> check_guess(50, 50)
        ('Win', '🎉 Correct!')
        >>> check_guess(75, 50)
        ('Too High', '📉 Go LOWER!')
        >>> check_guess(25, 50)
        ('Too Low', '📈 Go HIGHER!')
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"

    return "Too Low", "📈 Go HIGHER!"


# FEATURE: Hot/Cold indicator added using Claude Code for Challenge 4 Enhanced Game UI
def get_hotcold_label(guess: int, secret: int, range_size: int) -> str:
    """Return a Hot/Cold emoji label based on how close the guess is.

    The thresholds are relative to the range size so the feature
    scales across difficulty levels.

    Args:
        guess: The player's guessed number.
        secret: The target number to guess.
        range_size: The size of the guessing range (high - low).

    Returns:
        An emoji string indicating proximity: "🎯 Exact!",
        "🔥 Boiling!", "♨️ Hot!", "🌡️ Warm", "❄️ Cold",
        or "🧊 Freezing!".

    Examples:
        >>> get_hotcold_label(50, 50, 100)
        '🎯 Exact!'
        >>> get_hotcold_label(99, 50, 100)
        '🧊 Freezing!'
    """
    distance = abs(guess - secret)
    pct = distance / max(range_size, 1)

    if pct == 0:
        return "🎯 Exact!"
    if pct <= 0.05:
        return "🔥 Boiling!"
    if pct <= 0.15:
        return "♨️ Hot!"
    if pct <= 0.30:
        return "🌡️ Warm"
    if pct <= 0.50:
        return "❄️ Cold"
    return "🧊 Freezing!"
