# Clean Paste

**Clean Paste** is a simple text cleaner designed to remove hidden characters copied from AI agents that are detected by AI detection software. It is built entirely in Python using **CustomTkinter** as a premium, modern desktop utility. It sanitizes raw text in real-time, removing tracking artifacts, zero-width characters, normalizing non-standard typography (like smart quotes), and rephrasing typical AI-generated text patterns.

---

## Features

1. **Strip Invisible Characters:** Safely detects and destroys zero-width spaces (`U+200B`), zero-width joiners (`U+200C`/`U+200D`), and byte-order marks (`U+FEFF`) without breaking standard spaces, newlines, or tabs.
2. **Normalize Quotes & Dashes:** Converts smart quotes (`“”`, `‘’`), em/en dashes (`—`, `–`), and non-breaking spaces (`\u00a0`) into standard ASCII counterparts.
3. **Strip AI Watermarks (Statistical Paraphraser):** Detects and adjusts high-probability LLM transitions and filler words (e.g. "Furthermore,", "Moreover,", "utilize", "tapestry of") to humanize and simplify writing patterns.
4. **Premium Dark Mode GUI:** A beautiful interface featuring real-time input analysis, character difference calculators, and one-click clipboard integrations ("Paste & Clean" and "Copy to Clipboard").

---

## Installation

### Prerequisites

Make sure you have **Python 3.8 or higher** installed.

### Step 1: Clone the repository

```bash
git clone https://github.com/kareemaiman/clean-paste.git
cd clean-paste
```

### Step 2: Install dependencies

Install the required GUI and clipboard libraries:

```bash
pip install customtkinter pyperclip
```

---

## Usage

Start the application by running:

```bash
python main.py
```

### Tips for use:
- Paste text directly into the left panel (or click **Paste & Clean** to load directly from your clipboard).
- Cleaned text updates in real-time as you switch options or type.
- Click **Copy to Clipboard** (or the copy button in the footer) to save the sanitized output.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

