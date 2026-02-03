import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { database } from '../database/database.js';
import { products } from '../database/schema.js';
import { eq } from 'drizzle-orm';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export const getProductById = async (req, res) => {
  const { id } = req.params;

  const result = await database
    .select()
    .from(products)
    .where(eq(products.id, Number(id)));

  const product = result[0];

  if (!product) {
    return res.status(404).send('Produkt nie istnieje');
  }

  const productImagesDir = path.join(
    __dirname,
    '../assets/images/products',
    String(product.id)
  );

  let images = [];

  if (fs.existsSync(productImagesDir)) {
    const files = fs
      .readdirSync(productImagesDir)
      .filter(file => /\.(jpg|png)$/i.test(file));

    const mainImage = files.find(
      file => file.startsWith('main.')
    );

    const otherImages = files
      .filter(file => !file.startsWith('main.'))
      .sort();

    images = mainImage ?
      [mainImage, ...otherImages] : otherImages;
  }

  res.render('product', {
    product,
    images,
  });
};
