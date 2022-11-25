import { readFileSync } from "fs";

const dir = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
];

function part1(input: string): number {
    const cave: number[][] = input
        .trim()
        .split("\n")
        .map((line) => line.trim().split("").map(Number));
    console.log(cave);
    return 1;
}

function main(): void {
    const input: string = readFileSync(
        "../tests/sample_inputs/day_15_sample.txt"
    ).toString();
    console.log(part1(input));
}

main();
