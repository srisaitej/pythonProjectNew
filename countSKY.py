def count_letters(string):
    # Initialize counters for each letter
    count_S = 0
    count_K = 0
    count_Y = 0

    # Iterate over each character in the string
    for char in string:
        # Check if the character is 'S', 'K', or 'Y', and update the corresponding counter
        if char == 'S' or char == 's':
            count_S += 1
        elif char == 'K' or char == 'k':
            count_K += 1
        elif char == 'Y' or char == 'y':
            count_Y += 1

    return count_S, count_K, count_Y

# Example usage:
input_string = "Sky is the limit"
count_S, count_K, count_Y = count_letters(input_string)
print("Number of 'S' characters:", count_S)
print("Number of 'K' characters:", count_K)
print("Number of 'Y' characters:", count_Y)



import unittest


def count_letters(input_string, letters_list=None):
    """Count the occurrences of letters in the input string.

    Args:
        input_string (str): The input string to count letters in.
        letters_list (list): A list of letters to count.

    Returns:
        dict: A dictionary containing counts of letters specified in letters_list.
    """
    if letters_list is None:
        letters_list = ["S", "K", "Y"]
    letters_count = {i: 0 for i in letters_list}
    for letter in input_string:
        if letter not in letters_list:
            continue
        letters_count[letter] += 1
    return letters_count


class TestCharactersCount(unittest.TestCase):
    """Test case class for count_letters function."""

    def test_single_string(self):
        """Test with a single word string."""
        input_string = "SKY"
        expected_results = {"S": 1, "K": 1, "Y": 1}
        actual_result = count_letters(input_string)
        self.assertEqual(
            actual_result, expected_results, "Verifying the count of letters"
        )

    def test_multiple_occurrences(self):
        """Test with a string containing multiple occurrences of letters and numbers"""
        input_string = "SKY1SKY2SKY3"
        expected_results = {"S": 3, "K": 3, "Y": 3}
        actual_result = count_letters(input_string)
        self.assertEqual(
            actual_result, expected_results, "Verifying the count of letters with multiple occurrences and numbers."
        )

    def test_special_characters(self):
        """Test with a string containing special characters."""
        input_string = "!SKY$!@%K^&*Y"
        expected_results = {"S": 1, "K": 2, "Y": 2}
        actual_result = count_letters(input_string)
        self.assertEqual(
            actual_result, expected_results, "Verifying the count of letters with special characters."
        )

    def test_lowercase_letters(self):
        """Test with a string containing only lowercase letters."""
        input_string = "sky"
        expected_results = {"S": 0, "K": 0, "Y": 0}
        actual_result = count_letters(input_string)
        self.assertEqual(
            actual_result, expected_results, "Verifying the count of letters with lowercase."
        )

    def test_uppercase_letters(self):
        """Test with a string containing only uppercase letters."""
        input_string = "SKY"
        expected_results = {"S": 1, "K": 1, "Y": 1}
        actual_result = count_letters(input_string)
        self.assertEqual(
            actual_result, expected_results, "Verifying the count of letters with uppercase."
        )


if __name__ == "__main__":
    unittest.main()

########
from collections import Counter

def count_letters(string, letters):
    """Count occurrences of specified letters in the given string.

    Args:
        string (str): The input string to search.
        letters (str): A string containing the letters to count occurrences of.

    Returns:
        dict: A dictionary where the keys are the letters and the values are their respective counts.

    Raises:
        ValueError: If either the string or letters is None.
        TypeError: If either the string or letters is not a string.
    """
    if string is None or letters is None:
        raise ValueError("Both string and letters must be provided")

    if not isinstance(string, str) or not isinstance(letters, str):
        raise TypeError("Both string and letters must be strings")

    if not string or not letters:
        return {}

    letter_counts = Counter(string)

    result = {letter: letter_counts.get(letter, 0) for letter in letters}

    return result


# Example usage:
try:
    string = "Hello SKY!"
    letters_to_count = "SKY1234"
    result = count_letters(string, letters_to_count)
    print(result)  # Output - {'S': 1, 'K': 1, 'Y': 1, '1': 0, '2': 0, '3': 0, '4': 0}
except (ValueError, TypeError) as e:
    print(e)

