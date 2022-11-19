import { readFileSync } from "fs";
import { part1, part2 } from "../src/day4";

describe("testing day_4 File", () => {
    const sample_input: string = readFileSync(
        "./sample_inputs/day_4_sample.txt"
    ).toString();
    const input: string = readFileSync("./inputs/day_4.txt").toString();
    test("part1 testing", () => {
        expect(part1(sample_input)).toEqual(4512);
        console.log(`part1: ${part1(input)}`);
    });

    //Part 2 test
    test("part2 testing", () => {
        expect(part2(sample_input)).toEqual(1924);
        console.log(`part2: ${part2(input)}`);
    });
});
