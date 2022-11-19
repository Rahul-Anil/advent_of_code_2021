import { readFileSync } from "fs";

function part1(input: string[]): number {
    let epsilon: string = "";
    let gamma: string = "";
    for (let j = 0; j < input[0].length; ++j) {
        let count_0 = 0;
        let count_1 = 0;
        for (let i = 0; i < input.length; ++i) {
            if (input[i][j] === "0") {
                count_0++;
            } else {
                count_1++;
            }
        }
        if (count_0 > count_1) {
            epsilon = epsilon.concat("0");
            gamma = gamma.concat("1");
        } else {
            gamma = gamma.concat("0");
            epsilon = epsilon.concat("1");
        }
    }

    let epsilonNum: number = parseInt(epsilon, 2);
    let gammaNum: number = parseInt(gamma, 2);
    return epsilonNum * gammaNum;
}

function part2(input: string[]): number {
    let o2: string[] = input;
    let co2: string[] = input;

    //O2
    let idx_o2 = 0;
    while (o2.length > 1) {
        let c0 = 0;
        let c1 = 0;
        let ones: string[] = [];
        let zeros: string[] = [];

        for (let i = 0; i < o2.length; ++i) {
            if (o2[i][idx_o2] === "0") {
                c0++;
                zeros.push(o2[i]);
            } else {
                c1++;
                ones.push(o2[i]);
            }
        }

        if (c0 > c1) {
            o2 = zeros;
        } else {
            o2 = ones;
        }
        idx_o2++;
    }

    const o2Num: number = parseInt(o2[0], 2);

    //CO2
    let idx_co2 = 0;
    while (co2.length > 1) {
        let c0 = 0;
        let c1 = 0;
        let ones: string[] = [];
        let zeros: string[] = [];

        for (let i = 0; i < co2.length; ++i) {
            if (co2[i][idx_co2] === "0") {
                c0++;
                zeros.push(co2[i]);
            } else {
                c1++;
                ones.push(co2[i]);
            }
        }

        if (c0 > c1) {
            co2 = ones;
        } else {
            co2 = zeros;
        }

        idx_co2++;
    }

    const co2Num: number = parseInt(co2[0], 2);

    console.log(`o2num: ${o2Num}, co2num: ${co2Num}`);
    return co2Num * o2Num;
}

export { part1, part2 };
