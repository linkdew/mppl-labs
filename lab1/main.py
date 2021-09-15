def solution(s):
    result = []

    def allNaturalDivisors(number):
        divarray = []
        for k in range(2, int((number / 2)) + 1):
            if number % k == 0:
                divarray.append(k)
        return divarray

    divisors = allNaturalDivisors(len(s))

    for i in range(len(divisors)):
        result.append(s.count(s[:divisors[i]]))

    if (len(result) == 0) and (s != len(s) * s[0]):
        return 1
    elif (len(result) == 0) and s == (len(s) * s[0]):
        return len(s)
    else:
        return max(result)


def test():
    assert solution("abccbaabccba") == 2, "Check your implementation!"
    assert solution("abcabcabcabc") == 4, "Check your implementation!"
    print("Local tests for func passed!")


if __name__ == "__main__":
    test()
