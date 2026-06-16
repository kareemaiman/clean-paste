import tkinter as tk
import customtkinter as ctk
import pyperclip
import cleaner

# Set themes
ctk.set_appearance_mode("Dark")
# We can use blue or green or dark-blue
ctk.set_default_color_theme("blue")

class CleanPasteApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Clean Paste - Advanced Text Sanitizer")
        self.geometry("900x700")
        self.minsize(800, 600)

        # Config variables
        self.strip_invisible_var = ctk.BooleanVar(value=True)
        self.normalize_typo_var = ctk.BooleanVar(value=True)
        self.strip_statistical_var = ctk.BooleanVar(value=False)

        self._create_widgets()

    def _create_widgets(self):
        # Configure grid layout
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # --- Header Panel ---
        self.header_frame = ctk.CTkFrame(self, height=60, corner_radius=0)
        self.header_frame.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.header_frame.grid_propagate(False)
        
        self.title_label = ctk.CTkLabel(
            self.header_frame, 
            text="✨ CLEAN PASTE", 
            font=ctk.CTkFont(family="Helvetica", size=22, weight="bold")
        )
        self.title_label.pack(side="left", padx=20, pady=10)
        
        self.subtitle_label = ctk.CTkLabel(
            self.header_frame, 
            text="Stripping invisible trackers, smart-quotes, and AI watermarks", 
            font=ctk.CTkFont(family="Helvetica", size=12, slant="italic")
        )
        self.subtitle_label.pack(side="left", padx=10, pady=15)

        # --- Main Layout Body ---
        self.body_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.body_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=15)
        
        # Two equal columns for Input and Output, and a center control panel
        self.body_frame.grid_columnconfigure(0, weight=1)
        self.body_frame.grid_columnconfigure(2, weight=1)
        self.body_frame.grid_rowconfigure(0, weight=1)

        # --- Left Panel: Input ---
        self.input_frame = ctk.CTkFrame(self.body_frame)
        self.input_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.input_frame.grid_rowconfigure(1, weight=1)
        self.input_frame.grid_columnconfigure(0, weight=1)

        self.input_label = ctk.CTkLabel(
            self.input_frame, 
            text="Raw Text (Paste Here)", 
            font=ctk.CTkFont(weight="bold")
        )
        self.input_label.grid(row=0, column=0, sticky="w", padx=15, pady=(10, 5))

        self.input_text = ctk.CTkTextbox(self.input_frame, activate_scrollbars=True, wrap="word")
        self.input_text.grid(row=1, column=0, sticky="nsew", padx=15, pady=(0, 15))
        self.input_text.bind("<<Modified>>", self._on_input_changed)

        # --- Middle Controls & Options Panel ---
        self.controls_frame = ctk.CTkFrame(self.body_frame, width=220)
        self.controls_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=5)
        self.controls_frame.grid_columnconfigure(0, weight=1)
        
        self.options_label = ctk.CTkLabel(
            self.controls_frame, 
            text="Cleaning Options", 
            font=ctk.CTkFont(weight="bold", size=14)
        )
        self.options_label.grid(row=0, column=0, padx=15, pady=(15, 10))

        # Checkboxes/Toggles
        self.cb_invisible = ctk.CTkSwitch(
            self.controls_frame, 
            text="Strip Invisible Chars", 
            variable=self.strip_invisible_var,
            command=self.trigger_cleaning
        )
        self.cb_invisible.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        self.cb_typography = ctk.CTkSwitch(
            self.controls_frame, 
            text="Normalize Quotes & Dashes", 
            variable=self.normalize_typo_var,
            command=self.trigger_cleaning
        )
        self.cb_typography.grid(row=2, column=0, padx=20, pady=10, sticky="w")

        self.cb_statistical = ctk.CTkSwitch(
            self.controls_frame, 
            text="Strip AI Watermarks", 
            variable=self.strip_statistical_var,
            command=self.trigger_cleaning
        )
        self.cb_statistical.grid(row=3, column=0, padx=20, pady=10, sticky="w")

        # Action Buttons
        self.clean_btn = ctk.CTkButton(
            self.controls_frame, 
            text="Run Sanitizer", 
            command=self.trigger_cleaning,
            font=ctk.CTkFont(weight="bold")
        )
        self.clean_btn.grid(row=4, column=0, padx=20, pady=(25, 10), sticky="ew")

        self.paste_clean_btn = ctk.CTkButton(
            self.controls_frame, 
            text="Paste & Clean", 
            fg_color="#2c3e50",
            hover_color="#34495e",
            command=self.paste_from_clipboard
        )
        self.paste_clean_btn.grid(row=5, column=0, padx=20, pady=5, sticky="ew")

        self.clear_btn = ctk.CTkButton(
            self.controls_frame, 
            text="Clear All", 
            fg_color="#c0392b",
            hover_color="#e74c3c",
            command=self.clear_all
        )
        self.clear_btn.grid(row=6, column=0, padx=20, pady=5, sticky="ew")

        # Statistics / Info Panel
        self.stats_frame = ctk.CTkFrame(self.controls_frame, fg_color="transparent")
        self.stats_frame.grid(row=7, column=0, padx=20, pady=(30, 15), sticky="ew")
        self.stats_frame.grid_columnconfigure(0, weight=1)

        self.stats_title = ctk.CTkLabel(
            self.stats_frame, 
            text="Statistics", 
            font=ctk.CTkFont(weight="bold", size=12)
        )
        self.stats_title.grid(row=0, column=0, sticky="w", pady=(0, 5))

        self.chars_label = ctk.CTkLabel(self.stats_frame, text="Characters: 0 -> 0", anchor="w")
        self.chars_label.grid(row=1, column=0, sticky="w")

        self.words_label = ctk.CTkLabel(self.stats_frame, text="Words: 0 -> 0", anchor="w")
        self.words_label.grid(row=2, column=0, sticky="w")

        self.stripped_label = ctk.CTkLabel(self.stats_frame, text="Stripped Count: 0", anchor="w")
        self.stripped_label.grid(row=3, column=0, sticky="w")

        # --- Right Panel: Output ---
        self.output_frame = ctk.CTkFrame(self.body_frame)
        self.output_frame.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)
        self.output_frame.grid_rowconfigure(1, weight=1)
        self.output_frame.grid_columnconfigure(0, weight=1)

        self.output_label = ctk.CTkLabel(
            self.output_frame, 
            text="Cleaned Output", 
            font=ctk.CTkFont(weight="bold")
        )
        self.output_label.grid(row=0, column=0, sticky="w", padx=15, pady=(10, 5))

        self.output_text = ctk.CTkTextbox(self.output_frame, activate_scrollbars=True, wrap="word")
        self.output_text.grid(row=1, column=0, sticky="nsew", padx=15, pady=(0, 15))
        # Keep output text read-only except when updating
        self.output_text.configure(state="disabled")

        # --- Footer Status Bar ---
        self.footer_frame = ctk.CTkFrame(self, height=35, corner_radius=0)
        self.footer_frame.grid(row=2, column=0, sticky="nsew", padx=0, pady=0)
        
        self.status_label = ctk.CTkLabel(
            self.footer_frame, 
            text="Ready to clean.", 
            font=ctk.CTkFont(size=11)
        )
        self.status_label.pack(side="left", padx=20, pady=5)

        self.copy_btn = ctk.CTkButton(
            self.footer_frame, 
            text="📋 Copy to Clipboard", 
            width=150, 
            height=25,
            command=self.copy_to_clipboard,
            font=ctk.CTkFont(size=11, weight="bold")
        )
        self.copy_btn.pack(side="right", padx=20, pady=5)

    def _on_input_changed(self, event):
        # Reset the modified flag so we get future events
        self.input_text.edit_modified(False)
        # Automatically trigger cleaning on text entry/change for real-time responsiveness
        self.trigger_cleaning()

    def trigger_cleaning(self):
        raw_text = self.input_text.get("1.0", "end-1c")
        if not raw_text:
            self.output_text.configure(state="normal")
            self.output_text.delete("1.0", "end")
            self.output_text.configure(state="disabled")
            self.update_stats(0, 0, 0, 0, 0)
            return

        cleaned_text = raw_text

        # 1. Strip Invisible Characters
        if self.strip_invisible_var.get():
            cleaned_text = cleaner.strip_hidden_characters(cleaned_text)

        # 2. Normalize Typography
        if self.normalize_typo_var.get():
            cleaned_text = cleaner.normalize_typography(cleaned_text)

        # 3. Strip Statistical Watermarks
        if self.strip_statistical_var.get():
            cleaned_text = cleaner.statistical_paraphrase(cleaned_text)

        # Update output
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", cleaned_text)
        self.output_text.configure(state="disabled")

        # Stats calculation
        orig_chars = len(raw_text)
        orig_words = len(raw_text.split()) if raw_text.strip() else 0
        clean_chars = len(cleaned_text)
        clean_words = len(cleaned_text.split()) if cleaned_text.strip() else 0
        
        # Approximating stripped items
        stripped = orig_chars - clean_chars

        self.update_stats(orig_chars, clean_chars, orig_words, clean_words, stripped)
        self.status_label.configure(text="Text successfully cleaned and sanitized!")

    def update_stats(self, orig_c, clean_c, orig_w, clean_w, stripped):
        self.chars_label.configure(text=f"Characters: {orig_c} -> {clean_c}")
        self.words_label.configure(text=f"Words: {orig_w} -> {clean_w}")
        self.stripped_label.configure(text=f"Stripped Count: {max(0, stripped)}")

    def paste_from_clipboard(self):
        try:
            clipboard_text = pyperclip.paste()
            if clipboard_text:
                self.input_text.delete("1.0", "end")
                self.input_text.insert("1.0", clipboard_text)
                self.trigger_cleaning()
                self.status_label.configure(text="Clipboard content pasted & cleaned.")
            else:
                self.status_label.configure(text="Clipboard is empty.")
        except Exception as e:
            self.status_label.configure(text=f"Error pasting clipboard: {str(e)}")

    def copy_to_clipboard(self):
        cleaned_text = self.output_text.get("1.0", "end-1c")
        if cleaned_text:
            try:
                pyperclip.copy(cleaned_text)
                self.status_label.configure(text="Cleaned text copied to clipboard! ✅")
                # Visual button feedback
                self.copy_btn.configure(text="Copied! ✅", fg_color="#27ae60")
                self.after(2000, self.reset_copy_btn)
            except Exception as e:
                self.status_label.configure(text=f"Error copying: {str(e)}")
        else:
            self.status_label.configure(text="Nothing to copy.")

    def reset_copy_btn(self):
        self.copy_btn.configure(text="📋 Copy to Clipboard", fg_color=["#3b8ed0", "#1f538d"])

    def clear_all(self):
        self.input_text.delete("1.0", "end")
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.configure(state="disabled")
        self.update_stats(0, 0, 0, 0, 0)
        self.status_label.configure(text="Cleared.")
