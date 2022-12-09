import { readFileSync } from "fs";

function part01_02(
  crates: { [key: number]: string[] },
  procedure: string[][],
  part01: boolean
): string {
  for (let line of procedure) {
    let [qnt, from, to] = [+line[1], +line[3], +line[5]];
    let tmp = crates[from].splice(-qnt, qnt);
    if (part01) tmp.reverse();
    crates[to].push(...tmp);
  }
  let message: string = "";
  Object.entries(crates).forEach(([_, value]) => {
    message += value.pop();
  });
  return message;
}

function processInput(stacks: string[]): { [key: number]: string[] } {
  const crates: { [key: number]: string[] } = {};
  for (let i = 0; i < stacks.length - 1; i++) {
    let index = 1;
    for (let j = 0; j < stacks[i].length; j += 4) {
      if (!(index in crates)) {
        crates[index] = [];
      }
      if (stacks[i].charAt(j + 1) !== " ") {
        crates[index].unshift(stacks[i].charAt(j + 1));
      }
      index++;
    }
  }
  return crates;
}

function day05(): void {
  const result: string[] = readFileSync("./input.txt", "utf-8").split("\n\n");
  const stacks: string[] = result[0].split("\n");
  const procedure: string[][] = result[1]
    .split("\n")
    .map((line) => line.split(" "));
  let crates = processInput(stacks);
  console.log(`Part 1: ${part01_02(crates, procedure, true)}`);
  crates = processInput(stacks);
  console.log(`Part 2: ${part01_02(crates, procedure, false)}`);
}

day05();
