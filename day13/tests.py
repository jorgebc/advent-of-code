from day13 import parsePacketV2, extractList

testInputData = "[1,1,3,1,1]"
first, last = extractList(testInputData)
print(first)
print(last)


testExpectedResult = [1, 1, 3, 1, 1]
# result = parsePacketV2(testInputData)
# assert (
#    result == testExpectedResult
# ), f"Result should be {testExpectedResult} but was {result}"

# testInputData = "[[1],[2,3,4]]"
# testExpectedResult = [[1], [2, 3, 4]]
# result = parsePacketV2(testInputData)
# assert (
#    result == testExpectedResult
# ), f"Result should be {testExpectedResult} but was {result}"
