from heapq import heappush, heappop


def dist(v, w, eq):
    if eq:
        return 10000
    else:
        for i in xrange(1, len(w)):
            if v.endswith(w[:-i]):
                return i
        return len(w)


def construct_seq(s, d, w):
    t = w[s[0]]
    for i in xrange(1, len(s)):
        t = t + w[s[i]][-d[s[i - 1]][s[i]]:]
    return t


def heuristic(x, mdj):
    return sum(mdj[i] for i in xrange(len(x)) if x[i] == 0)


def adjacent_nodes(x):
    ret = []
    for i in xrange(len(x)):
        if x[i] == 0:
            y = list(x)
            y[i] = 1
            ret.append((i, tuple(y)))
    return ret


class Solution(object):
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        n = len(A)

        # special case
        if n == 1:
            return A[0]
        # assert n > 1

        # distance between words
        # dij := the cost in addition to add j after i
        dij = [[dist(A[i], A[j], i == j) for j in xrange(n)] for i in xrange(n)]

        # minimum cost to add j
        mdj = [min(dij[i][j] for i in xrange(n)) for j in xrange(n)]

        # A* search
        # init
        q = []  # priority queue with estimated cost
        for i in xrange(n):
            x = tuple(1 if j == i else 0 for j in xrange(n))
            g = len(A[i])  # actual cost from start
            h = heuristic(x, mdj)  # lower bound of cost till the goal
            heappush(q, (g + h, g, h, x, [i]))

        best_f = None
        best_p = None
        while len(q) > 0:
            # f, g, h, node, path
            f, g, h, x, p = heappop(q)

            if best_f is not None and f >= best_f:
                break

            for j, y in adjacent_nodes(x):
                gy = g + dij[p[-1]][j]
                py = p + [j]

                if sum(y) == n:  # is goal
                    if best_f is None or gy < best_f:
                        best_f = gy
                        best_p = py
                else:
                    hy = heuristic(y, mdj)
                    heappush(q, (gy + hy, gy, hy, y, py))

        return construct_seq(best_p, dij, A)