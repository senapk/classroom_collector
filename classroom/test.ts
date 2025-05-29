import { execSync } from 'child_process';
import * as fs from 'fs'; // Importa o módulo 'fs'

let passed = 0;
let total = 0;
let diff_showed = false;

console.log(
    '\n\n---------------------------\n\n🔍 Iniciando verificação da atividade...\n'
);

function save_file(path: string, content: string) {
    try {
        fs.writeFileSync(path, content);
    } catch (error) {
        console.error(`Erro ao escrever no arquivo (Síncrono): ${error}`);
    }
}
function remove_file(path: string) {
    if (fs.existsSync(path)) {
        // Verifica se o arquivo existe antes de tentar apagar
        fs.unlinkSync(path);
    }
}
function show_diff(content_a: string, content_b: string) {
    if (diff_showed) {
        return;
    }
    diff_showed = true;
    let file_a = '.debug_a.txt';
    let file_b = '.debug_b.txt';
    save_file(file_a, content_a);
    save_file(file_b, content_b);
    console.log(
        execSync(`tko -w 140 diff -d --path ${file_a} ${file_b}`).toString()
    );
    remove_file(file_a);
    remove_file(file_b);
}

// Teste 1: Verifica o main.ts
try {
    total += 1;
    // testa primeiro se roda
    const saidaEsperada = 'Ser ou não ser, eis a questão';
    const output = execSync('npm run build').toString();
    if (output.toString().includes(saidaEsperada)) {
        passed++;
        console.log('✅ main.ts: Saída em texto do código é a esperada.');
    } else {
        console.log('❌ main.ts: Saída em texto do código não é a esperada.');
        show_diff(saidaEsperada, output);
    }
} catch (e) {
    console.log('❌ main.ts: Erro: ' + e.message);
}

// Teste 2: Verifica o extra1.ts
try {
    total += 1;
    // testa primeiro se roda
    const saidaEsperada =
        'Comprimento do trecho: 18\n' +
        'Índice do trecho: 25\n' +
        'Frase revisada: Eu não gosto de spoilers';

    const output = execSync('npx tsx src/extra1.ts').toString();
    if (output.toString().includes(saidaEsperada)) {
        passed++;
        console.log('✅ extra1.ts: Saída em texto do código é a esperada.');
    } else {
        console.log('❌ extra1.ts: Saída em texto do código não é a esperada.');
        show_diff(saidaEsperada, output);
    }
} catch (e) {
    console.log('❌ extra1.ts: Erro: ' + e.message);
}

// Teste 3: Verifica o extra2.ts
try {
    total += 1;
    // testa primeiro se roda
    const saidaEsperada =
        'Se um triângulo tem lados de 9 e 12, então a hipotenusa mede 15.';

    const output = execSync('npx tsx src/extra2.ts').toString();
    if (output.toString().includes(saidaEsperada)) {
        passed++;
        console.log('✅ extra2.ts: Saída em texto do código é a esperada.');
    } else {
        console.log('❌ extra2.ts: Saída em texto do código não é a esperada.');
        show_diff(saidaEsperada, output);
    }
} catch (e) {
    console.log('❌ extra2.ts: Erro: ' + e.message);
}

// Teste 4: Verifica o extra3.ts
try {
    total += 1;
    // testa primeiro se roda
    const saidaEsperadaExtra3 = /Eu não gosto de (.+?)\./i;
    const output = execSync('npx tsx src/extra3.ts').toString();
    if (output.toString().search(saidaEsperadaExtra3) >= 0) {
        passed++;
        console.log('✅ extra3.ts: Saída em texto do código é a esperada.');
    } else {
        console.log('❌ extra3.ts: Saída em texto do código não é a esperada.');
    }
} catch (e) {
    console.log('❌ extra3.ts: Erro: ' + e.message);
}

// Teste 5: Media

function run_tko(folder: string) {
    try {
        total += 1;
        // testa primeiro se roda
        const output = execSync(
            `tko run -d ${folder}/cases.tio ${folder}/draft.ts`
        ).toString();
        let lines = output.split('\n');
        if (output.split('\n').length === 3) {
            passed++;
            console.log(`✅ ${folder}: Saída em texto do código é a esperada.`);
            console.log(
                lines
                    .slice(1, -1)
                    .map((x) => '   ' + x)
                    .join('\n')
            );
        } else {
            console.log(
                `❌ ${folder}: Saída em texto do código não é a esperada.`
            );
            if (!diff_showed) {
                diff_showed = true;
                console.log(
                    lines
                        .slice(1, -1)
                        .map((x) => '   ' + x)
                        .join('\n')
                );
            }
        }
    } catch (e) {
        console.log(`❌ ${folder}: Erro: ` + e.message);
    }
}

run_tko('src/media');
run_tko('src/leds');
run_tko('src/traficantes');
// Resultado final
console.log(
    `\n\n🎯 Resultado: ${passed}/${total} testes passaram.` +
        '\n\n---------------------------\n\n'
);

// Código de saída para GitHub Classroom
process.exit(passed === total ? 0 : 1);
