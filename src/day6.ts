import { readFileSync } from "fs";

function part1(input: string): number {
    let fishInit: number[] = input.trim().split(",").map(Number);
    let lanternFish = new Map();

    // Initializing lanternfishMap
    for (let i = 0; i < 9; ++i) {
        lanternFish.set(i, 0);
    }

    for (let i = 0; i < fishInit.length; ++i) {
        let fishTimer = lanternFish.get(fishInit[i]);
        lanternFish.set(fishInit[i], fishTimer + 1);
    }

    for (let d = 0; d < 80; ++d) {
        let z = lanternFish.get(0);
        lanternFish.set(0, 0);
        for (let i = 1; i < 9; ++i) {
            lanternFish.set(i - 1, lanternFish.get(i));
        }
        lanternFish.set(8, z);
        lanternFish.set(6, lanternFish.get(6) + z);
    }

    let sum = 0;
    for (let i = 0; i < 9; ++i) {
        sum += lanternFish.get(i);
    }

    return sum;
}

function part2(input: string): number {
    let fishInit: number[] = input.trim().split(",").map(Number);
    let lanternFish = new Map();

    // Initializing lanternfishMap
    for (let i = 0; i < 9; ++i) {
        lanternFish.set(i, 0);
    }

    for (let i = 0; i < fishInit.length; ++i) {
        let fishTimer = lanternFish.get(fishInit[i]);
        lanternFish.set(fishInit[i], fishTimer + 1);
    }

    for (let d = 0; d < 256; ++d) {
        let z = lanternFish.get(0);
        lanternFish.set(0, 0);
        for (let i = 1; i < 9; ++i) {
            lanternFish.set(i - 1, lanternFish.get(i));
        }
        lanternFish.set(8, z);
        lanternFish.set(6, lanternFish.get(6) + z);
    }

    let sum = 0;
    for (let i = 0; i < 9; ++i) {
        sum += lanternFish.get(i);
    }

    return sum;
}

function main(): void {
    const input: string = readFileSync(
        "../tests/sample_inputs/day_6_sample.txt"
    ).toString();

    console.log(part1(input));
    console.log(part2(input));
}

export { part1, part2 };

main();
