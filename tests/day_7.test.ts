import { readFileSync } from "fs";
import { part1, part2 } from "../src/day7";

describe("testing day_7 File", () => {
    const sample_input: string = readFileSync(
        "./sample_inputs/day_7_sample.txt"
    ).toString();
    const input: string = readFileSync("./inputs/day_7.txt").toString();
    test("part1 testing", () => {
        expect(part1(sample_input)).toEqual(37);
        console.log(`part1: ${part1(input)}`);
    });

    //Part 2 test
    test("part2 testing", () => {
        expect(part2(sample_input)).toEqual(168);
        console.log(`part2: ${part2(input)}`);
    });
});
