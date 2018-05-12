# Nested List in Python


if __name__ == '__main__':
    dict = { }
    for _ in range(int(input())):
        name = input()
        score = float(input())

        if score in dict :
            dict[score].append(name)
        else:
            dict[score] = [name]
    scores = list(dict.keys())
    scores.sort()

    for score in sorted(dict[scores[1]]):
        print(score)











