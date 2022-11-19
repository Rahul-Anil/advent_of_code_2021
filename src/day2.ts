function part1(input: string[]): number {
    let depth: number = 0;
    let h_pos: number = 0;

    for (let i = 0; i < input.length; ++i) {
        let [mov, pos] = [
            input[i].split(" ")[0],
            Number(input[i].split(" ")[1]),
        ];

        if (mov === "forward") {
            h_pos += pos;
        } else if (mov === "down") {
            depth += pos;
        } else {
            depth -= pos;
        }
    }

    return depth * h_pos;
}

function part2(input: string[]): number {
    let depth: number = 0;
    let h_pos: number = 0;
    let aim: number = 0;

    for (let i = 0; i < input.length; ++i) {
        let [mov, pos] = [
            input[i].split(" ")[0],
            Number(input[i].split(" ")[1]),
        ];

        if (mov === "forward") {
            h_pos += pos;
            depth += aim * pos;
        } else if (mov === "down") {
            aim += pos;
        } else {
            aim -= pos;
        }
    }

    return depth * h_pos;
}

export { part1, part2 };
