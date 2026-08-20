"""Day 07 — Hangman game logic and Streamlit view."""

from dataclasses import dataclass, field
import secrets

import streamlit as st


MAX_LIVES = 6
WORDS = (
    "python",
    "function",
    "variable",
    "dictionary",
    "algorithm",
    "terminal",
    "developer",
    "iteration",
    "computer",
    "streamlit",
)

HANGMAN_STAGES = (
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
)


@dataclass
class HangmanGame:
    """Store and update one Hangman match."""

    word: str
    guessed_letters: set[str] = field(default_factory=set)
    remaining_lives: int = MAX_LIVES

    @property
    def display_word(self) -> str:
        """Return the word with unguessed characters replaced by underscores."""
        return " ".join(
            letter.upper() if letter in self.guessed_letters else "_"
            for letter in self.word
        )

    @property
    def wrong_letters(self) -> list[str]:
        """Return incorrect guesses in alphabetical order."""
        return sorted(self.guessed_letters.difference(self.word))

    @property
    def status(self) -> str:
        """Return playing, won, or lost for the current match."""
        if all(letter in self.guessed_letters for letter in self.word):
            return "won"
        if self.remaining_lives == 0:
            return "lost"
        return "playing"

    def guess(self, raw_letter: str) -> str:
        """Apply a guess and return a result that the interface can display."""
        letter = raw_letter.strip().lower()
        if len(letter) != 1 or letter not in "abcdefghijklmnopqrstuvwxyz":
            return "invalid"
        if self.status != "playing":
            return "game_over"
        if letter in self.guessed_letters:
            return "already_guessed"

        self.guessed_letters.add(letter)
        if letter in self.word:
            return "correct"

        self.remaining_lives -= 1
        return "incorrect"


def new_game(word: str | None = None) -> HangmanGame:
    """Create a match using a provided word or a random word from the list."""
    selected_word = word or secrets.choice(WORDS)
    return HangmanGame(word=selected_word.lower())


def render_hangman() -> None:
    """Render an interactive Hangman match."""
    if "hangman_game" not in st.session_state:
        st.session_state.hangman_game = new_game()

    game: HangmanGame = st.session_state.hangman_game

    title_column, action_column = st.columns([4, 1])
    with title_column:
        st.markdown('<p class="eyebrow">Day 07 · Game</p>', unsafe_allow_html=True)
        st.title("🎯 Hangman")
        st.write("Guess the hidden programming word before the drawing is complete.")
    with action_column:
        st.write("")
        st.write("")
        if st.button("New game", use_container_width=True):
            st.session_state.hangman_game = new_game()
            st.session_state.pop("hangman_message", None)
            st.rerun()

    drawing_column, game_column = st.columns([1, 2], gap="large")

    with drawing_column:
        wrong_count = MAX_LIVES - game.remaining_lives
        st.code(HANGMAN_STAGES[wrong_count], language=None)
        st.metric("Lives remaining", f"{game.remaining_lives} / {MAX_LIVES}")
        st.progress(game.remaining_lives / MAX_LIVES)

    with game_column:
        st.markdown(
            f'<div class="word-display">{game.display_word}</div>',
            unsafe_allow_html=True,
        )
        st.write("")

        if game.wrong_letters:
            st.caption("Incorrect guesses: " + ", ".join(game.wrong_letters).upper())
        else:
            st.caption("Incorrect guesses will appear here.")

        if game.status == "playing":
            with st.form("hangman_guess", clear_on_submit=True):
                letter = st.text_input(
                    "Enter one letter",
                    max_chars=1,
                    placeholder="e.g. A",
                )
                submitted = st.form_submit_button(
                    "Submit guess", type="primary", use_container_width=True
                )

            if submitted:
                result = game.guess(letter)
                messages = {
                    "correct": ("success", "Great guess! That letter is in the word."),
                    "incorrect": ("error", "Not this time—you lost one life."),
                    "already_guessed": ("warning", "You already tried that letter."),
                    "invalid": ("warning", "Enter one letter from A to Z."),
                }
                st.session_state.hangman_message = messages.get(result)
                st.rerun()

            message = st.session_state.get("hangman_message")
            if message:
                getattr(st, message[0])(message[1])
        elif game.status == "won":
            st.success(f"You won! The word was {game.word.upper()}.")
            st.balloons()
        else:
            st.error(f"Game over. The word was {game.word.upper()}.")
