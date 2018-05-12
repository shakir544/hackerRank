# python - basic data types - finding the percentages

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    total = 0
    if query_name in student_marks.keys():
        marks = student_marks[query_name]
        length = len(marks)
        for mark in marks:
            total += mark
        avg = total / length
        print('%.2f' % avg)
