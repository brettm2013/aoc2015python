from aoc.core import timeit
import itertools


@timeit
def part1(data: str) -> int:
    travel_dict = {}
    all_destinations = []
    for line in data.strip().splitlines():
        dest_dist = line.split("=")
        distance = int(dest_dist[1].strip())
        locations_list = dest_dist[0].split("to")
        to_from = [locations_list[0].strip(), locations_list[1].strip()]

        for item in to_from:
            if item not in all_destinations:
                all_destinations.append(item)

        if to_from[0] in travel_dict:
            travel_dict[to_from[0]] += [(to_from[1], distance)]
        else:
            travel_dict[to_from[0]] = [(to_from[1], distance)]

        if to_from[1] in travel_dict:
            travel_dict[to_from[1]] += [(to_from[0], distance)]
        else:
            travel_dict[to_from[1]] = [(to_from[0], distance)]

    all_cities = set(all_destinations)

    def get_distances(start, end):
        for dest, dist in travel_dict.get(end, []):
            if dest == start:
                return dist
        return 0

    path_distances = []
    for path in itertools.permutations(all_cities):
        current_dist = 0

        for i in range(len(path) - 1):
            current_dist += get_distances(path[i], path[i + 1])
        path_distances.append(current_dist)

    return min(path_distances)


# Same logic as above but runs at 0(1) as opposed to O(n)
@timeit
def part2(data: str) -> int:
    dist_map = {}
    all_destinations = set()

    for line in data.strip().splitlines():
        start, _, end, _, dist = line.split()

        dist_map[(start, end)] = int(dist)
        dist_map[(end, start)] = int(dist)
        all_destinations.add(start)
        all_destinations.add(end)

    path_distances = []
    for path in itertools.permutations(all_destinations):
        current_dist = 0

        for i in range(len(path) - 1):
            current_dist += dist_map[(path[i], path[i + 1])]
        path_distances.append(current_dist)

    return max(path_distances)
