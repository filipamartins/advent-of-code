import { readFileSync } from "fs";

function charPriority(c: string): number {
  const charCode: number = c.charCodeAt(0);
  return c.toLowerCase() === c
    ? charCode - "a".charCodeAt(0) + 1
    : charCode - "A".charCodeAt(0) + 27;
}

function part01(rucksacks: string[]): number {
  let priority = 0;
  for (let r of rucksacks) {
    const fRucksack: string = r.slice(0, r.length / 2);
    const sRucksack: string = r.slice(r.length / 2, r.length);
    const repeatedChar: string = fRucksack
      .split("")
      .filter((char) => sRucksack.includes(char))[0];
    priority += charPriority(repeatedChar);
  }
  return priority;
}

function part02(rucksacks: string[]): number {
  let priority = 0;
  for (let i = 0; i < rucksacks.length; i += 3) {
    const repeatedChars: string[] = rucksacks[i]
      .split("")
      .filter((char) => rucksacks[i + 1].includes(char));
    const repeatedChar: string = repeatedChars.filter((char) =>
      rucksacks[i + 2].includes(char)
    )[0];
    priority += charPriority(repeatedChar);
  }
  return priority;
}

function day03(): void {
  const result: string[] = readFileSync("./input.txt", "utf-8").split("\n");
  console.log(`Part 1: ${part01(result)}`);
  console.log(`Part 2: ${part02(result)}`);
}

day03();
