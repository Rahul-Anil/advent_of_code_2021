import { readFileSync } from "fs";

let dir = [
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1],
    [0, -1],
    [-1, -1],
    [-1, 0],
    [-1, 1],
];

function part1(input: string): number {
    let energy = input
        .trim()
        .split("\n")
        .map((line) => line.trim().split("").map(Number));
    let flash: number = 0;

    for (let s = 0; s < 100; ++s) {
        let ef = new Array();
        for (let i = 0; i < energy.length; ++i) {
            for (let j = 0; j < energy[0].length; ++j) {
                energy[i][j]++;
                if (energy[i][j] > 9) {
                    ef.push([i, j]);
                }
            }
        }

        while (ef.length !== 0) {
            let [x, y] = ef[ef.length - 1];
            //console.log(`x: ${x}, y: ${y}`);
            ef.pop();

            if (energy[x][y] === 0) {
                continue;
            }

            energy[x][y] = 0;
            flash++;

            for (let d = 0; d < dir.length; ++d) {
                let [xd, yd] = dir[d];
                //console.log(`xd: ${xd}, yd: ${yd}`);

                let row = x + xd;
                let col = y + yd;

                if (
                    row >= 0 &&
                    row < energy.length &&
                    col >= 0 &&
                    col < energy[0].length &&
                    energy[row][col] !== 0
                ) {
                    energy[row][col]++;
                    if (energy[row][col] > 9) {
                        //console.log(`>9: ${energy[row][col]}`);
                        ef.push([row, col]);
                    }
                }
            }
        }
    }
    return flash;
}

function allEqual(energy: number[][]): boolean {
    for (let i = 0; i < energy.length; ++i) {
        for (let j = 0; j < energy.length; ++j) {
            if (energy[i][j] !== 0) {
                return false;
            }
        }
    }

    return true;
}

function part2(input: string): number {
    let energy = input
        .trim()
        .split("\n")
        .map((line) => line.trim().split("").map(Number));
    let step = 1;

    while (true) {
        let ef = new Array();
        for (let i = 0; i < energy.length; ++i) {
            for (let j = 0; j < energy[0].length; ++j) {
                energy[i][j]++;
                if (energy[i][j] > 9) {
                    ef.push([i, j]);
                }
            }
        }

        while (ef.length !== 0) {
            let [x, y] = ef[ef.length - 1];
            //console.log(`x: ${x}, y: ${y}`);
            ef.pop();

            if (energy[x][y] === 0) {
                continue;
            }

            energy[x][y] = 0;

            for (let d = 0; d < dir.length; ++d) {
                let [xd, yd] = dir[d];
                //console.log(`xd: ${xd}, yd: ${yd}`);

                let row = x + xd;
                let col = y + yd;

                if (
                    row >= 0 &&
                    row < energy.length &&
                    col >= 0 &&
                    col < energy[0].length &&
                    energy[row][col] !== 0
                ) {
                    energy[row][col]++;
                    if (energy[row][col] > 9) {
                        //console.log(`>9: ${energy[row][col]}`);
                        ef.push([row, col]);
                    }
                }
            }
        }

        if (allEqual(energy)) {
            return step;
        }

        step++;
    }
}

function main(): void {
    const input: string = readFileSync(
        "../tests/sample_inputs/day_11_sample.txt"
    ).toString();
    console.log(part1(input));
    console.log(part2(input));
}
main();
