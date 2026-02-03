import { database } from '../database/database.js';
import { products } from '../database/schema.js';
import { eq, inArray } from 'drizzle-orm';

export const addToCart = async (req, res) => {
  const productId = parseInt(req.body.productId, 10);
  const quantity = parseInt(req.body.count, 10);

  if (!Number.isInteger(productId) || quantity < 1) {
    return res.redirect(`/product/${productId}`);
  }

  let cart = [];

  if (req.signedCookies.cart) {
    try { cart = JSON.parse(req.signedCookies.cart); }
    catch { cart = []; }
  }

  const existing = cart.find(i => i.productId === productId);

  if (existing) {
    existing.quantity += quantity;
  } else {
    cart.push({ productId, quantity });
  }

  res.cookie(
    'cart',
    JSON.stringify(cart),
    {
        signed: true,
        maxAge: res.locals.maxCookieAge,
    }
  );

  res.redirect(`/product/${productId}`);
};

export const removeFromCart = (req, res) => {
  const productId = parseInt(req.body.productId, 10);

  let cart = [];

  if (req.signedCookies.cart) {
    cart = JSON.parse(req.signedCookies.cart);
  }

  cart = cart.filter(i => i.productId !== productId);

  res.cookie(
    'cart',
    JSON.stringify(cart),
    {
        signed: true,
        maxAge: res.locals.maxCookieAge,
    }
  );

  res.redirect('/cart');
};

export const showCart = async (req, res) => {
  let cart = [];

  if (req.signedCookies.cart) {
    cart = JSON.parse(req.signedCookies.cart);
  }

  if (cart.length === 0) {
    return res.render('cart', { items: [], total: 0 });
  }

  const ids = cart.map(i => i.productId);

  const dbProducts = await database
    .select()
    .from(products)
    .where(inArray(products.id, ids));

  const items = cart.map(item => {
    const product = dbProducts.find(p => p.id === item.productId);

    return {
      product,
      quantity: item.quantity,
      subtotal: product.price * item.quantity
    };
  });

  const total = items.reduce((sum, i) => sum + i.subtotal, 0);

  res.render('cart', { items, total });
};