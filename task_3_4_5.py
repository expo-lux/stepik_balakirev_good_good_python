import re
if __name__ == '__main__':
    autoTest = False
    if autoTest:
        original = "My best friend is Python!"
    else:
        original = input()
    result = re.sub(' ', "'", original, count=1)
    result = re.sub(' ', '"', result)
    answer = 'My\'best\"friend\"is\"Python!'
    if autoTest:
        assert answer == result, f"Failed {answer} != {result}"
    print(result)
    enumerate()