import express from 'express';
import { requireAdmin } from '../middleware/requireAdmin.js';
import {
    showUsers,
    showProducts,
    showOrders,
    updateProduct,
    deleteProduct,
    showAddProduct,
    addProduct,
} from '../controllers/admin.controller.js';

const router = express.Router();

router.get('/admin/users', requireAdmin, showUsers);

router.get('/admin/orders', requireAdmin, showOrders);

router.get('/admin/products', requireAdmin, showProducts);

router.get('/admin/add_product', requireAdmin, showAddProduct);

router.post('/admin/products/:id/edit', requireAdmin, updateProduct);

router.post('/admin/products/:id/delete', requireAdmin, deleteProduct);

router.post('/admin/add_product', requireAdmin, addProduct);

export default router;
