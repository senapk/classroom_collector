var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);
var draft_exports = {};
module.exports = __toCommonJS(draft_exports);
function input() {
  let X = input;
  X.L = X.L || require("fs").readFileSync(0).toString().split(/\r?\n/);
  return X.L.shift();
}
function qtd_leds(v) {
  if (v == 1) return 2;
  if (v == 2) return 5;
  if (v == 3) return 5;
  if (v == 4) return 4;
  if (v == 5) return 5;
  if (v == 6) return 6;
  if (v == 7) return 3;
  if (v == 8) return 7;
  if (v == 9) return 6;
  return 6;
}
function main() {
  let qtd = +input();
  for (let i = 0; i < qtd; i++) {
    let painel = input();
    let count = 0;
    for (let j = 0; j < painel.length; j++) {
      count += qtd_leds(Number(painel[j]));
    }
    console.log(count, "leds");
  }
}
main();
