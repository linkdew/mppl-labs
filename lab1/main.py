def solution(s):
    sliced = []
    result = []

    for i in range(len(s)):
        sliced.append(s[:i + 1])

    for _, i in enumerate(sliced):
        slicecount = s.count(i)
        slicefreq = len(s) / len(i)

        if (i * int(slicefreq)) == s:
            result.append(slicecount)

    return max(result)


def test():
    assert solution("abccbaabccba") == 2, "Check your implementation!"
    assert solution("abcabcabcabc") == 4, "Check your implementation!"
    assert solution("abcabcabcabcabcabcabcabc") == 8, "Check your implementation!"
    assert solution("abccba" * 33) == 33, "Check your implementation!"
    print("Local tests for func passed!")


if __name__ == "__main__":
    test()
