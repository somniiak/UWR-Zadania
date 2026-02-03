import fs from 'fs';
import util from 'util';

// Klasyczny interfejs (callback)
fs.readFile('book.txt', 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log('CALLBACK', data);
  }
});


// Ręcznie zwracamy promise
function readFilePromise(path) {
    return new Promise((resolve, reject) => {
        fs.readFile(path, 'utf-8', (err, data) => {
            if (err) {
                reject(err);
            } else {
                resolve(data);
            }
        });
    });
}

readFilePromise('book.txt', 'utf8')
  .then(data => console.log('PROMISE THEN', data))
  .catch(err => console.error(err));

(async () => {
    try {
        const data = await readFilePromise('book.txt', 'utf8');
        console.log('PROMISE ASYNC', data);
    } catch(err) {
        console.error(err);
    }
})();


// util.promisify
const readFileUtilPromisify = util.promisify(fs.readFile);

readFileUtilPromisify('book.txt', 'utf-8')
  .then(data => console.log('UTIL PROMISIFY', data))
  .catch(err => console.error(err));


// fs.promises
fs.promises.readFile('book.txt', 'utf-8')
  .then(data => console.log('FS PROMISES', data))
  .catch(err => console.error(err));