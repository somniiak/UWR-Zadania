import fs from 'fs';

fs.readFile('./book.txt', (err, data) => {
    if (err)
        throw err;
    else
        console.log(data.toString());
})
