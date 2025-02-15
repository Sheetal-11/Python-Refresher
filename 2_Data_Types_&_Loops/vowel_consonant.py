# Count vowels and consonants in a string

str_var = "Hello, World!"

# I'm using set() instead of lists because:
# Checking membership in a set (O(1)) is faster than a list (O(n)).
vowels = {'a', 'e', 'i', 'o', 'u'}
consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}

# Convert string to lowercase once
lower_str = str_var.casefold()

# Use sum() with set membership for concise counting
vowel_count = sum(1 for char in lower_str if char in vowels)
consonant_count = sum(1 for char in lower_str if char in consonants)

print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")



