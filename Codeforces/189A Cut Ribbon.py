import sys

def main():
    n, a, b, c = map(int, sys.stdin.readline().split())

    dp = [-1] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for length in (a, b, c):
            if i >= length and dp[i - length] != -1:
                dp[i] = max(dp[i], dp[i - length] + 1)

    print(dp[n])

if __name__ == "__main__":
    main()