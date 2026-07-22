word_1 = list(input())
word_2 = list(input())



matrix = [[i * 0 for i in range(len(word_1))] for j in range(len(word_2))]

def longest_common_substring(w_1, w_2, matr):
    for i in range(len(w_1)):
        for j in range(len(w_2)):
            if w_1[i] == w_2[j]:
                matr[i][j] = matr[i - 1][j - 1] + 1

    return matr


def longest_common_subsequence(w_1, w_2, matr):
    for i in range(len(w_1)):
        for j in range(len(w_2)):
            if w_1[i] == w_2[j]:
                matr[i][j] = matr[i - 1][j - 1] + 1
            else:
                matr[i][j] = max(matr[i - 1][j], matr[i][j - 1])

    return matr



print(longest_common_subsequence(word_1, word_2, matrix))
