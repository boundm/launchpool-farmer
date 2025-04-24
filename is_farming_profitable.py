def farming_profit_check(apr_percent, funding_percent_per_4h, capital_usd, is_short=True):
    apr_daily = apr_percent / 365 / 100
    funding_daily = funding_percent_per_4h * 6 / 100  # 6 раз в сутки

    # Доход от фарма (APR)
    farming_profit_daily = capital_usd * apr_daily

    # Расход на фандинг: в шорте — платим при отриц. ставке
    if is_short:
        funding_cost_daily = capital_usd * abs(funding_daily)
    else:
        funding_cost_daily = -capital_usd * funding_daily

    # Чистая прибыль
    net_daily = farming_profit_daily - funding_cost_daily
    net_yearly = net_daily * 365

    print("📈 Доход от фарма в день:       ${:.2f}".format(farming_profit_daily))
    print("📉 Расход на фандинг в день:    ${:.2f}".format(funding_cost_daily))
    print("💰 Чистая прибыль в день:       ${:.2f}".format(net_daily))
    print("📆 Чистая прибыль в год:        ${:.2f}".format(net_yearly))

    if net_daily > 0:
        print("\n✅ Фарм с хеджем ВЫГОДЕН!")
    elif net_daily < 0:
        print("\n❌ Фарм с хеджем НЕВЫГОДЕН.")
    else:
        print("\n⚖️ В ноль, без прибыли.")

    min_apr = funding_percent_per_4h * 6 * 365
    print("\n📌 Минимальный APR для безубыточности: {:.2f}%".format(min_apr))


def main():
    apr = float(input('Введи APR пула: '))
    funding = float(input('Введи фандинг: '))
    capital = float(input('Введи банк: '))
    farming_profit_check(apr, funding, capital, is_short=True)


if __name__ == "__main__":
    main()