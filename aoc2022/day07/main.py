from collections import defaultdict


class Node:
    def __init__(self, parent, name) -> None:
        self.parent = parent
        self.name = name
        self.files = defaultdict(dict)
        self.children = defaultdict(dict)

    def get_size(self):
        return sum(self.files.values()) + sum(
            c.get_size() for c in self.children.values()
        )

    def __repr__(self) -> str:
        return f"dir: {self.name}: {sum(s for s in self.files.values())}"

    def __iter__(self):
        for c in self.children.values():
            yield from c
        yield self

    def print_tree(self, offset=0) -> str:
        def append_files(s):
            return (
                s
                + "\n"
                + "\n".join(
                    f"{' ' * offset}file: {name}: {size}"
                    for name, size in self.files.items()
                )
            )

        def append_dirs(s):
            return (
                s
                + "\n"
                + "\n".join(c.print_tree(offset + 4) for c in self.children.values())
            )

        s = (" " * offset) + self.__repr__()
        if self.files:
            s = append_files(s)
        if self.children:
            s = append_dirs(s)
        return s


def parse_structure(lines, dir_tree):
    location = dir_tree
    for line in lines:
        match line.strip().split(" "):
            case ["$", "cd", "/"]:
                location = dir_tree
            case ["$", "cd", ".."]:
                location = location.parent
            case ["$", "cd", dir]:
                location = location.children[dir]
            case ["$", "ls"]:
                pass
            case ["dir", dirname]:
                location.children[dirname] = Node(location, dirname)
            case [filesize, filename]:
                location.files[filename] = int(filesize)


def part1():
    with open("aoc2022/day07/input.txt", "r") as in_f:
        dir_tree = Node(None, "/")
        parse_structure(in_f.readlines(), dir_tree)

    def get_max_100000(location, total):
        if (size := location.get_size()) <= 100000:
            total["total"] += size
        for c in location.children.values():
            get_max_100000(c, total)

    total = {"total": 0}
    get_max_100000(dir_tree, total)
    print(total["total"])


def part2():
    with open("aoc2022/day07/input.txt", "r") as in_f:
        dir_tree = Node(None, "/")
        parse_structure(in_f.readlines(), dir_tree)

        size_used = dir_tree.get_size()
        size_available = 70_000_000 - size_used
        size_required = 30_000_000 - size_available

        sizes = [c.get_size() for c in dir_tree]
        sizes.append(size_required)
        sizes = sorted(sizes)
        print(sizes[sizes.index(size_required) + 1])


part2()
