import { readFileSync } from "fs";

function part1(input: string): number {
    const output: string[][] = input
        .trim()
        .split("\n")
        .map((line) => line.split("|")[1].trim().split(" "));
    let sum: number = 0;
    type length = number;
    const uniqNum: Map<length, number> = new Map();
    uniqNum.set(2, 1);
    uniqNum.set(4, 4);
    uniqNum.set(3, 7);
    uniqNum.set(7, 8);
    for (let i = 0; i < output.length; ++i) {
        for (let j = 0; j < output[i].length; ++j) {
            if (uniqNum.has(output[i][j].length)) {
                sum++;
            }
        }
    }
    return sum;
}

function sortString(s: string): string {
    return s.split("").sort().join("");
}

function stringAinB(A: string, B: string): boolean {
    return A.split("").every((element) => B.split("").includes(element));
}

function part2(input: string): number {
    const output: string[][] = input
        .trim()
        .split("\n")
        .map((line) => line.split("|")[1].trim().split(" "));
    const signal: string[][] = input
        .trim()
        .split("\n")
        .map((line) => line.split("|")[0].trim().split(" "));

    let sum: number = 0;
    type length = number;
    const uniqNum: Map<length, number> = new Map();
    uniqNum.set(2, 1);
    uniqNum.set(4, 4);
    uniqNum.set(3, 7);
    uniqNum.set(7, 8);
    for (let i = 0; i < signal.length; ++i) {
        // stores pattern for a segment
        const segmentMaps = new Map();
        const reverseSegmentMaps = new Map();

        // get the patterns for unq line segment
        for (let j = 0; j < signal[i].length; ++j) {
            if (uniqNum.has(signal[i][j].length)) {
                let P = sortString(signal[i][j]);
                segmentMaps.set(uniqNum.get(signal[i][j].length), P);
                reverseSegmentMaps.set(P, uniqNum.get(signal[i][j].length));
            }
        }

        // 6 length segmented values: 6, 9, 0
        // get 6
        for (let j = 0; j < signal[i].length; ++j) {
            if (
                signal[i][j].length === 6 &&
                segmentMaps.get(1) &&
                !stringAinB(segmentMaps.get(1), signal[i][j])
            ) {
                let P = sortString(signal[i][j]);
                segmentMaps.set(6, P);
                reverseSegmentMaps.set(P, 6);
            }
        }

        // get 9
        for (let j = 0; j < signal[i].length; ++j) {
            if (
                signal[i][j].length === 6 &&
                segmentMaps.get(4) &&
                stringAinB(segmentMaps.get(4), signal[i][j]) &&
                !reverseSegmentMaps.has(sortString(signal[i][j]))
            ) {
                let P = sortString(signal[i][j]);
                segmentMaps.set(9, P);
                reverseSegmentMaps.set(P, 9);
            }
        }

        //get 0
        for (let j = 0; j < signal[i].length; ++j) {
            if (
                signal[i][j].length === 6 &&
                !reverseSegmentMaps.has(sortString(signal[i][j]))
            ) {
                let P = sortString(signal[i][j]);
                segmentMaps.set(0, P);
                reverseSegmentMaps.set(P, 0);
            }
        }

        // 5 length segmented values: 2, 3, 5
        // get 2
        for (let j = 0; j < signal[i].length; ++j) {
            if (
                signal[i][j].length === 5 &&
                segmentMaps.get(9) &&
                !stringAinB(signal[i][j], segmentMaps.get(9))
            ) {
                let P = sortString(signal[i][j]);
                segmentMaps.set(2, P);
                reverseSegmentMaps.set(P, 2);
            }
        }

        // get 3
        for (let j = 0; j < signal[i].length; ++j) {
            if (
                signal[i][j].length === 5 &&
                segmentMaps.get(1) &&
                stringAinB(segmentMaps.get(1), signal[i][j]) &&
                !reverseSegmentMaps.has(sortString(signal[i][j]))
            ) {
                let P = sortString(signal[i][j]);
                segmentMaps.set(3, P);
                reverseSegmentMaps.set(P, 3);
            }
        }

        // get 5
        for (let j = 0; j < signal[i].length; ++j) {
            if (
                signal[i][j].length === 5 &&
                !reverseSegmentMaps.has(sortString(signal[i][j]))
            ) {
                let P = sortString(signal[i][j]);
                segmentMaps.set(5, P);
                reverseSegmentMaps.set(P, 5);
            }
        }

        let numString: string = "";
        for (let k = 0; k < output[i].length; ++k) {
            if (reverseSegmentMaps.has(sortString(output[i][k]))) {
                numString = numString.concat(
                    reverseSegmentMaps.get(sortString(output[i][k])).toString()
                );
            }
        }
        sum += Number(numString);
    }

    return sum;
}

function main(): void {
    const input: string = readFileSync(
        "../tests/sample_inputs/day_8_sample.txt"
    ).toString();
    console.log(part1(input));
    console.log(part2(input));
}

export { part1, part2 };

main();
