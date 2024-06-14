dict_squares={i:i**2 for i in range(1,6)}
print(f'{dict_squares=}') #dict_squares={1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

ages=[10,20,30,100,120]
ages_dict={age:('young' if age<=100 else 'old') for age in ages}
print(f'{ages_dict=}') #ages_dict={10: 'young', 20: 'young', 30: 'young', 100: 'young', 120: 'old'}

my_dict={10: 'young', 20: 'young', 30: 'young', 100: 'young', 120: 'old'}
new_dict={v:k for k,v in my_dict.items()}
print(f'{new_dict}') #{'young': 100, 'old': 120}
'''The keys in the dictionary should be unique. It will not throw an error if there are duplicate keys but only takes
the latest pairs to keep the keys unique'''

even_odd_dict={num:('Even' if num%2==0 else 'Odd') for num in range(1,11)}
print(f'{even_odd_dict=}')
#even_odd_dict={1: 'Odd', 2: 'Even', 3: 'Odd', 4: 'Even', 5: 'Odd', 6: 'Even', 7: 'Odd', 8: 'Even', 9: 'Odd', 10: 'Even'}


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



