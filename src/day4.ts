import { readFileSync } from "fs";

class Board {
    public board: number[][];
    public bingoMark: number[][];

    constructor() {
        this.board = new Array(5).fill(0).map(() => new Array(5).fill(0));
        this.bingoMark = new Array(5).fill(1).map(() => new Array(5).fill(1));
    }

    fillBoard(board: number[][]): void {
        this.board = board;
    }

    markBingo(bingoNumber: number): void {
        this.board.forEach((row, rowIdx) => {
            row.forEach((val, valIdx) => {
                if (val === bingoNumber) {
                    this.bingoMark[rowIdx][valIdx] = 0;
                }
            });
        });
    }

    isBingo(): boolean {
        //Check rows
        for (let i = 0; i < this.bingoMark.length; ++i) {
            if (this.bingoMark[i].every((value) => value === 0)) {
                return true;
            }
        }

        //Check cols
        for (let i = 0; i < this.bingoMark[0].length; ++i) {
            if (this.bingoMark.map((v) => v[i]).every((value) => value === 0)) {
                return true;
            }
        }

        return false;
    }

    bingoScore(bingoNumber: number): number {
        let sum = 0;
        for (let i = 0; i < this.board.length; ++i) {
            for (let j = 0; j < this.board[0].length; ++j) {
                sum += this.board[i][j] * this.bingoMark[i][j];
            }
        }

        return sum * bingoNumber;
    }
}

function bingoScore(
    boardMap: Map<number, Board>,
    bingoNumber: number[]
): number {
    for (let i = 0; i < bingoNumber.length; ++i) {
        for (let j = 0; j < boardMap.size; ++j) {
            let board = boardMap.get(j);
            if (board) {
                board.markBingo(bingoNumber[i]);
                if (board.isBingo()) {
                    return board.bingoScore(bingoNumber[i]);
                }
            }
        }
    }

    return -1;
}

function letSquidWin(boardMap: Map<number, Board>, bingoNumber: number[]) {
    let winningOrder: number[] = [];
    let winningValue: number[] = [];
    while (winningOrder.length < boardMap.size) {
        for (let i = 0; i < bingoNumber.length; ++i) {
            for (let j = 0; j < boardMap.size; ++j) {
                let board = boardMap.get(j);
                if (board) {
                    board.markBingo(bingoNumber[i]);
                    if (board.isBingo()) {
                        if (!winningOrder.includes(j)) {
                            winningOrder.push(j);
                            winningValue.push(board.bingoScore(bingoNumber[i]));
                        }
                    }
                }
            }
        }
    }

    return winningValue[winningValue.length - 1];
}

function part1(input: string): number {
    const bingoNumber: number[] = input
        .split("\n")[0]
        .trim()
        .split(",")
        .map(Number);

    const bingoBoard: number[][][] = input
        .trim()
        .split("\n")
        .splice(2)
        .join("\n")
        .split("\n\n")
        .map((board) => {
            return board
                .split("\n")
                .map((row) => row.trim().split(/\s+/).map(Number));
        });

    const boardMap: Map<number, Board> = new Map();
    for (let i = 0; i < bingoBoard.length; ++i) {
        boardMap.set(i, new Board());
        let board = boardMap.get(i);
        if (board) {
            board.fillBoard(bingoBoard[i]);
        }
    }

    const solution1: number = bingoScore(boardMap, bingoNumber);
    return solution1;
}

function part2(input: string): number {
    const bingoNumber: number[] = input
        .split("\n")[0]
        .trim()
        .split(",")
        .map(Number);

    const bingoBoard: number[][][] = input
        .trim()
        .split("\n")
        .splice(2)
        .join("\n")
        .split("\n\n")
        .map((board) => {
            return board
                .split("\n")
                .map((row) => row.trim().split(/\s+/).map(Number));
        });

    const boardMap: Map<number, Board> = new Map();
    for (let i = 0; i < bingoBoard.length; ++i) {
        boardMap.set(i, new Board());
        let board = boardMap.get(i);
        if (board) {
            board.fillBoard(bingoBoard[i]);
        }
    }

    const solution2: number = letSquidWin(boardMap, bingoNumber);
    return solution2;
}

function main(): void {
    const input: string = readFileSync(
        "../tests/sample_inputs/day_4_sample.txt"
    ).toString();
    console.log(part1(input));
    console.log(part2(input));
}

main();

export { part1, part2 };
