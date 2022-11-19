import { readFileSync } from "fs";
import { part1, part2 } from "../src/day2";

describe("testing day_2 File", () => {
    const sample_input: string[] = readFileSync(
        "./sample_inputs/day_2_sample.txt"
    )
        .toString()
        .trim()
        .split("\n");
    const input: string[] = readFileSync("./inputs/day_2.txt")
        .toString()
        .trim()
        .split("\n");
    test("part1 testing", () => {
        expect(part1(sample_input)).toEqual(150);
        console.log(`part1: ${part1(input)}`);
    });

    //Part 2 test
    test("part2 testing", () => {
        expect(part2(sample_input)).toEqual(900);
        console.log(`part2: ${part2(input)}`);
    });
});
