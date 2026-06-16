# Code Wiki - AI Text Cleaner (Clean Paste clone)

## Project Goals
Build a premium, modern text cleaning desktop application using Python that:
1. Sanitizes raw text: Removes zero-width characters, format control characters, and hidden Unicode markings.
2. Normalizes typography: Converts smart quotes, non-standard dashes, and non-breaking spaces into standard equivalents.
3. Advanced Paraphrasing/Rewriting: Performs lexical/stylistic adjustments to strip statistical patterns or humanize text.
4. Premium Desktop Interface: A beautiful, modern dark-themed GUI (using CustomTkinter) with real-time cleaning feedback, clipboard copying/pasting, and customizable toggles.

## Tech Stack
- **Languages**: Python 3
- **GUI Library**: `customtkinter` (for modern dark mode UI) or `tkinter` fallback
- **Dependencies**: `customtkinter`, `pyperclip` (for reliable clipboard actions)

## Project Version
- Current Version: `0.1.0`

## File Structure & Functions
- **[cleaner.py](file:///c:/Users/karee/OneDrive/Desktop/random%20projects/ai%20text%20cleaner/cleaner.py)**: Text cleaning engine.
  - `strip_hidden_characters(text: str) -> str`: Removes zero-width characters, format controls, and hidden markings.
  - `normalize_typography(text: str) -> str`: Standardizes smart quotes, non-standard dashes, and non-breaking spaces.
  - `statistical_paraphrase(text: str) -> str`: Replaces typical high-probability LLM transition patterns and overused verbs.
- **[gui.py](file:///c:/Users/karee/OneDrive/Desktop/random%20projects/ai%20text%20cleaner/gui.py)**: CustomTkinter application layout and events.
  - `CleanPasteApp` (class): The main GUI window.
    - `__init__()`: Initializes state variable tracking and frame layout.
    - `_create_widgets()`: Instantiates the UI structure (header, textboxes, switches, and action buttons).
    - `_on_input_changed(event)`: Listens for modifications in the input text area and automatically updates results in real-time.
    - `trigger_cleaning()`: Directs data through selected cleaners, updates the view, and compiles stats.
    - `update_stats(...)`: Renders character and word changes in the UI.
    - `paste_from_clipboard()`: Pastes OS clipboard text directly and triggers sanitization.
    - `copy_to_clipboard()`: Copies sanitized output back to system clipboard with visual success notification.
    - `clear_all()`: Resets all inputs, outputs, and statistics trackers.
- **[main.py](file:///c:/Users/karee/OneDrive/Desktop/random%20projects/ai%20text%20cleaner/main.py)**: App launcher.
  - `main()`: Initializes and starts the desktop main loops.
- **[test_cleaner.py](file:///c:/Users/karee/OneDrive/Desktop/random%20projects/ai%20text%20cleaner/test_cleaner.py)**: Test suite.
  - Test functions for cleaning routines.

## Database Schema
No database is involved in this project. All operations are in-memory and stateless.

## Methodologies
- Clean Code principles
- Desktop GUI design patterns
- Stateless Text Processing

## Project Timeline
- **Start Date**: 2026-06-16
- **Latest Update**: 2026-06-16
