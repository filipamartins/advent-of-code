import { readFileSync } from "fs";

function part01(pairs: string[][]): number {
  let sum: number = 0;
  for (let p of pairs) {
    const [p1, p2]: string[][] = p.map((elf) => elf.split("-"));
    const [n1, n2, n3, n4] = [+p1[0], +p1[1], +p2[0], +p2[1]];
    if ((n1 <= n3 && n2 >= n4) || (n3 <= n1 && n4 >= n2)) {
      sum += 1;
    }
  }
  return sum;
}

function part02(pairs: string[][]): number {
  let sum: number = 0;
  for (let p of pairs) {
    const [p1, p2]: string[][] = p.map((elf) => elf.split("-"));
    const [n1, n2, n3, n4] = [+p1[0], +p1[1], +p2[0], +p2[1]];
    if (n1 <= n4 && n3 <= n2) sum += 1;
  }
  return sum;
}

function day04(): void {
  const result: string[][] = readFileSync("./input.txt", "utf-8")
    .split("\n")
    .map((str) => str.split(","));
  console.log(`Part 1: ${part01(result)}`);
  console.log(`Part 2: ${part02(result)}`);
}

day04();
