import { readFileSync } from "fs";

const SYMBOL_SCORE = {
  A: {
    X: 3 + 1,
    Y: 6 + 2,
    Z: 0 + 3,
  },
  B: {
    X: 0 + 1,
    Y: 3 + 2,
    Z: 6 + 3,
  },
  C: {
    X: 6 + 1,
    Y: 0 + 2,
    Z: 3 + 3,
  },
};

const SHAPE_TO_CHOOSE = {
  A: {
    X: "Z",
    Y: "X",
    Z: "Y",
  },
  B: {
    X: "X",
    Y: "Y",
    Z: "Z",
  },
  C: {
    X: "Y",
    Y: "Z",
    Z: "X",
  },
};

function part01(rounds: string[][]) {
  let score = 0;
  for (let r of rounds) {
    let [symbol1, symbol2] = r;
    score += SYMBOL_SCORE[symbol1][symbol2];
  }
  return score;
}

function part02(rounds: string[][]): number {
  let score = 0;
  for (let r of rounds) {
    let [symbol1, symbol2] = r;
    symbol2 = SHAPE_TO_CHOOSE[symbol1][symbol2];
    score += SYMBOL_SCORE[symbol1][symbol2];
  }
  return score;
}

function day02(): void {
  const result: string[] = readFileSync("./input.txt", "utf-8").split("\n");
  let rounds: string[][] = result.map((r) => r.split(" "));
  console.log(`Part 1: ${part01(rounds)}`);
  console.log(`Part 2: ${part02(rounds)}`);
}

day02();
