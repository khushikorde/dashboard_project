def word_frequency(text):
  """Counts the frequency of words in a given text and stores the results in a dictionary.

  Args:
    text: The text to analyze.

  Returns:
    A dictionary where keys are words and values are their corresponding frequencies.
  """

  words = text.split()
  word_count = {}
  for word in words:
    word_count[word] = word_count.get(word, 0) + 1
  return word_count

# Example usage:
text = "This is a sample text. This text has some repeated words."
frequency_dict = word_frequency(text)
print(frequency_dict)