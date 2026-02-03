import express from 'express';
import { getProductById } from '../controllers/product.controller.js';

const router = express.Router();

router.get('/product/:id', getProductById);

export default router;
