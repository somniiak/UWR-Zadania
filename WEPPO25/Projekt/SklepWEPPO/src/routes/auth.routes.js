import express from 'express';
import {
  showSignup,
  handleSignup,
  showLogin,
  handleLogin,
} from '../controllers/auth.controller.js';

const router = express.Router();

router.get('/signup', showSignup);
router.post('/signup', handleSignup);

router.get('/login', showLogin);
router.post('/login', handleLogin);

router.get('/logout', (req, res) => {
  res.clearCookie('user');
  res.redirect('/');
});

export default router;
