import readline from 'readline';
import fs from 'fs';

// https://stackoverflow.com/a/32599033

async function processLineByLine(file, count=3) {
    const fileStream = fs.createReadStream(file);

    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity,
    });

    const dict = {}
    const re = /^\d\d:\d\d:\d\d (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) (GET|POST) \S+ \d{3}$/;

    for await (const line of rl) {
        let match = re.exec(line);
        if (!match) continue;
        const key = match[1];
        dict[key] = (dict[key] || 0) + 1;
    }

    const sorted = Object.entries(dict)
      .sort(([, countA], [, countB]) => countB - countA)
      .slice(0, count);

    return sorted;
}

processLineByLine('server.log', 3)
    .then((res) => {
        res.forEach(([ip, count], index) => {
            console.log(`${index + 1}. ${ip}: ${count} requests`);
        });
    })
    .catch((err) => {
        console.error('Error processing file:', err);
    });