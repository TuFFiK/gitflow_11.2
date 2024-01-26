def capitalize_words(sentence):
    """
    Capitalize the first letter of each word in a sentence.

    Args:
        sentence (str): The input sentence.

    Returns:
    - str: The sentence with the first letter of each word capitalized.
    """
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
