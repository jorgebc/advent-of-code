def parsePacket(packet):
    print(packet)

    if len(packet) == 0:
        return []

    if packet[0].isdigit():
        if len(packet) == 1:
            return int(packet[0])
        else:
            return [int(packet[0])] + [parsePacket(packet[1:])]

    if packet[0] == ",":
        return parsePacket(packet[1:])

    if packet[0] == "]":
        return parsePacket(packet[1:])

    if packet[0] == "[":
        return [] + parsePacket(packet[1:])


def listStarting(packet):
    return packet[0] == "[" and packet[:1] == "]"


def listFinishing(packet):
    return packet[0] == "["


def find_nth(string, substring, n):
    if n == 1:
        return string.find(substring)
    else:
        return string.find(substring, find_nth(string, substring, n - 1) + 1)


def countOpenBracketsTillFirstNumber(packet):
    counter = 0
    for c in packet:
        counter = counter + 1
        if c != "[":
            break

    return counter


def extractList(packet):
    start = 1
    nth = countOpenBracketsTillFirstNumber(packet)
    finish = find_nth(packet, "]", nth)
    print(finish)
    first = packet[start:finish]
    last = 
    return [first, last]


def parsePacketV2(packet):
    print(f"packet {packet}\n")

    if len(packet) == 0:
        return []

    if packet[0] == ",":
        return parsePacketV2(packet[1:])

    if packet[0].isdigit():
        if len(packet) == 1:
            return [int(packet[0])]

        return [int(packet[0])] + parsePacketV2(packet[1:])

    first, rest = extractList(packet)
    print(first)
    print(rest)
    return parsePacketV2(first) + parsePacketV2(rest)
