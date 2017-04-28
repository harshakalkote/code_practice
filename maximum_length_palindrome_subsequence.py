def maximum_length_palindrome_subsequence(text):
    text = list(text)
    textlength = len(text)
    palindrome_string = [[0 for i in xrange(textlength)] for j in xrange(textlength)]
    for i in xrange(textlength):
        palindrome_string[i][i] = 1
    for gap in xrange(1,textlength):
        for i in xrange(textlength-1):
            h = i + gap
            if h >= textlength:
                break
            if text[i] == text[h]:
                if gap == 1:
                    palindrome_string[i][h] = 2
                else:    
                    palindrome_string[i][h] = palindrome_string[i+1][h-1] + 2 
            else:
                palindrome_string[i][h] = max(palindrome_string[i+1][h], palindrome_string[i][h-1])
    return palindrome_string[0][textlength-1]                
                
print maximum_length_palindrome_subsequence('abcbda')
