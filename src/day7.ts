import { readFileSync } from "fs";

function mode(arr: number[]): number {
    let modeMap = new Map();
    let count: number = 0;
    let max: number = 0;
    for (let i = 0; i < arr.length; ++i) {
        if (modeMap.get(arr[i])) {
            modeMap.set(arr[i], modeMap.get(arr[i]) + 1);
        } else {
            modeMap.set(arr[i], 1);
        }

        if (count < modeMap.get(arr[i])) {
            max = arr[i];
            count = modeMap.get(arr[i]);
        }
    }

    return max;
}

function part1(input: string): number {
    const crabPos: number[] = input.trim().split(",").map(Number);
    const align: number = mode(crabPos);
    let fuel = 0;
    for (let i = 0; i < crabPos.length; ++i) {
        fuel += Math.abs(crabPos[i] - align);
    }

    return fuel;
}

function crabFuel(pos: number, crabPos: number[]): number {
    let fuel = 0;
    for (let i = 0; i < crabPos.length; ++i) {
        let n = Math.abs(crabPos[i] - pos);
        fuel += (n * (n + 1)) / 2;
    }
    return fuel;
}

function part2(input: string): number {
    const crabPos: number[] = input.trim().split(",").map(Number);
    const minCrab: number = Math.min(...crabPos);
    const maxCrab: number = Math.max(...crabPos);
    let fuel: number[] = new Array();
    for (let i = minCrab; i < maxCrab; ++i) {
        fuel.push(crabFuel(i, crabPos));
    }

    const minFuel: number = Math.min(...fuel);
    return minFuel;
}

function main(): void {
    const input: string = readFileSync(
        "../tests/sample_inputs/day_7_sample.txt"
    ).toString();
    console.log(part1(input));
    console.log(part2(input));
}

export { part1, part2 };

main();
