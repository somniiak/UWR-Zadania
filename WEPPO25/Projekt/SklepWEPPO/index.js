import 'dotenv/config';
import app from './src/app.js';

const PORT = process.env.PORT || 3000;

if (!process.env.DATABASE_URL) {
  throw new Error('DATABASE_URL not set');
}

app.listen(PORT, () => {
    console.log(`${process.env.SHOP_NAME} running at http://localhost:${PORT}`);
});