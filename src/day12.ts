import { readFileSync } from "fs";

function isSmallCave(s: string): boolean {
    return /^[a-z]*$/.test(s);
}

function part1(input: string): number {
    const graph = {};
    const nodes: string[][] = input
        .trim()
        .split("\n")
        .map((l) => {
            const [from, to] = l.split("-");
            if (!graph[from]) {
                graph[from] = [];
            }
            if (!graph[to]) {
                graph[to] = [];
            }

            graph[from].push(to);
        });

    return 1;
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
