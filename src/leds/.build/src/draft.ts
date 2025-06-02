function input(): string { let X: any = input; X.L = X.L || require("fs").readFileSync(0).toString().split(/\r?\n/); return X.L.shift(); } export {};

function qtd_leds(v: number): number {
    if (v == 1) return 2;
    if (v == 2) return 5;
    if (v == 3) return 5;
    if (v == 4) return 4;
    if (v == 5) return 5;
    if (v == 6) return 6;
    if (v == 7) return 3;
    if (v == 8) return 7;
    if (v == 9) return 5;
    return 6;
}

function main() {
    let qtd = +input();
    for (let i = 0; i < qtd; i++) {
        let painel: string = input();
        let count = 0;
        for (let j = 0; j < painel.length; j++) {
            count += qtd_leds(Number(painel[j]))
        }
        console.log(count, "leds");
    }
}
main();
