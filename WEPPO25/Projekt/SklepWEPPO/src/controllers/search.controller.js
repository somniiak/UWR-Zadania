import { database } from '../database/database.js';
import { products } from '../database/schema.js';
import { ilike, or } from 'drizzle-orm';

export const searchProducts = async (req, res) => {
  const q = req.query.q?.trim();

  if (!q) {
    return res.render('search', {
      q: '',
      products: [],
    });
  }

  const results = await database
    .select()
    .from(products)
    .where(
      or(
        ilike(products.name, `%${q}%`),
        ilike(products.description, `%${q}%`)
      )
    );

  res.render('search', {
    q,
    products: results,
  });
};
