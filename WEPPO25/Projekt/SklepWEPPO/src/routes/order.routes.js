import express from 'express';
import { createOrder, showOrder } from '../controllers/order.controller.js';
import { requireAuth } from '../middleware/requireAuth.js';

const router = express.Router();

router.post('/order/create', requireAuth, createOrder);

router.get('/order/:id', requireAuth, showOrder);

export default router;
