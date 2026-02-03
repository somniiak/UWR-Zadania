import { database } from '../database/database.js';
import { users } from '../database/schema.js';
import { eq } from 'drizzle-orm';
import { hashPassword, verifyPassword } from '../util/password.js';

const setAuthCookie = (res, user) => {
  res.cookie(
    'user',
    {
      id: user.id,
      email: user.email,
      role: user.role,
    },
    {
      signed: true,
      maxAge: res.locals.maxCookieAge,
    }
  );
};

export const showSignup = (req, res) => {
  res.render('signup', { error: null });
};

export const showLogin = (req, res) => {
  res.render('login', { error: null });
};

export const handleSignup = async (req, res) => {
  const { email, password, password2 } = req.body;

  if (password !== password2) {
    return res.render('signup', { error: 'Hasła nie są takie same' });
  }

  if (!email || !password) {
    return res.render('signup', { error: 'Wszystkie pola są wymagane' });
  }

  try {
    const existing = await database
      .select()
      .from(users)
      .where(eq(users.email, email));

    if (existing.length > 0) {
      return res.render('signup', { error: 'Użytkownik już istnieje' });
    }

    const passwordHash = await hashPassword(password);

    const [newUser] = await database
      .insert(users)
      .values({
        email,
        passwordHash,
        role: 'user',
      })
    .returning();

    setAuthCookie(res, newUser);
    res.redirect('/');
  } catch (err) {
    console.error(err);
    res.render('signup', { error: 'Błąd serwera' });
  }
};

export const handleLogin = async (req, res) => {
  const { email, password } = req.body;

  if (!email || !password) {
    return res.render('login', { error: 'Nieprawidłowe dane logowania' });
  }

  try {
    const [user] = await database
      .select()
      .from(users)
      .where(eq(users.email, email));

    if (!user) {
      return res.render('login', { error: 'Nieprawidłowe dane logowania' });
    }

    const ok = await verifyPassword(password, user.passwordHash);
    if (!ok) {
      return res.render('login', { error: 'Nieprawidłowe dane logowania' });
    }

    setAuthCookie(res, user);
    res.redirect('/');
  } catch (err) {
    console.error(err);
    res.render('login', { error: 'Błąd serwera' });
  }
};
