import https from 'https';

// https://stackoverflow.com/a/47986626

function fetch(url) {
    return new Promise((resolve, reject) => {
        https.get(url, (res) => {
            let status = res.statusCode;

            if (status != 200) {
                reject(new Error(
                    `Request failed with status code: ${status}`));
                // consume response data to free up memory
                res.resume();
            }

            res.setEncoding('utf8');
            let rawData = '';

            res.on('data', (chunk) => {
                rawData += chunk;
            });
            res.on('end', () => {
                resolve(rawData);
            });
        }).on('error', (e) => {
            reject(new Error(
                `Got error: ${e.message}`));
        });;
    });
}

fetch('https://mccd.space/posts/ocaml-the-worlds-best/')
    .then(response => {
        console.log(response)
    })
    .catch(error => {
        console.error(error)
    });