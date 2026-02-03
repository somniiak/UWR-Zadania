export const requireAuth = (req, res, next) => {
  const user = req.signedCookies.user;

  if (!user) {
    return res.redirect('/login');
  }

  req.user = user;
  next();
};
