import cleaner

def test_strip_hidden_characters():
    # Zero-width spaces, joiners, and BOM should be stripped
    text = "Hello\u200b World\ufeff!\u200c"
    assert cleaner.strip_hidden_characters(text) == "Hello World!"
    
    # Standard spacing (tabs, newlines) should be preserved
    text_with_newlines = "Line 1\nLine 2\tTabbed"
    assert cleaner.strip_hidden_characters(text_with_newlines) == text_with_newlines

def test_normalize_typography():
    # Smart quotes, en/em dashes, non-breaking spaces should be normalized
    text = "“Hello” – ‘World’—with\u00a0spaces."
    expected = '"Hello" - \'World\'-with spaces.'
    assert cleaner.normalize_typography(text) == expected

def test_statistical_paraphrase():
    # LLM words like "Furthermore", "utilize", "tapestry" should be rephrased
    text = "Furthermore, we can utilize this library. It is a tapestry of code."
    # Furthermore, -> Also, ; utilize -> use ; tapestry -> complex structure
    # Wait, let's verify casing as well. "Furthermore," -> "Also,"
    result = cleaner.statistical_paraphrase(text)
    assert "Also," in result
    assert "use" in result
    assert "complex structure" in result
    assert "Furthermore" not in result
    assert "utilize" not in result
    assert "tapestry" not in result
    print("All tests passed successfully!")

if __name__ == "__main__":
    test_strip_hidden_characters()
    test_normalize_typography()
    test_statistical_paraphrase()

