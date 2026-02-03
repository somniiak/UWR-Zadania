import { eq } from 'drizzle-orm';
import { database } from '../database/database.js';
import { users, products, orders } from '../database/schema.js';

export const showUsers = async (req, res) => {
  try {
    const allUsers = await database.select().from(users);

    res.render('admin/users', {
      users: allUsers,
    });
  } catch (err) {
    console.error(err);
    res.status(500).send('Błąd serwera');
  }
};

export const showOrders = async (req, res) => {
  try {
    const allOrders = await database
      .select({
        id: orders.id,
        email: users.email,
        status: orders.status
      })
      .from(orders)
      .leftJoin(users, eq(users.id, orders.userId))

    res.render('admin/orders', {
      orders: allOrders,
    });
  } catch (err) {
    console.error(err);
    res.status(500).send('Błąd serwera');
  }
};

export const showProducts = async (req, res) => {
  try {
    const allProducts = await database
      .select()
      .from(products)
      .orderBy(products.id);

    res.render('admin/products', {
      products: allProducts,
    });
  } catch (err) {
    console.error(err);
    res.status(500).send('Błąd serwera');
  }
};

export const updateProduct = async (req, res) => {
  const { newName, newDesc, newPrice } = req.body;
  const { id } = req.params;

  await database
    .update(products)
    .set({
      name: newName,
      description: newDesc,
      price: newPrice,
    })
    .where(eq(products.id, id));

  res.redirect('/admin/products');
};

export const deleteProduct = async (req, res) => {
  const { id } = req.params;

  await database
    .delete(products)
    .where(eq(products.id, id));

  res.redirect('/admin/products');
};

export const showAddProduct = (req, res) => {
  res.render('admin/add_product');
};

export const addProduct = async (req, res) => {
  const { name, price, description } = req.body;

  await database.insert(products).values({
    name,
    price,
    description,
  });

  res.render('admin/add_product', { productStatus : name } );
};
