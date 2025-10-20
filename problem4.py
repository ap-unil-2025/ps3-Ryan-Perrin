"""
Problem 4: File Word Counter
Process text files and perform various analyses.
"""

def create_sample_file(filename="sample.txt"):
    """
    Create a sample text file for testing.

    Args:
        filename (str): Name of the file to create
    """
    content = """Python is a powerful programming language.
It is widely used in web development, data science, and automation.
Python's simple syntax makes it great for beginners.
Many companies use Python for their projects."""

    with open(filename, 'w') as f:
        f.write(content)
    print(f"Created {filename}")


def count_words(filename):
    
    """
    Count total words in the file.

    Args:
        filename (str): Name of the file to analyze

    Returns:
        int: Total number of words
    """
    # TODO: Open file and count words
    # Hint: Use split() to separate words
    
    with open(filename, 'r') as f: #open the file in read mode
        text = f.read() #read the text
        words = text.split()  #split() separate on the spaces
    return len(words) #returns the number total of words


def count_lines(filename):
    with open(filename, 'r')as f: #open the file in read mode
        lines = f.readlines() #read all the lines and put them into a list
    return len(lines) #return the total number of lines
    """
    Count total lines in the file.

    Args:
        filename (str): Name of the file to analyze

    Returns:
        int: Total number of lines
    """
    # TODO: Open file and count lines


def count_characters(filename, include_spaces=True):
     with open(filename, 'r') as f: #open the file in read mode
        text = f.read() #read all the text as a single string of characters
     if not include_spaces: #if we don't want to count spaces and line breaks -> remove them (false)
        text = text.replace(" ", "").replace("\n", "") #removes spaces and line breaks by replacing them by nothing
     return len(text) #returns the length of the final string 
"""
    
    Count characters in the file.
    Args:
        filename (str): Name of the file to analyze
        include_spaces (bool): Whether to include spaces in count
    
    Returns:
        int: Total number of characters
"""
    # TODO: Open file and count characters
    # If include_spaces is False, don't count spaces
     

def find_longest_word(filename):
    import string #import punctuation

    with open(filename, 'r') as f: #same as usual
        text = f.read()

    for p in string.punctuation: #general punctuation as p
        text = text.replace(p, "") #replace all the punctuation and special characters by nothing in order to delete them

    words = text.split() #splits the text into words
    return max(words, key=len) if words else "" #returns the longest word in the textif there is at least one

    """
    Find and return the longest word in the file.

    Args:
        filename (str): Name of the file to analyze

    Returns:
        str: The longest word found
    """
    # TODO: Find the longest word
    # Hint: You might need to remove punctuation



def word_frequency(filename):
    import string #import puncutations
    frequency = {} #create an empty dictionnary to stock the the frequency of the words

    with open(filename, 'r') as f: #same than before
        text = f.read().lower() #put all the text in lower characters in order to not make difference

    for p in string.punctuation:
        text = text.replace(p, "") #same than before, remove punctuation and special characters

    words = text.split() #split the text in different words

    for word in words: #take all the words separately of the list "words"
        frequency[word] = frequency.get(word, 0) + 1 #increase by one each time the same word appears

    return frequency
    """
    Return a dictionary of word frequencies.
    Convert words to lowercase and remove punctuation.

    Args:
        filename (str): Name of the file to analyze

    Returns:
        dict: Dictionary with words as keys and frequencies as values
    """
    import string

    frequency = {}

    # TODO: Open file
    # TODO: Read all words
    # TODO: Convert to lowercase
    # TODO: Remove punctuation (use string.punctuation)
    # TODO: Count frequency of each word

    return frequency


def analyze_file(filename):
    """
    Perform complete analysis of the file.

    Args:
        filename (str): Name of the file to analyze
    """
    print(f"\nAnalyzing: {filename}")
    print("-" * 40)

    try:
        # Display all analyses
        print(f"Lines: {count_lines(filename)}")
        print(f"Words: {count_words(filename)}")
        print(f"Characters (with spaces): {count_characters(filename, True)}")
        print(f"Characters (without spaces): {count_characters(filename, False)}")
        print(f"Longest word: {find_longest_word(filename)}")

        # Display top 5 most common words
        print("\nTop 5 most common words:")
        freq = word_frequency(filename)

        # Sort by frequency and get top 5
        top_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
        for word, count in top_words:
            print(f"  '{word}': {count} times")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Main function to run the file analyzer."""
    # Create sample file
    create_sample_file()

    # Analyze the sample file
    analyze_file("sample.txt")

    # Allow user to analyze their own file
    print("\n" + "=" * 40)
    user_file = input("Enter a filename to analyze (or press Enter to skip): ").strip()
    if user_file:
        analyze_file(user_file)


if __name__ == "__main__":
    main()