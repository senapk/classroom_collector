function input(): string { let X: any = input; X.L = X.L || require("fs").readFileSync(0).toString().split(/\r?\n/); return X.L.shift(); } export {};

function main() {
    let a = +input()
    let b = +input()
    console.log(((a+b)/2).toFixed(1))
}
main();
