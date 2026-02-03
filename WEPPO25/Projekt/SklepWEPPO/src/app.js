import path from 'path';
import { fileURLToPath } from 'url';
import express from 'express';
import expressLayouts from 'express-ejs-layouts';
import cookieParser from 'cookie-parser';

import homeRoutes from './routes/home.routes.js';
import productRoutes from './routes/product.routes.js';
import authRoutes from './routes/auth.routes.js';
import adminRoutes from './routes/admin.routes.js';
import searchRoutes from './routes/search.routes.js';
import cartRoutes from './routes/cart.routes.js';
import orderRoutes from './routes/order.routes.js';

const app = express();

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use('/assets', express.static(path.join(__dirname, 'assets')));
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser(process.env.COOKIE_SECRET));
app.use(expressLayouts);
app.set('layout', 'layout');

app.use((req, res, next) => {
  res.locals.shopName = process.env.SHOP_NAME;
  res.locals.maxCookieAge = Number(process.env.COOKIE_MAX_AGE);
  res.locals.user = req.signedCookies.user || null;
  next();
});

app.use(
  homeRoutes,
  productRoutes,
  authRoutes,
  adminRoutes,
  searchRoutes,
  cartRoutes,
  orderRoutes,
);

export default app;
