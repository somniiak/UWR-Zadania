import { database } from '../database/database.js';
import { products } from '../database/schema.js';
import { sql, asc } from 'drizzle-orm';

export const homePage = async (req, res) => {
  const randomProducts = await database
    .select()
    .from(products)
    .orderBy(sql`RANDOM()`)
    .limit(10);

  const cheapestProducts = await database
    .select()
    .from(products)
    .orderBy(asc(products.price))
    .limit(10);

  res.render('home', {
    randomProducts,
    cheapestProducts,
  });
};
