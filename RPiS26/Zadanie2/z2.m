% ---------------------
% Zadanie 2, Podpunkt 0
% ---------------------

% https://docs.octave.org/v9.3.0/Script-Files.html
% Skrypt z wieloma funkcjami
1;

% https://en.wikipedia.org/wiki/Romberg's_method
function res = romberg(f, a, b)
  maxn = 15;
  R = zeros(maxn, maxn);

  R(1,1) = (b - a) * (f(a) + f(b)) / 2;

  for i = 2:maxn
    h = (b - a) / 2^(i-1);

    suma = 0;
    for k = 1:2^(i-2)
      suma += f(a + (2*k - 1)*h);
    end

    R(i,1) = 0.5 * R(i-1,1) + h * suma;

    for j = 2:i
      R(i,j) = R(i,j-1) + (R(i,j-1) - R(i-1,j-1))/(4^(j-1) - 1);
    end
  end

  res = R(maxn, maxn);
end

% https://en.wikipedia.org/wiki/Incomplete_gamma_function
function res = gamma_inc(k, x)
  if x <= 0
    res = 0;
  else
    g = @(t) exp(-(t^(1/k)));
    res = (1/k) * romberg(g, 0, x^k);
  end
end

% https://en.wikipedia.org/wiki/Gamma_function
% https://en.wikipedia.org/wiki/Lanczos_approximation#Simple_implementation
function res = gamma_fun(z)
  %  Współczynniki przybliżenia Lanczosa (g=7, n=9)
  g = 7;
  p = [
    0.99999999999980993,
    676.5203681218851,
    -1259.1392167224028,
    771.32342877765313,
    -176.61502916214059,
    12.507343278686905,
    -0.13857109526572012,
    9.9843695780195716e-6,
    1.5056327351493116e-7,
  ];

  if z < 0.5
    % gamma(z) * gamma(1-z) = pi/sin(pi * z)
    res = pi / (sin(pi * z) * gamma_fun(1 - z));
  else
    z -= 1;
    x = p(1);
    for i = 2:9
      x += p(i) / (z + i - 1);
    end
    t = z + g + 0.5;
    res = sqrt(2 * pi) * t^(z + 0.5) * exp(-t) * x;
  end
end

% https://en.wikipedia.org/wiki/Chi-squared_distribution#Cumulative_distribution_function
function res = z2(x, k)
  res = gamma_inc(k/2, x/2) / gamma_fun(k/2);
end
