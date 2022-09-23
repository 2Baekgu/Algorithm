t = int(input())
for _ in range(t):
    a, b =(map(str, input().split()))
    s_a = ''.join(sorted(a))
    s_b = ''.join(sorted(b))
    if s_a == s_b:
        print(f'{a} & {b} are anagrams.')
    else: print(f'{a} & {b} are NOT anagrams.')