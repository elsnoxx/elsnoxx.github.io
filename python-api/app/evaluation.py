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

# --- GROWTH ---
def growth_analysis(revenue_growth, earnings_growth):
    # revenue_growth: info.get('revenueGrowth')
    # earnings_growth: info.get('earningsGrowth')
    score = 0
    if revenue_growth and revenue_growth > 0.10: score += 1 # Růst tržeb > 10%
    if earnings_growth and earnings_growth > 0.15: score += 1 # Růst zisku > 15%
    
    if score == 2: return "Aggressive Growth"
    if score == 1: return "Steady Growth"
    return "Stagnant / Value"

# --- DEBT (Zadluženost) ---
def debt_analysis(debt_to_equity):
    # debt_to_equity: info.get('debtToEquity') -> v % (např. 150 = 1.5)
    if debt_to_equity is None: return "Unknown"
    if debt_to_equity < 50: return "Low Debt (Safe)"
    if debt_to_equity < 100: return "Moderate Debt"
    return "High Debt (Risk)"

# --- CASH FLOW KVALITA ---
def cash_flow_quality(fcf, net_income):
    # Poměr FCF k čistému zisku - ukazuje, jestli zisk nejsou jen "čísla na papíře"
    if not fcf or not net_income or net_income == 0: return "Unknown"
    ratio = fcf / net_income
    if ratio > 1: return "High Quality (Cash Cow)"
    if ratio > 0.7: return "Good Quality"
    return "Low Quality (Accounting Profit only)"

# --- TECHNICKÁ ANALÝZA (Základy) ---
def technical_summary(current_price, ma50, ma200):
    # ma50: info.get('fiftyDayAverage')
    # ma200: info.get('twoHundredDayAverage')
    if not ma50 or not ma200: return "N/A"
    
    if current_price > ma50 > ma200:
        return "Strong Bullish Trend"
    if current_price < ma50 < ma200:
        return "Strong Bearish Trend"
    return "Sideways / Consolidation"

def evaluate_stock(ticker_symbol):
    # 1. Inicializace a stažení dat (včetně session pro prevenci 429)
    stock = yf.Ticker(ticker_symbol)
    info = stock.info
    
    if not info or 'currentPrice' not in info:
        return {"error": f"Ticker {ticker_symbol} nebyl nalezen nebo chybí data."}

    # 2. Sběr surových dat (Raw Data)
    raw_data = {
        "symbol": ticker_symbol,
        "current_price": info.get('currentPrice'),
        "eps": info.get('trailingEps'),
        "book_value": info.get('bookValue'),
        "fcf": info.get('freeCashflow'),
        "shares_outstanding": info.get('sharesOutstanding'),
        "dividend_rate": info.get('dividendRate'),
        "dividend_yield": info.get('dividendYield'),
        "pe_ratio": info.get('trailingPE'),
        "beta": info.get('beta'),
        "roe": info.get('returnOnEquity'),
        "net_margin": info.get('profitMargins'),
        "current_ratio": info.get('currentRatio'),
        "low_52w": info.get('fiftyTwoWeekLow'),
        "high_52w": info.get('fiftyTwoWeekHigh'),
    }

    # Konstanty pro výpočty
    growth_est = 0.10  # 10% růst
    discount_rate = 0.10
    terminal_growth = 0.02

    # 3. Výpočty Valuací (volání tvých existujících funkcí)
    valuations = {
        "graham_number": graham_number(raw_data['eps'], raw_data['book_value']),
        "graham_revision": graham_number_revision(raw_data['eps'], growth_est * 100),
        "dcf_price": simplified_dcf(raw_data['fcf'], growth_est, raw_data['shares_outstanding'], discount_rate, terminal_growth),
        "gordon_model": gordon_growth_model(raw_data['dividend_rate'], 0.05, discount_rate),
        "pe_multiple_fair": pe_multiples(raw_data['eps'], info.get('forwardPE', 20))
    }

    # 4. Slovní hodnocení (Indikátory)
    indicators = {
        "beta_status": beta_analysis(raw_data['beta']),
        "dividend_status": dividend_analysis(raw_data['dividend_yield']),
        "roe_status": roe_analysis(raw_data['roe']),
        "margin_status": netp_profit_margin_analysis(raw_data['net_margin']),
        "liquidity_status": current_ratio_analysis(raw_data['current_ratio']),
        "price_position_52w": "bottom" if raw_data['current_price'] < (raw_data['low_52w'] * 1.1) else "top" if raw_data['current_price'] > (raw_data['high_52w'] * 0.9) else "middle"
    }

    # 5. Finální shrnutí
    valid_prices = [p for p in [valuations["graham_revision"], valuations["dcf_price"], valuations["pe_multiple_fair"]] if p]
    avg_fair_price = sum(valid_prices) / len(valid_prices) if valid_prices else None
    
    summary = {
        "average_fair_price": avg_fair_price,
        "margin_of_safety": ((avg_fair_price - raw_data['current_price']) / avg_fair_price * 100) if avg_fair_price else None,
        "recommendation": "BUY" if (avg_fair_price and avg_fair_price > raw_data['current_price']) else "SELL/HOLD"
    }

    extended_analysis = {
        "growth_profile": growth_analysis(info.get('revenueGrowth'), info.get('earningsGrowth')),
        "debt_risk": debt_analysis(info.get('debtToEquity')),
        "cash_flow_reliability": cash_flow_quality(info.get('freeCashflow'), info.get('netIncomeToCommon')),
        "technical_trend": technical_summary(
            info.get('currentPrice'), 
            info.get('fiftyDayAverage'), 
            info.get('twoHundredDayAverage')
        )
    }

    # 2. Kontext trhu (Relativní ocenění vůči sektoru)
    # yfinance neposkytuje průměr sektoru přímo, ale můžeme srovnat P/E s indexem S&P 500 (cca 20-25)
    market_context = {
        "market_premium": "Above Market" if (info.get('trailingPE') or 0) > 25 else "Below Market",
        "sector": info.get('sector'),
        "industry": info.get('industry')
    }

    # Finální spojení do návratového objektu
    return {
        "raw_data": raw_data,
        "valuations": valuations,
        "indicators": indicators,
        "advanced_analysis": extended_analysis,
        "market_context": market_context,
        "summary": summary
    }
