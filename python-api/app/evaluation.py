import yfinance as yf
import math

# Valuation Metrics
def graham_number(eps, book_value):
    if eps > 0 and book_value > 0:
        return math.sqrt(22.5 * eps * book_value)
    return None

def graham_number_revision(eps, growth_rate):
    if eps > 0:
        return eps * (8.5 + 2 * growth_rate)
    return None

def pe_multiples(eps, avg_pe):
    if eps > 0 and avg_pe > 0:
        return eps * avg_pe
    return None

def peg_ratio(pe, growth_rate):
    if pe and growth_rate and growth_rate > 0:
        return pe / growth_rate
    return None

def gordon_growth_model(dividend, growth_rate, discount_rate=0.10):
    if dividend and growth_rate and discount_rate > growth_rate:
        return dividend / (discount_rate - growth_rate)
    return None

def simplified_dcf(free_cash_flow, growth_rate, shares_outstanding, discount_rate=0.10, terminal_growth=0.02):
    if not free_cash_flow or not shares_outstanding:
        return None

    cash_flows = []
    for i in range(1, 6):
        future_fcf = free_cash_flow * ((1 + growth_rate) ** i)
        discounted_fcf = future_fcf / ((1 + discount_rate) ** i)
        cash_flows.append(discounted_fcf)

    terminal_value = (cash_flows[-1] * (1 + terminal_growth)) / (discount_rate - terminal_growth)
    discounted_terminal_value = terminal_value / ((1 + discount_rate) ** 5)

    intrinsic_value = sum(cash_flows) + discounted_terminal_value
    return intrinsic_value / shares_outstanding

# Dynamic Analysis and risk assessment
def beta_analysis(beta):
    if beta is not None:
        if beta < 1:
            return "defensive"
        elif beta > 1:
            return "risk"
        else:
            return "neutral"
    return "Beta is not available"


# Dividend Analysis
def dividend_analysis(dividend_yield):
    if dividend_yield is not None:
        if dividend_yield > 0.04:
            return "high yield"
        elif dividend_yield > 0.02:
            return "moderate yield"
        else:
            return "low yield"
    return "Dividend yield is not available"

# Profitability
def roe_analysis(roe):
    if roe is not None:
        if roe > 0.15:
            return "highly profitable"
        elif roe > 0.10:
            return "moderately profitable"
        else:
            return "low profitability"
    return "ROE is not available"

def roic_analysis(roic):
    if roic is not None:
        if roic > 0.15:
            return "highly efficient"
        elif roic > 0.10:
            return "moderately efficient"
        else:
            return "low efficiency"
    return "ROIC is not available"

def netp_profit_margin_analysis(net_profit_margin):
    if net_profit_margin is not None:
        if net_profit_margin > 0.20:
            return "highly profitable"
        elif net_profit_margin > 0.10:
            return "moderately profitable"
        else:
            return "low profitability"
    return "Net profit margin is not available"

def current_ratio_analysis(current_ratio):
    if current_ratio is not None:
        if current_ratio > 2:
            return "strong liquidity"
        elif current_ratio > 1:
            return "adequate liquidity"
        else:
            return "weak liquidity"
    return "Current ratio is not available"

def evaluate_stock(ticker_symbol):
    # 1. Stažení dat pouze JEDNOU
    stock = yf.Ticker(ticker_symbol)
    info = stock.info  # Toto je nejtěžší operace, uděláme ji jen jednou
    
    if not info or 'currentPrice' not in info:
        print(f"Chyba: Data pro {ticker_symbol} nebyla nalezena.")
        return

    # 2. Extrakce proměnných z info
    price = info.get('currentPrice')
    eps = info.get('trailingEps')
    book_value = info.get('bookValue')
    fcf = info.get('freeCashflow')
    shares = info.get('sharesOutstanding')
    div_rate = info.get('dividendRate')
    pe = info.get('trailingPE')
    beta = info.get('beta')
    div_yield = info.get('dividendYield')
    roe = info.get('returnOnEquity')
    roic = info.get('returnOnAssets') # YFinance nemá čisté ROIC, ROA je nejbližší náhrada
    net_margin = info.get('profitMargins')
    curr_ratio = info.get('currentRatio')

    # Odhad růstu (buď z info, nebo vlastní fixní odhad)
    # yfinance občas vrací 'earningsQuarterlyGrowth'
    growth = 0.10  # Konzervativní odhad 10 %

    # 3. Výpočty Fair Price
    g_price = graham_number(eps, book_value)
    gr_price = graham_number_revision(eps, growth * 100)
    dcf_price = simplified_dcf(fcf, growth, shares)
    ddm_price = gordon_growth_model(div_rate, 0.05) # Předpoklad 5% růst dividendy
    peg = peg_ratio(pe, growth * 100)

    # 4. Výpis Výsledků
    print(f"\n" + "="*40)
    print(f" ANALÝZA AKCIE: {ticker_symbol} ".center(40, "="))
    print(f"Aktuální cena: {price} USD")
    print("-" * 40)
    
    print(f"{'Metoda':<25} | {'Férová cena':<10}")
    print("-" * 40)
    print(f"{'Grahamovo číslo':<25} | {round(g_price, 2) if g_price else 'N/A'}")
    print(f"{'Graham Revidovaný':<25} | {round(gr_price, 2) if gr_price else 'N/A'}")
    print(f"{'DCF Model (5y)':<25} | {round(dcf_price, 2) if dcf_price else 'N/A'}")
    print(f"{'Gordon Model (DDM)':<25} | {round(ddm_price, 2) if ddm_price else 'N/A'}")
    
    print("-" * 40)
    print(f"PEG Ratio: {round(peg, 2) if peg else 'N/A'} (Ideál < 1.0)")
    print(f"Beta (Riziko): {beta_analysis(beta)}")
    print(f"Ziskovost (ROE): {roe_analysis(roe)}")
    print(f"Likvidita: {current_ratio_analysis(curr_ratio)}")
    print("-" * 40)

    # 5. Výpočet průměrné férové ceny a Margin of Safety
    # Vezmeme průměr z dostupných metod kromě základního Grahama (který bývá u tech moc nízko)
    valid_prices = [p for p in [gr_price, dcf_price, ddm_price] if p]
    if valid_prices:
        avg_fair_price = sum(valid_prices) / len(valid_prices)
        margin = ((avg_fair_price - price) / avg_fair_price) * 100
        print(f"PRŮMĚRNÁ FÉROVÁ CENA: {round(avg_fair_price, 2)} USD")
        print(f"MARGIN OF SAFETY: {round(margin, 2)} %")
        if margin > 0:
            print("STAV: Akcie je pravděpodobně PODHODNOCENÁ")
        else:
            print("STAV: Akcie je pravděpodobně NADHODNOCENÁ")
    print("="*40)
    return {
        "ticker": ticker_symbol,
        "current_price": price,
        "graham_number": g_price,
        "graham_revision": gr_price,
        "dcf_price": dcf_price,
        "ddm_price": ddm_price,
        "peg_ratio": peg,
        "beta_analysis": beta_analysis(beta),
        "roe_analysis": roe_analysis(roe),
        "current_ratio_analysis": current_ratio_analysis(curr_ratio),
    }

# Spuštění pro Apple
evaluate_stock("AAPL")