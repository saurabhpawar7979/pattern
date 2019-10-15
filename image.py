# Python program for Finite Automata
# Patterntern searching Algorithm

NO_OF_CHARS = 256


def getNextState(Pattern, M, state, x):
    '''
    calculate the next state
    '''

    # If the character c is same as next character
    # in Patterntern, then simply increment state

    if state < M and x == ord(Pattern[state]):
        return state + 1

    i = 0
    # ns stores the result which is next state

    # ns finally contains the longest prefix
    # which is also suffix in "Pattern[0..state-1]c"

    # Start from the largest possible value and
    # stop when you find a prefix which is also suffix
    for ns in range(state, 0, -1):
        if ord(Pattern[ns - 1]) == x:
            while (i < ns - 1):
                if Pattern[i] != Pattern[state - ns + 1 + i]:
                    break
                i += 1
            if i == ns - 1:
                return ns
    return 0


def computeTF(Pattern, M):
    '''
    This function builds the TF table which
    represents Finite Automata for a given Patterntern
    '''
    global NO_OF_CHARS

    TF = [[0 for i in range(NO_OF_CHARS)]
          for _ in range(M + 1)]

    for state in range(M + 1):
        for x in range(NO_OF_CHARS):
            z = getNextState(Pattern, M, state, x)
            TF[state][x] = z

    return TF


def search(Pattern, Text):
    '''
    Prints all occurrences of Pattern in Text
    '''
    global NO_OF_CHARS
    M = len(Pattern)
    N = len(Text)
    TF = computeTF(Pattern, M)

    # Process Text over FA.
    state = 0
    for i in range(N):
        state = TF[state][ord(Text[i])]
        if state == M:
            print("Pattern found at index: {}".
                  format(i - M + 1))

        # Driver program to test above function


def main():
    Text = input("Enter Text : ")
    Pattern = input("Enter Pattern : ")
    search(Pattern, Text)


if __name__ == '__main__':
    main()