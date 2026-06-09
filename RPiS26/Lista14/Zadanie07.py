data = []
with open('l14z07.csv') as f:
    data = [int(x) for x in f.readlines()]

n = len(data)
lambda_mle = sum(data) / n

print(f"n = {n}")
print(f"suma = {sum(data)}")
print(f"lambda_MLE = {lambda_mle:.4f}")
