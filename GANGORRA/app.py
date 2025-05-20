p1, c1, p2, c2 = map(int, input().split())
conta1 = p1 * c1
conta2 = p2 * c2
if conta1 == conta2:
    print("0")
elif conta1 > conta2:
    print("-1")
else:
    print("1")