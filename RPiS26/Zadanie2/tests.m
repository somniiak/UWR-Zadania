% ---------------------
% Zadanie 2 - Testy
% ---------------------
1;

% Załaduj implementację
source("z2.m");

function run_tests()
  tol = 1e-4;
  passed = 0;
  failed = 0;

  % Format: {x, k}
  test_cases = {
    0.0,  2;
    0.5,  0.75;
    1.0,  2;
    2.0,  2;
    5.0,  2;
    1.0,  1;
    1.0,  4;
    1.0,  10;
    3.0,  5;
    10.0, 5;
    0.1,  1;
    100.0, 50;
  };

  printf("%-10s %-6s %-12s %-12s %-12s %s\n", ...
         "x", "k", "custom", "builtin", "diff", "status");
  printf("%s\n", repmat("-", 1, 65));

  for i = 1:rows(test_cases)
    x = test_cases{i, 1};
    k = test_cases{i, 2};

    custom  = z2(x, k);
    builtin = gammainc(x/2, k/2);
    diff    = abs(custom - builtin);

    if diff < tol
      status = "PASS";
      passed++;
    else
      status = "FAIL";
      failed++;
    end

    printf("%-10.4f %-6d %-12.8f %-12.8f %-12.2e %s\n", ...
           x, k, custom, builtin, diff, status);
  end

  printf("%s\n", repmat("-", 1, 65));
  printf("Wynik: %d/%d testów zaliczonych\n", passed, passed + failed);
end

run_tests();
