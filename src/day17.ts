import { readFileSync } from "fs";

function part1(input: string): number {
    let [[x1, x2], [y1, y2]] = input
        .trim()
        .split(":")[1]
        .trim()
        .split(",")
        .map((c) => c.split("=")[1].split("..").map(Number));

    let maxY: number = 0;
    let count: number = 0;

    for (let initYVel = y1; initYVel < Math.abs(y1); ++initYVel) {
        for (let initXVel = 0; initXVel < x2 + 1; ++initXVel) {
            let Vx = initXVel;
            let Vy = initYVel;

            let xCurr = 0; // Initial X potision
            let yCurr = 0; // Initial Y position

            let maxYPath = 0; // initial y position is set to 0

            for (let t = 0; t < 2 * Math.abs(y1) + 2; ++t) {
                // Position changes by velocity
                xCurr += Vx;
                yCurr += Vy;

                // Velocity changes for next step
                Vx = Math.max(0, Vx - 1);
                Vy -= 1;

                maxYPath = Math.max(maxYPath, yCurr);

                // check if hit the target
                if (xCurr >= x1 && xCurr <= x2 && yCurr >= y1 && yCurr <= y2) {
                    // HIT
                    maxY = Math.max(maxY, maxYPath);
                    count++;
                    break;
                }
            }
        }
    }

    return maxY;
}

function part2(input: string): number {
    let [[x1, x2], [y1, y2]] = input
        .trim()
        .split(":")[1]
        .trim()
        .split(",")
        .map((c) => c.split("=")[1].split("..").map(Number));

    let maxY: number = 0;
    let count: number = 0;

    for (let initYVel = y1; initYVel < Math.abs(y1); ++initYVel) {
        for (let initXVel = 0; initXVel < x2 + 1; ++initXVel) {
            let Vx = initXVel;
            let Vy = initYVel;

            let xCurr = 0; // Initial X potision
            let yCurr = 0; // Initial Y position

            let maxYPath = 0; // initial y position is set to 0

            for (let t = 0; t < 2 * Math.abs(y1) + 2; ++t) {
                // Position changes by velocity
                xCurr += Vx;
                yCurr += Vy;

                // Velocity changes for next step
                Vx = Math.max(0, Vx - 1);
                Vy -= 1;

                maxYPath = Math.max(maxYPath, yCurr);

                // check if hit the target
                if (xCurr >= x1 && xCurr <= x2 && yCurr >= y1 && yCurr <= y2) {
                    // HIT
                    maxY = Math.max(maxY, maxYPath);
                    count++;
                    break;
                }
            }
        }
    }
    return count;
}

function main(): void {
    const input: string = readFileSync(
        "../tests/sample_inputs/day_17_sample.txt"
    ).toString();
    console.log(part1(input));
    console.log(part2(input));
}

main();
