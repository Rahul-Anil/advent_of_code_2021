import { readFileSync } from "fs";
import { part1, part2 } from "../src/day9";

describe("testing day_9 File", () => {
    const sample_input: string = readFileSync(
        "./sample_inputs/day_9_sample.txt"
    ).toString();
    const input: string = readFileSync("./inputs/day_9.txt").toString();
    test("part1 testing", () => {
        expect(part1(sample_input)).toEqual(15);
        console.log(`part1: ${part1(input)}`);
    });

    //Part 2 test
    test("part2 testing", () => {
        expect(part2(sample_input)).toEqual(1134);
        console.log(`part2: ${part2(input)}`);
    });
});
