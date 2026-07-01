# =============================================================================
# Portfolio Choice, Diversification and CAPM Evaluation
# MSc in Data Science - Introduction to Quantitative Finance and Risk Management
# =============================================================================

# -----------------------------------------------------------------------------
# Required Libraries Installation
# -----------------------------------------------------------------------------
# Run these commands in your terminal if libraries are not installed:
#
# pip install numpy          # Numerical computing
# pip install pandas         # Data manipulation and analysis
# pip install matplotlib     # Plotting and visualization
# pip install yfinance       # Yahoo Finance data download
# pip install statsmodels    # Statistical models and regression
# pip install scipy          # Scientific computing and optimization
# pip install seaborn        # Statistical data visualization
# -----------------------------------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import statsmodels.api as sm
from scipy.optimize import minimize
import seaborn as sns

# =============================================================================
# 0. Setup & Configuration
# =============================================================================

# Plotting defaults
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["figure.dpi"] = 110

# Reproducibility
np.random.seed(42)

# Universe: one stock per GICS sector (10 of 11 sectors)
TICKERS = {
    "LRCX": "Lam Research (Information Technology)",
    "DE":   "Deere & Co. (Industrials)",
    "VRTX": "Vertex Pharmaceuticals (Health Care)",
    "LULU": "Lululemon (Consumer Discretionary)",
    "EOG":  "EOG Resources (Energy)",
    "SPGI": "S&P Global (Financials)",
    "NEE":  "NextEra Energy (Utilities)",
    "FCX":  "Freeport-McMoRan (Materials)",
    "TTWO": "Take-Two Interactive (Communication Services)",
    "COST": "Costco (Consumer Staples)",
}

STOCKS = list(TICKERS.keys())
MARKET = "SPY"                      # market proxy / benchmark
ALL_SYMBOLS = STOCKS + [MARKET]

# Sample windows
START_DATE = "2016-01-01"
SPLIT_DATE = "2025-12-31"          # end of estimation period (inclusive)
OOS_START  = "2026-01-01"          # start of out-of-sample period
END_DATE   = "2026-03-31"          # end of out-of-sample period

# Conventions
RF_ANNUAL      = 0.0               # risk-free rate assumed 0% (stated explicitly)
RF_WEEKLY      = RF_ANNUAL / 52
WEEKS_PER_YEAR = 52                # annualization factor

print(f"{len(STOCKS)} stocks + market proxy '{MARKET}'")
print(f"Estimation   : {START_DATE} -> {SPLIT_DATE}")
print(f"Out-of-sample: {OOS_START} -> {END_DATE}")
print(f"Risk-free rate assumed: {RF_ANNUAL:.0%}")

# =============================================================================
# 1. Data Collection
# =============================================================================

# Download weekly adjusted closing prices from Yahoo Finance
raw = yf.download(
    ALL_SYMBOLS,
    start=START_DATE,
    end=END_DATE,
    interval="1wk",
    auto_adjust=True,
    progress=False,
)

prices = raw["Close"][ALL_SYMBOLS].copy()
prices = prices.dropna(how="all").sort_index()

# Sanity checks
print("Price matrix shape:", prices.shape)
print("Date range:", prices.index.min().date(), "->", prices.index.max().date())
print("\nMissing values per column:")
print(prices.isna().sum())

# =============================================================================
# 2. Return Construction and Descriptive Statistics
# =============================================================================

# Weekly simple returns for every asset
returns = prices.pct_change().dropna(how="any")

# Split into estimation and out-of-sample windows
ret_est = returns.loc[:SPLIT_DATE]      # 2016 -> 2025-12-31
ret_oos = returns.loc[OOS_START:]       # 2026-01-01 -> 2026-03-31

# Convenience views
ret_est_stocks = ret_est[STOCKS]
ret_est_mkt    = ret_est[MARKET]
ret_oos_stocks = ret_oos[STOCKS]
ret_oos_mkt    = ret_oos[MARKET]

print("Estimation weeks:", len(ret_est), "| Out-of-sample weeks:", len(ret_oos))

# Per-stock descriptive statistics over the estimation period
desc = pd.DataFrame({
    "Mean weekly": ret_est_stocks.mean(),
    "Ann. mean":   ret_est_stocks.mean() * WEEKS_PER_YEAR,
    "Weekly vol":  ret_est_stocks.std(),
    "Ann. vol":    ret_est_stocks.std() * np.sqrt(WEEKS_PER_YEAR),
    "Min weekly":  ret_est_stocks.min(),
    "Max weekly":  ret_est_stocks.max(),
})
print(desc.sort_values("Ann. vol", ascending=False).round(4))

# Covariance and correlation matrices (weekly, estimation period)
cov_matrix  = ret_est_stocks.cov()
corr_matrix = ret_est_stocks.corr()

fig, ax = plt.subplots(figsize=(9, 7))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm",
            vmin=-1, vmax=1, square=True, cbar_kws={"label": "correlation"}, ax=ax)
ax.set_title("Weekly return correlation - estimation period")
plt.tight_layout()
plt.show()

# =============================================================================
# 3. Diversification Analysis
# =============================================================================

# Reusable portfolio analytics (annualized)
mean_weekly = ret_est_stocks.mean()   # expected-return estimate used throughout

def port_return(weights, mean_ret=mean_weekly, ann=WEEKS_PER_YEAR):
    """Annualized portfolio return from weekly mean returns"""
    return float(np.dot(weights, mean_ret) * ann)

def port_vol(weights, cov=cov_matrix, ann=WEEKS_PER_YEAR):
    """Annualized portfolio volatility from the weekly covariance matrix"""
    w = np.asarray(weights)
    return float(np.sqrt(w @ cov.values @ w) * np.sqrt(ann))

def port_sharpe(weights, mean_ret=mean_weekly, cov=cov_matrix, rf=RF_ANNUAL):
    """Portfolio Sharpe ratio"""
    return (port_return(weights, mean_ret) - rf) / port_vol(weights, cov)

def max_drawdown_est(weights):
    """Maximum drawdown over the estimation period"""
    r = ret_est_stocks @ np.asarray(weights)
    cum = (1 + r).cumprod()
    running_max = cum.cummax()
    return float((cum / running_max - 1.0).min())

# Portfolio 1: equally weighted across all 10 stocks
w_eq = pd.Series(1.0 / len(STOCKS), index=STOCKS)

# Portfolio 2: concentrated in the 2 most volatile stocks (50/50)
two_most_vol = desc["Ann. vol"].sort_values(ascending=False).head(2).index.tolist()
w_conc = pd.Series(0.0, index=STOCKS)
w_conc[two_most_vol] = 0.5
print("Two most volatile stocks:", two_most_vol)

# Summary metrics for both portfolios (including max drawdown)
simple_summary = pd.DataFrame({
    "Equal-weight (10)": [port_return(w_eq), port_vol(w_eq), port_sharpe(w_eq), max_drawdown_est(w_eq)],
    f"Concentrated ({' + '.join(two_most_vol)})": [port_return(w_conc), port_vol(w_conc), port_sharpe(w_conc), max_drawdown_est(w_conc)],
}, index=["Ann. return", "Ann. volatility", "Sharpe ratio", "Max drawdown"]).round(4)
print(simple_summary)

# Cumulative performance over the estimation period
cum_eq   = (1 + ret_est_stocks @ w_eq.values).cumprod()
cum_conc = (1 + ret_est_stocks @ w_conc.values).cumprod()

fig, ax = plt.subplots()
cum_eq.plot(ax=ax, label="Equal-weight (10 stocks)")
cum_conc.plot(ax=ax, label=f"Concentrated ({' + '.join(two_most_vol)})")
ax.set_title("Cumulative performance - estimation period")
ax.set_ylabel("Growth of $1")
ax.legend()
plt.tight_layout()
plt.show()

# =============================================================================
# 4. Efficient Frontier Without Short-Selling
# =============================================================================

N = len(STOCKS)
bounds_long = tuple((0.0, 1.0) for _ in range(N))   # no short-selling
budget = {"type": "eq", "fun": lambda w: np.sum(w) - 1.0}
w0 = np.repeat(1.0 / N, N)

# Minimum-variance portfolio (long-only)
res_mvp = minimize(port_vol, w0, method="SLSQP", bounds=bounds_long, constraints=[budget])
w_mvp = pd.Series(res_mvp.x, index=STOCKS)

# Tangency portfolio = maximum Sharpe ratio (long-only)
neg_sharpe = lambda w: -port_sharpe(w)
res_tan = minimize(neg_sharpe, w0, method="SLSQP", bounds=bounds_long, constraints=[budget])
w_tan = pd.Series(res_tan.x, index=STOCKS)

# Trace the efficient frontier: minimise vol for a grid of target returns
def frontier(bounds, n=60):
    ann_mean = mean_weekly * WEEKS_PER_YEAR
    targets = np.linspace(ann_mean.min(), ann_mean.max(), n)
    vols, rets = [], []
    for t in targets:
        cons = [budget, {"type": "eq", "fun": lambda w, t=t: port_return(w) - t}]
        r = minimize(port_vol, w0, method="SLSQP", bounds=bounds, constraints=cons)
        if r.success:
            vols.append(port_vol(r.x)); rets.append(t)
    return np.array(vols), np.array(rets)

fr_vol, fr_ret = frontier(bounds_long)

# Plot frontier with individual stocks and key portfolios
fig, ax = plt.subplots()
ax.plot(fr_vol, fr_ret, "b-", lw=2, label="Efficient frontier (no short)")
ax.scatter(desc["Ann. vol"], desc["Ann. mean"], c="grey", marker="o", zorder=3)
for s in STOCKS:
    ax.annotate(s, (desc.loc[s, "Ann. vol"], desc.loc[s, "Ann. mean"]),
                fontsize=8, xytext=(4, 2), textcoords="offset points")
ax.scatter(port_vol(w_eq),  port_return(w_eq),  c="green",  marker="s", s=90,  label="Equal-weight", zorder=4)
ax.scatter(port_vol(w_mvp), port_return(w_mvp), c="purple", marker="*", s=220, label="Min-variance", zorder=4)
ax.scatter(port_vol(w_tan), port_return(w_tan), c="red",    marker="*", s=220, label="Tangency", zorder=4)
ax.set_xlabel("Annualized volatility"); ax.set_ylabel("Annualized return")
ax.set_title("Efficient frontier without short-selling")
ax.legend(); plt.tight_layout(); plt.show()

# Key portfolio statistics
print(f"Min-variance : ret={port_return(w_mvp):.4f}  vol={port_vol(w_mvp):.4f}  Sharpe={port_sharpe(w_mvp):.4f}")
print(f"Tangency     : ret={port_return(w_tan):.4f}  vol={port_vol(w_tan):.4f}  Sharpe={port_sharpe(w_tan):.4f}")

# Report weights (drop near-zero rows for readability)
weights_long = pd.DataFrame({"Min-variance": w_mvp, "Tangency": w_tan})
print(weights_long[weights_long.abs().max(axis=1) > 1e-4].round(4))

# =============================================================================
# 5. Efficient Frontier With Bounded Short-Selling
# =============================================================================

bounds_short = tuple((-1.0, 1.0) for _ in range(N))   # bounded short-selling

# Tangency portfolio with bounded short-selling
res_tan_s = minimize(neg_sharpe, w0, method="SLSQP", bounds=bounds_short, constraints=[budget])
w_tan_short = pd.Series(res_tan_s.x, index=STOCKS)

# Bounded-short frontier
frs_vol, frs_ret = frontier(bounds_short)

# Overlay both frontiers
fig, ax = plt.subplots()
ax.plot(fr_vol, fr_ret, "b-", lw=2, label="No short-selling (0 <= w <= 1)")
ax.plot(frs_vol, frs_ret, "r--", lw=2, label="Bounded short-selling (-1 <= w <= 1)")
ax.scatter(desc["Ann. vol"], desc["Ann. mean"], c="grey", marker="o", zorder=3)
for s in STOCKS:
    ax.annotate(s, (desc.loc[s, "Ann. vol"], desc.loc[s, "Ann. mean"]),
                fontsize=8, xytext=(4, 2), textcoords="offset points")
ax.set_xlabel("Annualized volatility"); ax.set_ylabel("Annualized return")
ax.set_title("Efficient frontier: no-short vs bounded short-selling")
ax.legend(); plt.tight_layout(); plt.show()

print(f"Tangency (bounded short): ret={port_return(w_tan_short):.4f}  "
      f"vol={port_vol(w_tan_short):.4f}  Sharpe={port_sharpe(w_tan_short):.4f}")

# Compare tangency weights under the two regimes
tan_compare = pd.DataFrame({"Tangency (long-only)": w_tan,
                            "Tangency (bounded short)": w_tan_short}).round(4)
print(tan_compare)

# =============================================================================
# 6. CAPM and Beta Estimation
# =============================================================================

# Per-stock CAPM regressions: R_i = alpha + beta * R_m   (Rf = 0)
X = sm.add_constant(ret_est_mkt)                 # market returns + intercept
mkt_ann_return = ret_est_mkt.mean() * WEEKS_PER_YEAR

rows, betas = {}, {}
for s in STOCKS:
    model = sm.OLS(ret_est_stocks[s], X).fit()
    beta  = model.params[MARKET]
    betas[s] = beta
    realized     = mean_weekly[s] * WEEKS_PER_YEAR
    capm_implied = RF_ANNUAL + beta * (mkt_ann_return - RF_ANNUAL)
    rows[s] = {
        "Beta": beta,
        "Alpha (ann.)": model.params["const"] * WEEKS_PER_YEAR,
        "Realized ann. ret": realized,
        "CAPM-implied ret": capm_implied,
        "Diff (realized - CAPM)": realized - capm_implied,
    }
capm_table = pd.DataFrame(rows).T.round(4)
betas = pd.Series(betas)
print(capm_table)

# Portfolio betas = weighted average of stock betas
port_betas = pd.Series({
    "Equal-weight": float(betas @ w_eq.values),
    "Min-variance": float(betas @ w_mvp.values),
    "Tangency":     float(betas @ w_tan.values),
}).round(4)
print("Portfolio betas:")
print(port_betas)

# Security Market Line
fig, ax = plt.subplots()
ax.scatter(betas, capm_table["Realized ann. ret"], c="steelblue", zorder=3)
for s in STOCKS:
    ax.annotate(s, (betas[s], capm_table.loc[s, "Realized ann. ret"]),
                fontsize=8, xytext=(4, 2), textcoords="offset points")
bx = np.linspace(0, betas.max() * 1.1, 50)
ax.plot(bx, RF_ANNUAL + bx * (mkt_ann_return - RF_ANNUAL), "r--", label="CAPM / SML")
ax.scatter(1.0, mkt_ann_return, c="black", marker="D", s=80, label="Market (SPY)", zorder=4)
ax.set_xlabel("Beta"); ax.set_ylabel("Average annualized return")
ax.set_title("Security Market Line"); ax.legend()
plt.tight_layout(); plt.show()

# =============================================================================
# 7. Out-of-Sample Evaluation
# =============================================================================

def max_drawdown(cum_series):
    """Maximum drawdown from cumulative wealth index"""
    running_max = cum_series.cummax()
    return float((cum_series / running_max - 1.0).min())

def evaluate_oos(weights, name):
    """Evaluate portfolio out-of-sample"""
    r = ret_oos_stocks @ np.asarray(weights)
    cum = (1 + r).cumprod()
    capm = sm.OLS(r, sm.add_constant(ret_oos_mkt)).fit()   # OOS beta + Jensen's alpha
    return pd.Series({
        "Cumulative return":   cum.iloc[-1] - 1,
        "Ann. vol":            r.std() * np.sqrt(WEEKS_PER_YEAR),
        "Sharpe":              (r.mean() * WEEKS_PER_YEAR - RF_ANNUAL) / (r.std() * np.sqrt(WEEKS_PER_YEAR)),
        "Max drawdown":        max_drawdown(cum),
        "Beta (OOS)":          capm.params[MARKET],
        "Jensen alpha (ann.)": capm.params["const"] * WEEKS_PER_YEAR,
    }, name=name), cum

# Freeze the estimation-period weights and apply them out of sample
portfolios = {
    "Equal-weight":             w_eq.values,
    "Min-variance":             w_mvp.values,
    "Tangency":                 w_tan.values,
    "Tangency (bounded short)": w_tan_short.values,
}

results, cums = [], {}
for name, w in portfolios.items():
    s, cum = evaluate_oos(w, name)
    results.append(s); cums[name] = cum
oos_table = pd.DataFrame(results).round(4)
print(oos_table)

# Plot cumulative trajectories vs the market benchmark
cum_mkt = (1 + ret_oos_mkt).cumprod()
fig, ax = plt.subplots()
for name, cum in cums.items():
    cum.plot(ax=ax, label=name)
cum_mkt.plot(ax=ax, label="SPY (market)", color="black", linestyle="--")
ax.set_title("Out-of-sample cumulative return (Jan-Mar 2026)")
ax.set_ylabel("Growth of $1"); ax.legend()
plt.tight_layout(); plt.show()

print("\n" + "="*80)
print("Analysis complete.")
print("="*80)
