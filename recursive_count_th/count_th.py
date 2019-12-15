'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
Initial commit
'''
def count_th(word, count=0):
# Defining n1 length of the given word and n2 length of the string 'th'
    n1 = len(word)
    n2 = len('th')

# If the n1's length is 0 or is less than n2 retrun 0
    if (n1 == 0 or n1 < n2):
        return 0

# Else if the length of the word is equal 2 and if the word is 'th' increase counter by 1
    elif len(word) == 2:
        if word == 'th':
            count +=1
        return count

# Else if the values of the first 2 indexes equals 'th', increase the counter by 1
# and start the count_th function by decreasing words's first index to start from [1]
    elif (word[0: 2] == 'th'):
        count += 1
        return count_th(word[1:], count)

# Else start the count_th function by decreasing word's first index to start from [1]
    else:
        return count_th(word[1:], count)
print(count_th('thsssth'))

