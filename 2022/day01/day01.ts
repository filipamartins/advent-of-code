import { readFileSync } from "fs";

function getElvesSums(elves: number[][]): number[] {
  return elves.map((elf) => elf.reduce((a, b) => a + b, 0));
}

function part01(elves: number[][]): number {
  let elvesSums = getElvesSums(elves);
  return Math.max(...elvesSums);
}

function part02(elves: number[][]): number {
  let elvesSums = getElvesSums(elves);
  return elvesSums
    .sort((a, b) => b - a)
    .slice(0, 3)
    .reduce((a, b) => a + b, 0);
}

function day01(): void {
  const result: string[] = readFileSync("./input.txt", "utf-8").split("\n\n");
  const elves: number[][] = result.map((elf) =>
    elf.split("\n").map((str) => parseInt(str))
  );
  console.log(`Part 1: ${part01(elves)}`);
  console.log(`Part 2: ${part02(elves)}`);
}

day01();
