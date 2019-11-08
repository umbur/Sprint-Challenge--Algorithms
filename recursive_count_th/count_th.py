'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
Initial commit
'''
def count_th(word, count=0):

    n1 = len(word)
    n2 = len('th')

    if (n1 == 0 or n1 < n2):
        return 0

    elif len(word) == 2:
        if word == 'th':
            count +=1
        return count

    elif (word[0: 2] == 'th'):
        count += 1
        return count_th(word[2 - 1:], count)

    else:
        return count_th(word[2 - 1:], count)
print(count_th('thsssth'))
