import { readFileSync } from "fs";

const dir = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
];

function minAdjVal(row: number, col: number, cave: number[][]): number {
    const adjPoints: number[] = new Array();
    for (let i = 0; i < dir.length; ++i) {
        let [x, y] = dir[i];
        if (
            row + x >= 0 &&
            row + x < cave.length &&
            col + y >= 0 &&
            col + y < cave[0].length
        ) {
            adjPoints.push(cave[row + x][col + y]);
        }
    }

    return Math.min(...adjPoints);
}

function part1(input: string): number {
    let riskLevel: number = 0;
    const cave: number[][] = input
        .trim()
        .split("\n")
        .map((line) => line.trim().split("").map(Number));

    for (let i = 0; i < cave.length; ++i) {
        for (let j = 0; j < cave[0].length; ++j) {
            if (cave[i][j] < minAdjVal(i, j, cave)) {
                riskLevel += cave[i][j] + 1;
            }
        }
    }

    return riskLevel;
}

function getLowPoints(cave: number[][]): [number, number][] {
    const lowPoints: [number, number][] = new Array();
    for (let i = 0; i < cave.length; ++i) {
        for (let j = 0; j < cave[0].length; ++j) {
            if (cave[i][j] < minAdjVal(i, j, cave)) {
                lowPoints.push([i, j]);
            }
        }
    }

    return lowPoints;
}

function walk(
    cave: number[][],
    row: number,
    col: number,
    seen: boolean[][],
    basin: [number, number][]
): boolean {
    //Base case
    // out of bounds
    if (row < 0 || row >= cave.length || col < 0 || col >= cave[0].length) {
        return false;
    }

    // if 9
    if (cave[row][col] === 9) {
        return false;
    }

    if (seen[row][col]) {
        return false;
    }

    // recursive part
    seen[row][col] = true;
    basin.push([row, col]);

    for (let i = 0; i < dir.length; ++i) {
        let [x, y] = dir[i];
        if (walk(cave, row + x, col + y, seen, basin)) {
            return true;
        }
    }

    return false;
}

function part2(input: string): number {
    let basinLength: number[] = [];
    const cave: number[][] = input
        .trim()
        .split("\n")
        .map((line) => line.trim().split("").map(Number));
    const lowPoints: [number, number][] = getLowPoints(cave);

    for (let lowPoint = 0; lowPoint < lowPoints.length; ++lowPoint) {
        let [x, y] = lowPoints[lowPoint];
        const seen: boolean[][] = [];
        const basin: [number, number][] = [];

        for (let i = 0; i < cave.length; ++i) {
            seen[i] = new Array(cave[0].length).fill(false);
        }

        walk(cave, x, y, seen, basin);
        basinLength.push(basin.length);
    }

    basinLength.sort(function (a, b) {
        return a - b;
    });
    basinLength.reverse();

    return basinLength[0] * basinLength[1] * basinLength[2];
}

function main(): void {
    const input: string = readFileSync(
        "../tests/sample_inputs/day_9_sample.txt"
    ).toString();
    console.log(part1(input));
    console.log(part2(input));
}

export { part1, part2 };

main();
