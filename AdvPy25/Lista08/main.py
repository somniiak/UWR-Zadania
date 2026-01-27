import asyncio
from aiohttp import ClientSession
from datetime import datetime as dt
from collections import defaultdict
import matplotlib.pyplot as plt

async def get_currency_data(currency, year, session=ClientSession):
    """Pobiera dane z API NBP."""
    start = f"{year}-01-01"
    end = f"{year}-12-31"
    today_year = dt.now().year

    if year == today_year:
        end = dt.now().strftime("%Y-%m-%d")


    url = f"https://api.nbp.pl/api/exchangerates/rates/A/{currency}/{start}/{end}/?format=json"

    async with session.get(url) as r:
        return await r.json()

def process_currency(result):
    """Oblicza średnią miesięczną dla jednego roku."""
    data = defaultdict(list)

    for rate in result["rates"]:
        month = int(rate["effectiveDate"][5:7])
        value = float(rate["mid"])
        data[month].append(value)

    return {
        month: sum(values) / len(values)
        for month, values in data.items()
    }

def predict_currency(result):
    '''Dla każdego miesiąca obliczamy różnicę między ostatnim a
    poprzednim rokiem i dodajemy tę różnicę do ostatniego roku.'''
    years_sorted = sorted(result.keys())
    last_year = years_sorted[-1]
    prev_year = years_sorted[-2]

    res = {}

    for month in range(1, 13):
        prev = result[prev_year].get(month, 0)
        last = result[last_year].get(month, 0)
        res[month] = 2 * last - prev
    
    return res

async def main():
    years = [2023, 2024]
    codes = ["EUR", "USD"]

    # Ściaganie kursów walut 
    async with ClientSession() as session:
        tasks = {}
        for code in codes:
            for year in years:
                tasks[(code, year)] = asyncio.create_task(
                    get_currency_data(code, year, session))

        results = {k: await t for k, t in tasks.items()}

    # Obliczenie średnich dla miesięcy
    processed = {}
    for code in codes:
        processed[code] = {}
        for year in years:
            processed[code][year] = process_currency(results[(code, year)])

    # Prognoza na przyszły rok
    for code in codes:
        processed[code][max(years) + 1] = predict_currency(processed[code])

    # Wykresy
    plt.figure(figsize=(12, 6))
    months_list = range(1, 13)

    for code, years_data in processed.items():
        for year, months_data in years_data.items():
            values = [months_data.get(m, 0) for m in months_list]
            if year == 2025:
                plt.plot(months_list, values, marker='o', linestyle='dashed', label=f"{code} {year} (prognoza)")
            else:
                plt.plot(months_list, values, marker='o', linestyle='solid', label=f"{code} {year}")

    plt.title("Średnie miesięczne kursy EUR i USD z prognozą na 2025")
    plt.xlabel("Miesiąc")
    plt.ylabel("Kurs w PLN")
    plt.xticks(range(1, 13))
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    asyncio.run(main())
