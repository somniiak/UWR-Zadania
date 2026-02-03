export const requireAdmin = (req, res, next) => {
  const user = req.signedCookies.user;

  if (!user || user.role !== 'admin') {
    return res.status(403).send('Brak dostępu');
  }

  next();
};
