t = int(input())
for _ in range(t):
    hc, dc = [int(x) for x in input().split()]
    hm, dm = [int(x) for x in input().split()]
    k, w, a = [int(x) for x in input().split()]
    if k != 0:
        for i in range(k+1):
            j = k - i
            dc2 = dc + i * w
            hc2 = hc + j * a
            """
            print("try {}".format(i))
            print("   dc2 = {}".format(dc2))
            print("   hc2 = {}".format(hc2))
            """
            c_turns = hm // dc2
            if hm % dc2 != 0:
                c_turns += 1
            m_turns = hc2 // dm
            if hc2 % dm != 0:
                m_turns += 1
            if c_turns <= m_turns:
                print("YES")
                break
        else:
            print("NO")
    else:
        c_turns = hm // dc
        if hm % dc != 0:
            c_turns += 1
        m_turns = hc // dm
        if hc % dm != 0:
            m_turns += 1
        if c_turns <= m_turns:
            print("YES")
        else:
            print("NO")


