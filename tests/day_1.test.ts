import { readFileSync } from "fs";
import { part1, part2 } from "../src/day1";

describe("testing day1 File", () => {
    const sample_input: string[] = readFileSync(
        "./sample_inputs/day_1_sample.txt"
    )
        .toString()
        .split("\n");
    const input: string[] = readFileSync("./inputs/day_1.txt")
        .toString()
        .split("\n");
    test("part1 testing", () => {
        expect(part1(sample_input)).toEqual(7);
        console.log(`part1: ${part1(input)}`);
    });

    //Part 2 test
    test("part2 testing", () => {
        expect(part2(sample_input)).toEqual(5);
        console.log(`part2: ${part2(input)}`);
    });
});
