import { readFileSync } from "fs";

const hexToBin: Map<string, string> = new Map();
{
    readFileSync("day16_helper.txt")
        .toString()
        .trim()
        .split("\n")
        .map((lines) => lines.split(" = "))
        .map(([x, y]) => hexToBin.set(x, y));
}

class Packet {
    origin: string;
    packetVersion: number;
    packetId: number;
    literalValue?: number;
    operatorType?: number;
    childPackets;
    extraBits: string;

    constructor(binArr: string) {
        this.origin = binArr;
        this.packetVersion = parseInt(binArr.slice(0, 3), 2);
        this.packetId = parseInt(binArr.slice(3, 6), 2);
        this.childPackets = new Array();
        this.extraBits = "";

        this.display();

        const bin: string = binArr.slice(6);
        if (this.packetId === 4) {
            this.parseLiteral(bin);
        } else {
            this.operatorType = Number(bin[0]);
            if (this.operatorType === 0) {
                this.opType0(bin.slice(1));
            } else if (this.operatorType === 1) {
                this.opType1(bin.slice(1));
            }
        }
    }

    display(): void {
        console.log("\n");
        console.log(`ORIGIN: ${this.origin}`);
        console.log(`packet version: ${this.packetVersion}`);
        console.log(`packet id ${this.packetId}`);
        console.log("\n");
    }

    parseLiteral(bin: string): void {
        let stopBit: number = 1;
        let literalValBin: string = "";
        let idx = 0;

        while (stopBit === 1) {
            stopBit = Number(bin[idx]);
            literalValBin += bin.slice(idx + 1, idx + 5);
            idx += 5;
        }

        this.literalValue = parseInt(literalValBin, 2);
        this.extraBits = bin.slice(idx);
    }

    opType0(bin: string): void {
        let subPackLen: number = parseInt(bin.slice(0, 15), 2);
        let subPacket: string = bin.slice(15, 15 + subPackLen);

        while (parseInt(subPacket, 2)) {
            let newPacket = new Packet(subPacket);
            this.childPackets.push(newPacket);
            subPacket = newPacket.extraBits;
        }

        this.extraBits = bin.slice(15 + subPackLen);
    }

    opType1(bin: string): void {
        let numSubPackets = parseInt(bin.slice(0, 11), 2);
        let subPacket = bin.slice(11);
        for (let i = 0; i < numSubPackets; ++i) {
            let newPacket = new Packet(subPacket);
            this.childPackets.push(newPacket);
            subPacket = newPacket.extraBits;
        }
        this.extraBits = subPacket;
    }

    totalVersion(): number {
        let version: number = this.packetVersion;
        for (let c of this.childPackets) {
            version += c.totalVersion();
        }
        return version;
    }

    val(): number | undefined {
        if (this.packetId === 4) {
            let literalVal = this.literalValue;
            if (literalVal) {
                return literalVal;
            }
        }

        let childSubPacketVal = new Array();
        for (let c of this.childPackets) {
            childSubPacketVal.push(c.val());
        }

        if (this.packetId === 0) {
            return childSubPacketVal.reduce((acc, curr) => acc + curr);
        } else if (this.packetId === 1) {
            return childSubPacketVal.reduce((acc, curr) => acc * curr);
        } else if (this.packetId === 2) {
            return Math.min(...childSubPacketVal);
        } else if (this.packetId === 3) {
            return Math.max(...childSubPacketVal);
        } else if (this.packetId === 5) {
            if (childSubPacketVal[0] > childSubPacketVal[1]) {
                return 1;
            } else {
                return 0;
            }
        } else if (this.packetId === 6) {
            if (childSubPacketVal[0] < childSubPacketVal[1]) {
                return 1;
            } else {
                return 0;
            }
        } else if (this.packetId === 7) {
            if (childSubPacketVal[0] === childSubPacketVal[1]) {
                return 1;
            } else {
                return 0;
            }
        }
    }
}

function part1(input: string): number {
    let binRep = "";
    for (let i = 0; i < input.length; ++i) {
        binRep += hexToBin.get(input[i]);
    }

    const p = new Packet(binRep);
    console.log("P1");
    return p.totalVersion();
}

function part2(input: string): number | undefined {
    let binRep = "";
    for (let i = 0; i < input.length; ++i) {
        binRep += hexToBin.get(input[i]);
    }

    const p = new Packet(binRep);
    console.log("P2");
    let p2 = p.val();
    if (p2) {
        return p2;
    }
}

function main(): void {
    const input: string = readFileSync(
        "../tests/sample_inputs/day_16_sample.txt"
    ).toString();
    console.log(part1(input));
    console.log(part2(input));
}

main();
