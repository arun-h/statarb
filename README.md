
# Statistical Arbitrage Trading System for Nifty

A statistical arbitrage (pairs trading) system designed for the Indian stock market.
This project identifies liquid stocks, finds cointegrated pairs, models spreads, and generates market-neutral long–short trades.


Project Overview

Statistical arbitrage aims to exploit temporary mispricing between historically related stocks.

Core Idea:

-Identify stocks that move together.

-Detect deviations (spread widens).

-Buy the cheap one, short(sell) the expensive one.

-Wait for price convergence and exit.

-Keep the portfolio market-neutral, reducing directional risk.

This project focuses on NIFTY 50 futures-enabled stocks and will later integrate with broker APIs for live execution.

## **Project Progress Checklist**

### **Phase 1**

#### **Task 1.1: Environment Setup** ✅ COMPLETED
- [x] Created project folder structure
  - `data/raw/`
  - `data/processed/`
  - `src/`
  - `notebooks/`
  - `results/`
- [x] Set up virtual environment
- [x] Installed required dependencies
  - pandas
  - numpy
  - yfinance
  - statsmodels
  - matplotlib
  - seaborn
  - jupyter
- [x] Initialized Jupyter notebook environment

**Status:** ✅ Complete 

---

#### **Task 1.2: Liquidity Analysis & Stock Universe Selection** ⏳ IN PROGRESS
- [x] Compiled Nifty 50 constituent list (50 stocks)
- [x] Downloaded 6 months historical data (Jun 2024 - Dec 2024)
- [x] Calculated liquidity metrics for each stock:
  - Average daily turnover (₹ Crores)
  - Median daily turnover
  - Average volume
  - Latest price
  - Bid-ask spread proxy (High-Low %)
- [x] Created liquidity comparison DataFrame

**Status:**

---

#### **Task 1.3: Apply Cash Market Filters** ⏳ IN PROGRESS
- [ ] Filter by minimum average turnover (≥₹50 Crores)
- [ ] Filter by minimum median turnover (≥₹30 Crores)
- [ ] Filter by price range (₹300 - ₹4,000)
- [ ] Filter by spread threshold (<2%)
- [ ] Filter by data quality (≥100 trading days)
- [ ] Generate final stock universe (12-15 stocks)
- [ ] Export filtered stock list

**Status:** 

---

#### **Task 1.4: Download 2-Year Historical Data** ⏳ PENDING
- [ ] Download 2 years data for filtered stocks
- [ ] Validate data quality (missing values, outliers)
- [ ] Handle corporate actions
- [ ] Save cleaned data to `data/raw/`

**Status:** ⏸️ Pending

---

#### **Task 1.5: Build Multi-Factor Pair Scorer** ⏳ PENDING
- [ ] Implement cointegration test
- [ ] Calculate hedge ratios
- [ ] Calculate half-life of mean reversion
- [ ] Build 6-factor scoring system
- [ ] Test on sample pairs

**Status:** ⏸️ Pending

---

