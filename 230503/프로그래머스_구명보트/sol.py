from collections import deque


def solution(people, limit):
    people.sort()
    people = deque(people)
    temp = 0

    while people:
        if len(people) == 1:
            temp += 1
            break
        if limit >= people[0] + people[-1]:
            people.pop()
            people.popleft()
            temp += 1
        elif limit < people[0] + people[-1]:
            temp += 1
            people.pop()

    answer = temp
    return answer