import { readFileSync } from "fs";

function part1(input: string): number {
    let score = 0;
    const syntax: string[][] = input
        .trim()
        .split("\n")
        .map((line) => line.trim().split(""));

    const syntaxScore = new Map();
    syntaxScore.set(")", 3);
    syntaxScore.set("]", 57);
    syntaxScore.set("}", 1197);
    syntaxScore.set(">", 25137);

    const openToClose: Map<string, string> = new Map();
    openToClose.set("(", ")");
    openToClose.set("[", "]");
    openToClose.set("{", "}");
    openToClose.set("<", ">");

    const closeToOpen: Map<string, string> = new Map();
    closeToOpen.set(")", "(");
    closeToOpen.set("]", "[");
    closeToOpen.set("}", "{");
    closeToOpen.set(">", "<");

    for (let i = 0; i < syntax.length; ++i) {
        let b: string[] = [];
        for (let j = 0; j < syntax[i].length; ++j) {
            if (openToClose.has(syntax[i][j])) {
                b.push(syntax[i][j]);
            } else {
                let openBracket = b.pop();
                if (openBracket !== closeToOpen.get(syntax[i][j])) {
                    score += syntaxScore.get(syntax[i][j]);
                    break;
                }
            }
        }
    }

    return score;
}

function part2(input: string): number {
    let scoreList: number[] = [];
    const syntax: string[][] = input
        .trim()
        .split("\n")
        .map((line) => line.trim().split(""));

    const syntaxScore = new Map();
    syntaxScore.set("(", 1);
    syntaxScore.set("[", 2);
    syntaxScore.set("{", 3);
    syntaxScore.set("<", 4);

    const openToClose: Map<string, string> = new Map();
    openToClose.set("(", ")");
    openToClose.set("[", "]");
    openToClose.set("{", "}");
    openToClose.set("<", ">");

    const closeToOpen: Map<string, string> = new Map();
    closeToOpen.set(")", "(");
    closeToOpen.set("]", "[");
    closeToOpen.set("}", "{");
    closeToOpen.set(">", "<");

    for (let i = 0; i < syntax.length; ++i) {
        let bracket: string[] = [];
        let invalidBracket: boolean = false;
        for (let j = 0; j < syntax[i].length; ++j) {
            if (openToClose.has(syntax[i][j])) {
                bracket.push(syntax[i][j]);
            } else {
                let openBracket = bracket.pop();
                if (openBracket !== closeToOpen.get(syntax[i][j])) {
                    invalidBracket = true;
                    break;
                }
            }
        }

        if (!invalidBracket) {
            bracket.reverse();
            let score: number = 0;
            for (let k = 0; k < bracket.length; ++k) {
                score *= 5;
                score += syntaxScore.get(bracket[k]);
            }

            scoreList.push(score);
        }
    }
    scoreList.sort((a, b) => a - b);
    let midIdx = Math.floor(scoreList.length / 2);
    return scoreList[midIdx];
}

function main(): void {
    const input: string = readFileSync(
        "../tests/sample_inputs/day_10_sample.txt"
    ).toString();
    console.log(part1(input));
    console.log(part2(input));
}

main();

export { part1, part2 };
