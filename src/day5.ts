import { readFileSync } from "fs";

function maxElement(arr: number[][]): number {
    let max = -Infinity;
    for (let i = 0; i < arr.length; ++i) {
        for (let j = 0; j < arr[0].length; ++j) {
            if (max < arr[i][j]) {
                max = arr[i][j];
            }
        }
    }

    return max;
}

function part1(input: string): number {
    const coords: number[][] = input
        .trim()
        .split("\n")
        .map((line) => line.split(" -> ").join(",").split(",").map(Number));
    const maxCoord = maxElement(coords) + 1;

    const graph: number[][] = new Array(maxCoord)
        .fill(0)
        .map(() => new Array(maxCoord).fill(0));

    for (let i = 0; i < coords.length; ++i) {
        if (coords[i][0] === coords[i][2]) {
            let row = coords[i][0];
            let minElement = Math.min(coords[i][1], coords[i][3]);
            let maxElement = Math.max(coords[i][1], coords[i][3]);
            for (let col = minElement; col <= maxElement; ++col) {
                graph[row][col]++;
            }
        } else if (coords[i][1] === coords[i][3]) {
            let col = coords[i][3];
            let minElement = Math.min(coords[i][0], coords[i][2]);
            let maxElement = Math.max(coords[i][0], coords[i][2]);
            for (let row = minElement; row <= maxElement; ++row) {
                graph[row][col]++;
            }
        } else {
            continue;
        }
    }

    let count = 0;
    for (let i = 0; i < maxCoord; ++i) {
        for (let j = 0; j < maxCoord; ++j) {
            if (graph[i][j] > 1) {
                count++;
            }
        }
    }
    return count;
}
function part2(input: string): number {
    const coords: number[][] = input
        .trim()
        .split("\n")
        .map((line) => line.split(" -> ").join(",").split(",").map(Number));
    const maxCoord = maxElement(coords) + 1;

    const graph: number[][] = new Array(maxCoord)
        .fill(0)
        .map(() => new Array(maxCoord).fill(0));

    for (let i = 0; i < coords.length; ++i) {
        if (coords[i][0] === coords[i][2]) {
            let row = coords[i][0];
            let minElement = Math.min(coords[i][1], coords[i][3]);
            let maxElement = Math.max(coords[i][1], coords[i][3]);
            for (let col = minElement; col <= maxElement; ++col) {
                graph[row][col]++;
            }
        } else if (coords[i][1] === coords[i][3]) {
            let col = coords[i][3];
            let minElement = Math.min(coords[i][0], coords[i][2]);
            let maxElement = Math.max(coords[i][0], coords[i][2]);
            for (let row = minElement; row <= maxElement; ++row) {
                graph[row][col]++;
            }
        } else {
            let dx = coords[i][0] - coords[i][2] > 0 ? -1 : 1;
            let dy = coords[i][1] - coords[i][3] > 0 ? -1 : 1;
            let row = coords[i][0];
            let col = coords[i][1];
            graph[row][col]++;
            while (row !== coords[i][2]) {
                row += dx;
                col += dy;
                graph[row][col]++;
            }
        }
    }

    let count = 0;
    for (let i = 0; i < maxCoord; ++i) {
        for (let j = 0; j < maxCoord; ++j) {
            if (graph[i][j] > 1) {
                count++;
            }
        }
    }
    return count;
}
function main() {
    const input: string = readFileSync(
        "../tests/sample_inputs/day_5_sample.txt"
    ).toString();
    console.log(part1(input));
    console.log(part2(input));
}

main();

export { part1, part2 };
