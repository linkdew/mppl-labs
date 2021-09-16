def solution(s):
    result = []

    def allNaturalDivisors(number):
        for k in range(2, int(number**0.5) + 1):
            if number % k == 0:
                result.append(s.count(s[:k]))
                result.append(s.count(s[:(number // k)]))
        return result

    result = allNaturalDivisors(len(s))

    if (len(result) == 0) and (s != len(s) * s[0]):
        return 1
    elif (len(result) == 0) and s == (len(s) * s[0]):
        return len(s)
    else:
        return max(result)


def test():
    assert solution("abccbaabccba") == 2, "Check your implementation!"
    assert solution("abcabcabcabc") == 4, "Check your implementation!"
    assert solution("abcabcabcabcabcabcabcabcabc") == 9, "Check your implementation!"
    assert solution("abccba" * 38) == 38, "Check your implementation!"
    print("Local tests for func passed!")


if __name__ == "__main__":
    test()
