"use strict";
exports.__esModule = true;
var fs_1 = require("fs");
var input = (0, fs_1.readFileSync)("input.txt")
    .toString()
    .split("\n")
    .map(Number);
var increasedCount = 0;
for (var i = 1; i < input.length; ++i) {
    if (input[i - 1] < input[i]) {
        increasedCount++;
    }
}
console.log(increasedCount);
