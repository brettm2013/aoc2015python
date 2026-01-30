from aoc.core import timeit


@timeit
def part1(data: str) -> int:
    # class Location:
    #     def __init__(self, x: int = 0, y: int = 0):
    #         self.x = x
    #         self.y = y
    #
    houses_visited: dict[tuple[int, int], int] = {}
    # houses_visited: dict[Location, int] = {}

    location: tuple[int, int] = (0, 0)
    # location: Location = Location()

    for move in data:
        houses_visited[location] = houses_visited.get(location, 0) + 1
        match move:
            case ">":
                # East
                location = (location[0] + 1, location[1])
                # location.x += 1
            case "^":
                # North
                # location.y += 1
                location = (location[0], location[1] + 1)
            case "v":
                # South
                # location.y -= 1
                location = (location[0], location[1] - 1)
            case "<":
                # West
                location = (location[0] - 1, location[1])
                # location.x -= 1
    return len(houses_visited)


@timeit
def part2(data: str) -> int:
    houses_visited: dict[tuple[int, int], int] = {}

    location_santa: tuple[int, int] = (0, 0)
    location_robo: tuple[int, int] = (0, 0)
    is_santa = True

    for move in data:
        if is_santa:
            houses_visited[location_santa] = houses_visited.get(location_santa, 0) + 1
            match move:
                case ">":
                    # East
                    location_santa = (location_santa[0] + 1, location_santa[1])
                case "^":
                    # North
                    location_santa = (location_santa[0], location_santa[1] + 1)
                case "v":
                    # South
                    location_santa = (location_santa[0], location_santa[1] - 1)
                case "<":
                    # West
                    location_santa = (location_santa[0] - 1, location_santa[1])
                    # location.x -= 1
        else:
            houses_visited[location_robo] = houses_visited.get(location_robo, 0) + 1
            match move:
                case ">":
                    # East
                    location_robo = (location_robo[0] + 1, location_robo[1])
                    # location.x += 1
                case "^":
                    # North
                    # location.y += 1
                    location_robo = (location_robo[0], location_robo[1] + 1)
                case "v":
                    # South
                    # location.y -= 1
                    location_robo = (location_robo[0], location_robo[1] - 1)
                case "<":
                    # West
                    location_robo = (location_robo[0] - 1, location_robo[1])
                    # location.x -= 1
        is_santa = not is_santa

    return len(houses_visited)
