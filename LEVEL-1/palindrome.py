def palindrome_str(string):
    if string==string[::-1]:
        print('yes,string is palindrome')

    else: 
        print('No,string is not palindrome')

string = input('enter a string:')
palindrome_str(string)