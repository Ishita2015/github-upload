def minion_game(string):
    # your code goes here
    vowels = ['A', 'E', 'I', 'O', 'U']
    vlist = []
    clist = []
    for i in range(0, len(s)):
        for j in range(i+1, len(s)+1):
            if s[i] in vowels:
                vlist.append(s[i:j])
                #print ('Vowels list:', vlist)
            else:
                clist.append(s[i:j])
                #print ('Consonants list', clist)
    if len(vlist) > len(clist):
        print('Kevin', len(vlist))
    elif len(vlist) < len(clist):
        print('Stuart', len(clist))
    else:
        print('Draw')

# def minion_game(string):
#     # your code goes here
#     vowels = ['A', 'E', 'I', 'O', 'U']
#     vlist = 0
#     clist = 0
#     for i in range(0, len(s)):
#         if s[i] in vowels:
#             vlist += len(s) - i
#             #print ('Vowels list:', vlist)
#         else:
#             clist += len(s) - i
#             #print ('Consonants list', clist)
#     if vlist > clist:
#         print('Kevin', vlist)
#     elif vlist < clist:
#         print('Stuart', clist)
#     else:
#         print('Draw')


if __name__ == '__main__':
    s = input("Enter your string: ")
    minion_game(s)
