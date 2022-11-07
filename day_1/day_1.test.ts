import part1 from "./day1";
import { readFileSync } from "fs";

test("part1", function () {
    const sample_input = readFileSync("sample.txt").toString().split("\n");
    expect(part1(sample_input).toEqual(7));
});
