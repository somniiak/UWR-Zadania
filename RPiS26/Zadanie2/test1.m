1;

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

function res = gamma_inc(k, x)
  if x <= 0
    res = 0;
  else
    g = @(t) exp(-(t^(1/k)));
    res = (1/k) * romberg(g, 0, x^k);
  end
end

x = linspace(0, 100, 100);
k_vals = [0.2, 2, 5];
colors = {'b', 'r', 'g'};

figure;
hold on;

for i = 1:length(k_vals)
    k = k_vals(i);

    y_custom  = arrayfun(@(xi) gamma_inc(k/2, xi/2), x);
    y_builtin = gammainc(x/2, k/2) * gamma(k/2);

    plot(x, y_custom,  colors{i}, 'LineWidth', 2, ...
         'DisplayName', sprintf('gamma\\_inc(), k=%d', k));
    plot(x, y_builtin, 'k--', 'LineWidth', 1, ...
         'DisplayName', sprintf('wbudowana, k=%d', k));
end

hold off;
h = legend ("show");
xlabel('x', 'FontSize', 12);
ylabel('\gamma(k/2, x/2)', 'FontSize', 12);
title('Porównanie niekompletnej funkcji Gamma (podstawinie)', 'FontSize', 13);
grid on;
