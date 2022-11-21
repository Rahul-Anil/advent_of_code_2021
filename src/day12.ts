import { readFileSync } from "fs";

function isSmallCave(s: string): boolean {
    return /^[a-z]*$/.test(s);
}

function part1(input: string): number {
    const graph: Record<string, Set<string>> = {};
    input
        .trim()
        .split("\n")
        .map((line) => {
            const [from, to] = line.split("-");

            if (!graph[from]) {
                graph[from] = new Set();
            }

            graph[from].add(to);

            if (!graph[to]) {
                graph[to] = new Set();
            }

            graph[to].add(from);
        });

    console.log(graph);

    const paths: Set<string[]> = new Set();
    const todo = [["start"]];

    while (todo.length !== 0) {
        let p = todo.pop();
        if (p) {
            const path: string[] = p;

            if (path[path.length - 1] === "end") {
                paths.add(path);
                continue;
            }

            let lastNode: string = path[path.length - 1];
            graph[lastNode].forEach((node) => {
                if (!isSmallCave(node) || !path.includes(node)) {
                    let newPath: string[] = [...path, node];
                    todo.push(newPath);
                }
            });
        }
    }

    return paths.size;
}

function part2(input: string): number {
    return 1;
}

function main(): void {
    const input: string = readFileSync(
        "../tests/sample_inputs/day_12_sample.txt"
    ).toString();
    console.log(part1(input));
}

main();

export { part1, part2 };
