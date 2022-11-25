import { readFileSync } from "fs";

type Coord = [number, number];

function yFold(coords: Set<Coord>, val: number): Set<Coord> {
    const newCoords: Set<Coord> = new Set();
    coords.forEach(([x, y]) => {
        if (y > val) {
            let yNew = 2 * val - y;
            let coord: Coord = [x, yNew];
            newCoords.add(coord);
        } else {
            let coord: Coord = [x, y];
            newCoords.add(coord);
        }
    });

    return newCoords;
}

function xFold(coords: Set<Coord>, val: number): Set<Coord> {
    const newCoords: Set<Coord> = new Set();
    coords.forEach(([x, y]) => {
        if (x > val) {
            let xNew = 2 * val - x;
            let coord: Coord = [xNew, y];
            newCoords.add(coord);
        } else {
            let coord: Coord = [x, y];
            newCoords.add(coord);
        }
    });

    return newCoords;
}

function dispayDots(coords: Set<Coord>): number {
    let y_max: number = -Infinity;
    let x_max: number = -Infinity;
    let c: number = 0;

    coords.forEach(([x, y]) => {
        if (x > x_max) {
            x_max = x;
        }

        if (y > y_max) {
            y_max = y;
        }
    });

    let paper: string[][] = new Array();
    for (let i = 0; i < y_max + 1; ++i) {
        paper[i] = new Array(x_max + 1).fill(".");
    }

    coords.forEach(([x, y]) => {
        paper[y][x] = "#";
    });

    for (let i = 0; i < y_max + 1; ++i) {
        console.log(paper[i].join(" "));
    }

    for (let i = 0; i < y_max + 1; ++i) {
        for (let j = 0; j < x_max + 1; ++j) {
            if (paper[i][j] === "#") {
                c++;
            }
        }
    }

    return c;
}

function part1(input: string): number {
    let [coordsRaw, foldInstructionsRaw] = input.trim().split("\n\n");
    let coords: Set<Coord> = new Set();
    coordsRaw
        .split("\n")
        .map((line) => line.trim().split(",").map(Number))
        .map(([x, y]) => coords.add([x, y]));

    const foldInstrutions: [string, number][] = foldInstructionsRaw
        .split("\n")
        .map((line) => line.split(" ")[2].split("="))
        .map(([x, y]) => [x, Number(y)]);

    for (let i = 0; i < 1; ++i) {
        let [axis, val] = foldInstrutions[i];
        if (axis == "x") {
            coords = xFold(coords, val);
        } else {
            coords = yFold(coords, val);
        }
    }

    let c = dispayDots(coords);
    return c;
}

function part2(input: string): void {
    let [coordsRaw, foldInstructionsRaw] = input.trim().seplit("\n\n");
    let coords: Set<Coord> = new Set();
    coordsRaw
        .split("\n")
        .map((line) => line.trim().split(",").map(Number))
        .map(([x, y]) => coords.add([x, y]));

    const foldInstrutions: [string, number][] = foldInstructionsRaw
        .split("\n")
        .map((line) => line.split(" ")[2].split("="))
        .map(([x, y]) => [x, Number(y)]);

    for (let i = 0; i < foldInstrutions.length; ++i) {
        let [axis, val] = foldInstrutions[i];
        if (axis == "x") {
            coords = xFold(coords, val);
        } else {
            coords = yFold(coords, val);
        }
    }

    dispayDots(coords);
}

function test(): void {
    const input: string = readFileSync(
        "../tests/sample_inputs/day_13_sample.txt"
    ).toString();
    console.log(part1(input));
}

function main(): void {
    const input: string = readFileSync("../tests/inputs/day_13.txt").toString();
    console.log(part1(input));
    part2(input);
}

main();
