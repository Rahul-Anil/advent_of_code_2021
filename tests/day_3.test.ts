import { readFileSync } from "fs";
import { part1, part2 } from "../src/day3";

describe("testing day_3 File", () => {
    const sample_input: string[] = readFileSync(
        "./sample_inputs/day_3_sample.txt"
    )
        .toString()
        .trim()
        .split("\n");
    const input: string[] = readFileSync("./inputs/day_3.txt")
        .toString()
        .trim()
        .split("\n");
    test("part1 testing", () => {
        expect(part1(sample_input)).toEqual(198);
        console.log(`part1: ${part1(input)}`);
    });

    //Part 2 test
    test("part2 testing", () => {
        expect(part2(sample_input)).toEqual(230);
        console.log(`part2: ${part2(input)}`);
    });
});
