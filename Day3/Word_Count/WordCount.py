def words(A):

    word = A.split
    d = dict()

    for word in A:
        if word.isdigit():
          d[int(word)] = A.count(word)
        else: 
            d[word] = A.count(word)
    return d
    print dict.items()
    print sorted(dict.word(),key=A.count(word))
