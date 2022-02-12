def demo1(input):
    x = int(input[0])
    cows = input[1].split(" ")
    cows = list(map(int, cows))
    cows.sort()
    stalls = input[2].split(" ")
    stalls = list(map(int, stalls))
    answer = 1
    def bigger(x):
        ans = 0
        for i in stalls:
            if i >= x:
                ans += 1
        return ans

    for c, i in enumerate(cows):
        answer = answer * (bigger(i) - ((x - 1) - c));
    return str(answer)