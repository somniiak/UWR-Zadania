import { database } from '../database/database.js';
import { orders, orderItems, products } from '../database/schema.js';
import { eq, inArray } from 'drizzle-orm';

export const createOrder = async (req, res) => {
  if (!req.user) {
    return res.redirect('/login');
  }

  let cart = [];

  if (req.signedCookies.cart) {
    try { cart = JSON.parse(req.signedCookies.cart); }
    catch { cart = []; }
  }

  if (cart.length === 0) {
    return res.redirect('/cart');
  }

  const ids = cart.map(i => i.productId);

  const dbProducts = await database
    .select()
    .from(products)
    .where(inArray(products.id, ids));

  const [order] = await database
    .insert(orders)
    .values({
      userId: req.user.id,
      status: 'new',
      createdAt: new Date(),
    })
    .returning();

  const items = cart.map(item => {
    const product = dbProducts.find(p => p.id === item.productId);

    return {
      orderId: order.id,
      productId: product.id,
      quantity: item.quantity,
      price: product.price,
    };
  });

  await database.insert(orderItems).values(items);

  res.clearCookie('cart');
  res.redirect(`/order/${order.id}`);
};

export const showOrder = async (req, res) => {
  const orderId = parseInt(req.params.id, 10);

  if (!Number.isInteger(orderId)) {
    return res.redirect('/');
  }

  const [order] = await database
    .select()
    .from(orders)
    .where(eq(orders.id, orderId));

  if (!order) {
    return res.status(404).send('Nie znaleziono zamówienia');
  }

  // zabezpiecznie
  if (!req.user || (order.userId !== req.user.id && req.user.role !== 'admin')) {
    return res.status(403).send('Brak dostępu');
  }

  const items = await database
    .select({
      name: products.name,
      price: orderItems.price,
      quantity: orderItems.quantity,
      productId: products.id,
    })
    .from(orderItems)
    .innerJoin(products, eq(products.id, orderItems.productId))
    .where(eq(orderItems.orderId, orderId));

  const total = items.reduce(
    (sum, i) => sum + Number(i.price) * i.quantity,
    0
  );

  res.render('order-success', {
    order,
    items,
    total,
  });
};
