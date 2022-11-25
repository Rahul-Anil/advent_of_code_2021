import { read, readFile, readFileSync } from "fs";

function part1(input: string): number {
    let [p1, p2] = input.trim().split("\n\n");
    let polymer: string[] = p1.trim().split("");
    const template: Record<string, string> = {};
    p2.trim()
        .split("\n")
        .map((line) => line.trim().split(" -> "))
        .map(([from, to]) => {
            template[from] = to;
        });

    //10 steps
    for (let s = 0; s < 10; ++s) {
        let newPolymer: string[] = [];
        newPolymer.push(polymer[0]);
        for (let i = 0; i < polymer.length - 1; ++i) {
            let pair = polymer[i] + polymer[i + 1];
            if (template[pair]) {
                newPolymer.push(template[pair]);
                newPolymer.push(polymer[i + 1]);
            }
        }
        polymer = newPolymer;
    }

    const counter: Map<string, number> = new Map();
    for (let i = 0; i < polymer.length; ++i) {
        if (!counter.get(polymer[i])) {
            counter.set(polymer[i], 1);
        } else {
            //console.log("HERE");
            let v = counter.get(polymer[i]);
            if (v) {
                let c: number = v;
                c++;
                counter.set(polymer[i], c);
            }
        }
    }

    const min: number = Math.min(...counter.values());
    const max: number = Math.max(...counter.values());

    return max - min;
}

function nIncrement(m: Map<string, number>, a: string): void {
    if (!m.get(a)) {
        m.set(a, 1);
    } else {
        let v = m.get(a);
        if (v) {
            let c: number = v;
            c++;
            m.set(a, c);
        }
    }
}

function setMapVal(m: Map<string, number>, k: string, v: number): void {
    if (!m.get(k)) {
        m.set(k, v);
    } else {
        let val = m.get(k);
        if (val) {
            let newVal: number = val + v;
            m.set(k, newVal);
        }
    }
}

function part2(input: string): number {
    let [p1, p2] = input.trim().split("\n\n");
    let polymer: string[] = p1.trim().split("");
    const template: Record<string, string> = {};
    p2.trim()
        .split("\n")
        .map((line) => line.trim().split(" -> "))
        .map(([from, to]) => {
            template[from] = to;
        });

    let pairs: string[] = [];
    for (let i = 0; i < polymer.length - 1; ++i) {
        pairs.push(polymer[i] + polymer[i + 1]);
    }

    let pairCounter: Map<string, number> = new Map();
    for (let i = 0; i < pairs.length; ++i) {
        nIncrement(pairCounter, pairs[i]);
    }

    for (let s = 0; s < 40; ++s) {
        let newPairs: Map<string, number> = new Map();
        for (let [key, val] of pairCounter) {
            let newEle = template[key];
            let k1 = key[0] + newEle;
            let k2 = newEle + key[1];
            setMapVal(newPairs, k1, val);
            setMapVal(newPairs, k2, val);
        }
        pairCounter = newPairs;
    }

    let elementCounter: Map<string, number> = new Map();
    setMapVal(elementCounter, polymer[polymer.length - 1], 1);
    for (let [key, val] of pairCounter) {
        let k1 = key[0];
        setMapVal(elementCounter, k1, val);
    }
    const min: number = Math.min(...elementCounter.values());
    const max: number = Math.max(...elementCounter.values());

    return max - min;
}
function main(): void {
    const input: string = readFileSync(
        "/home/pakru/garchomp/projects/advent_of_code_2021/tests/sample_inputs/day_14_sample.txt"
    ).toString();
    console.log(part1(input));
    console.log(part2(input));
}

main();
