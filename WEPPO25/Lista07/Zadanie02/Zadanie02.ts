/*
### Generowanie klucza prywatnego
openssl genrsa -out private.key 2048

### Generowanie CSR (Certificate Signing Request)
openssl req -new -key private.key -out request.csr

### Wystawienie certyfikatu samopodpisanego
openssl x509 -req -days 365 -in request.csr -signkey private.key -out certificate.crt

### Utworzenie kontenera PKCS#12 (*.pfx)
openssl pkcs12 -export -out certificate.pfx -inkey private.key -in certificate.crt
*/

import * as https from 'https';
import * as fs from 'fs';

const options = {
  pfx: fs.readFileSync('./certificate.pfx'),
  passphrase: '12345'
};

const server = https.createServer(options, (req, res) => {
    res.writeHead(200, {"Content-Type": "text/plain; charset=utf-8"});
    res.end('HTTPS działa.');
});

server.listen(8443, () => {
    console.log('Serwer https://localhost:8443');
});