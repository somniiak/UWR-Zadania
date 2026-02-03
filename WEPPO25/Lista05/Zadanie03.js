import readline from 'readline';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

var number = Math.floor(Math.random() * 101);

function ask() {
    rl.question(
        'Podaj wartość od 0 do 100: ',
        (answer) => {
            if (answer < 0 || answer > 100) {
                console.log('Wartość poza wymaganym zakresem!\n');
                ask();
            }
            else if (answer < number) {
                console.log('Za mało!\n');
                ask();
            }
            else if (answer > number) {
                console.log('Za dużo!\n');
                ask();
            }
            else {
                console.log('Odgadnięto liczbę ' + number + '!');
                rl.close();
            }
        }
    );
}

ask()
