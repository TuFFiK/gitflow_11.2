def capitalize_words(sentence):
    """Capitalize the first letter of each word in a sentence."""
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

def capitalize_first_letters(sentence):
    """Capitalize the first letter of each word in a sentence.

    Returns:
        str: The sentence with the first letter of each word capitalized.
    """
    return ' '.join([word.capitalize() for word in sentence.split()])
