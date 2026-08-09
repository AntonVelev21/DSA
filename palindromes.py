def is_palindrome(s) -> bool:
    cleaned_string = ''.join([l for l in s if l.isalnum()]).lower()
    return cleaned_string == cleaned_string[::-1]

print(is_palindrome(s = " "))