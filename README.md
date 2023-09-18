# phase3-code-challenge
# Data Structures and Algorithms

## Stacks

### Question 1: is_balanced

The `is_balanced` function checks if a given expression containing parentheses, curly braces, and square brackets is balanced. An expression is considered balanced if each opening bracket has a corresponding closing bracket in the correct order.

#### Usage

```python
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False


### remove_duplicates
The remove_duplicates function takes a sequence (list or tuple) and returns a new sequence with duplicates removed while maintaining the original order of elements.
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]


### word_frequency
The word_frequency function takes a sentence and returns a dictionary containing the frequency of each word in the sentence. It ignores punctuation and considers words in a case-insensitive manner.

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
