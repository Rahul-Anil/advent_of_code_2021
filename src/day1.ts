function part1(input: string[]): number {
    const inputNum: number[] = input.map(Number);

    let increasedCount: number = 0;
    for (let i = 1; i < inputNum.length; ++i) {
        if (inputNum[i - 1] < inputNum[i]) {
            increasedCount++;
        }
    }

    return increasedCount;
}

function part2(input: string[]): number {
    const inputNum: number[] = input.map(Number);

    let increasedCount: number = 0;
    for (let i = 3; i < inputNum.length; ++i) {
        if (inputNum[i] > inputNum[i - 3]) {
            increasedCount++;
        }
    }
    return increasedCount;
}

export { part1, part2 };
