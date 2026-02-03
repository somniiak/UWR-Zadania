import express from 'express';
import { addToCart, removeFromCart, showCart } from '../controllers/cart.controller.js';

const router = express.Router();

router.get('/cart', showCart);

router.post('/cart/add', addToCart);

router.post('/cart/delete', removeFromCart);

export default router;
