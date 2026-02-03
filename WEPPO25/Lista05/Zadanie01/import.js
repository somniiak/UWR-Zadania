import { add, sub } from "./esm_export.mjs"
import chalk from "chalk"

console.log(chalk.bgYellow.bold("===   ESM    ==="));
console.log("1 + 2 = " + add(1, 2));
console.log("1 - 2 = " + sub(1, 2) + "\n");


const colors = require("colors");
const cjs = require("./cjs_export.js")

console.log(colors.bgGreen.bold("=== CommonJS ==="));
console.log("1 + 2 = " + cjs.add(1, 2));
console.log("1 - 2 = " + cjs.sub(1, 2) + "\n");
