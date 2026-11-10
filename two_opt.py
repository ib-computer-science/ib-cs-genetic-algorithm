import random

from distances import DISTANCES, STARTCITY, VISITED_CITIES


def route_length(route):
    """Length of the closed tour STARTCITY -> route -> STARTCITY."""
    length = DISTANCES[STARTCITY][route[0]] + DISTANCES[STARTCITY][route[-1]]
    for city_a, city_b in zip(route, route[1:]):
        length += DISTANCES[city_a][city_b]
    return length


def _best_move(route):
    """Find the most improving 2-opt move (reversal of route[i:j + 1]).

    Returns (delta, i, j), where delta is the (non-positive) change in route
    length that move would produce; (0, None, None) if no move improves on
    the route as given."""
    n = len(route)
    best_delta, best_i, best_j = 0, None, None
    for i in range(n):
        a = STARTCITY if i == 0 else route[i - 1]
        b = route[i]
        for j in range(i + 1, n):
            c = route[j]
            d = STARTCITY if j == n - 1 else route[j + 1]
            delta = DISTANCES[a][c] + DISTANCES[b][d] - DISTANCES[a][b] - DISTANCES[c][d]
            if delta < best_delta:
                best_delta, best_i, best_j = delta, i, j
    return best_delta, best_i, best_j


def local_search(route):
    """Improve route in place via 2-opt until no improving move remains."""
    while True:
        _, i, j = _best_move(route)
        if i is None:
            return
        route[i:j + 1] = route[i:j + 1][::-1]


def solve(num_restarts):
    """Run 2-opt from num_restarts random starting tours, return the
    shortest (route, length) found."""
    assert num_restarts > 0
    best_route, best_length = None, None
    for _ in range(num_restarts):
        route = list(VISITED_CITIES)
        random.shuffle(route)
        local_search(route)
        length = route_length(route)
        if best_length is None or length < best_length:
            best_route, best_length = route, length
    return best_route, best_length


def _route_to_string(route):
    return STARTCITY + "".join(route) + STARTCITY


def main():
    num_restarts = 200
    route, length = solve(num_restarts)
    print(f"best [ {_route_to_string(route)} ] length [ {length} ]")


if __name__ == "__main__":
    main()
