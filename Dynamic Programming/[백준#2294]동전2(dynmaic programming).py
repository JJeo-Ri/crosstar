import sys
inp = sys.stdin.readline
n, k = map(int, inp().split())
coins = [int(inp()) for _ in range(n)]
print(n,k, coins)
#dp[k] = k원을 만드는데 필요한 최소 동전의 개수
dp = [10001] * (k+1)
dp[0] = 0
for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i],dp[i-coin]+1)

if dp[k]==10001:
    print(-1)
else:
    print(dp[k])