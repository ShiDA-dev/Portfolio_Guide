# Data & Marketing Analyst Portfolio Guide

Welcome to my Data & Marketing Analysis Portfolio.

---

## Projects Overview

| # | Project | Business Focus | Tools / Skills | Outcome |
| --- | --- | --- | --- | --- |
| 1 | **[PortfolioAI](https://github.com/StevenShi998/PortfolioAI)** | ML-driven stock allocation and plain-English recommendations for end users. | Python, Variational LSTM, PostgreSQL, full-stack dashboard | Backtested allocations, recommendation history, user preference–driven outputs. |
| 2 | **[Bright Smiles](Bright-Smiles)** | Which Arizona pediatric dental offices are worth a closer look for acquisition. | Python (pandas), Power BI | Top 50 shortlist, map dashboard, enrollment and rating score. |
| 3 | **[Custom CPI & Grocery Budget](https://github.com/StevenShi998/Custom-CPI-Study)** | Why CPI increased over the last 5 years; what the drivers were and why. | SQL (CTEs, window functions), Python (pandas, NumPy), Power BI | 60-month trend, increase/decrease breakdown, beef category focus; dashboard-ready. |
| 4 | **[StageTEN](https://github.com/StevenShi998/StageTEN)** | Marketing reports and automation for HubSpot/Shopify (deal naming, app downloader, KPIs). | Python, pandas, Google Analytics, HubSpot CRM | Consistent deal naming, lifecycle segmentation, channel performance reports. |
| 5 | **[UW Course Explorer](https://github.com/StevenShi998/UW-Course-SearchTree)** | Prerequisite and future-course trees with search and ratings-weighted path recommendations. | JavaScript, SQL, graph traversal, DAG logic | Interactive tree view, optimal path selection, UW Flow–based preferences. |
| 6 | **[Alchemy E-commerce](https://github.com/StevenShi998/Alchemy-E-commerce)** | My own e-commerce store with product photography, email campaigns, and marketing content. | Adobe Photoshop, Adobe Lightroom, Shopify, email marketing | Live store, marketing campaigns, $30k+ real revenue. |
| 7 | **[FFT for Retail Cycle Detection](https://github.com/StevenShi998/Fast-Fourier-Transform)** | Dominant cycles in U.S. retail sales; smoothed series for campaign and planning use. | Python, NumPy FFT, pandas, Matplotlib, low-pass filtering | Annual cycle identification, raw vs smoothed comparison, business interpretation. |

---

## Skills

### Programming Languages
<table>
  <tr>
    <td align="center"><img src="https://go-skill-icons.vercel.app/api/icons?i=python" width="40"><br><b>Python</b></td>
    <td align="center"><img src="https://go-skill-icons.vercel.app/api/icons?i=mysql" width="40"><br><b>SQL</b></td>
  </tr>
</table>

### Data Analysis & Visualization
<table>
  <tr>
    <td align="center"><img src="https://go-skill-icons.vercel.app/api/icons?i=pandas" width="40"><br><b>Pandas</b></td>
    <td align="center"><img src="https://go-skill-icons.vercel.app/api/icons?i=numpy" width="40"><br><b>NumPy</b></td>
    <td align="center"><img src="https://go-skill-icons.vercel.app/api/icons?i=matplotlib" width="40"><br><b>Matplotlib</b></td>
    <td align="center"><img src="https://go-skill-icons.vercel.app/api/icons?i=tableau" width="40"><br><b>Tableau</b></td>
    <td align="center"><img src="https://img.shields.io/badge/-Power%20BI-F2C811?style=flat-square&logo=power-bi&logoColor=black" width="40"><br><b>Power BI</b></td>
  </tr>
</table>

### ML
<table>
  <tr>
    <td align="center"><img src="https://go-skill-icons.vercel.app/api/icons?i=tensorflow" width="40"><br><b>TensorFlow</b></td>
    <td align="center"><img src="https://go-skill-icons.vercel.app/api/icons?i=pytorch" width="40"><br><b>PyTorch</b></td>
    <td align="center"><img src="https://img.shields.io/badge/-PySpark-FDEE21?style=flat-square&logo=apache-spark&logoColor=black" width="40"><br><b>PySpark</b></td>
  </tr>
</table>

### Databases & Cloud
<table>
  <tr>
    <td align="center"><img src="https://go-skill-icons.vercel.app/api/icons?i=postgres" width="40"><br><b>PostgreSQL</b></td>
    <td align="center"><img src="https://img.shields.io/badge/-Databricks-FF3621?style=flat-square&logo=databricks&logoColor=white" width="40"><br><b>Databricks</b></td>
  </tr>
</table>

---

## Certifications
<table>
  <tr>
    <td align="center">
      <img src="materials/certification/tableau.png" width="180" alt="Tableau Desktop Specialist"><br>
      <b>Tableau Desktop Specialist</b>
    </td>
    <td align="center">
      <img src="materials/certification/Google%20Data%20Analytics.png" width="180" alt="Google Data Analytics"><br>
      <b>Google Data Analytics</b>
    </td>
  </tr>
</table>

---

## Project Details

### 1. Dynamic Portfolio Optimization (PortfolioAI)

| | |
| --- | --- |
| **Skills** | Python (TensorFlow), Variational LSTM, PostgreSQL, FastAPI, SQLAlchemy |
| **Outcome** | Live app with user interface for preference-driven stock portfolio allocations |
| **Link** | [PortfolioAI](https://github.com/StevenShi998/PortfolioAI) |

![PortfolioAI recommendation dashboard](materials/images/portfolio-ai-hero.png)

*Recommendation dashboard with allocation output and model-backed explanation.*

End-to-end web app that turns model output into user-facing recommendations: users set risk tolerance, market cap, sectors, and indicator preferences; the app returns backtested allocations and a plain-English explanation. Demonstrates data pipeline thinking, dashboard communication, and product-oriented analytics.

---

### 2. Bright Smiles Arizona Acquisition Screen

| | |
| --- | --- |
| **Skills** | Python (pandas), Power BI |
| **Outcome** | Top 50 pediatric shortlist and an interactive map dashboard |
| **Link** | [Bright-Smiles](Bright-Smiles) |

![Bright Smiles acquisition shortlist](materials/images/bright-smiles-hero.png)

*Ranked shortlist of pediatric offices and where those candidates sit on the map.*

![Bright Smiles Arizona market overview](materials/images/bright-smiles-market.png)

*Market overview: 3,000 offices, 480 pediatric, and the four largest brands set aside.*

Screened 3,000 Arizona dental offices for a kids' dentistry chain looking at acquisition targets. Kept pediatric offices outside the four largest brands, checked city enrollment against Census population, and scored 157 offices on child enrollment, kids per pediatric office, review-adjusted rating, and dentist count. The Power BI report joins that table to a map. Top office: Sunset Family Dental in Phoenix. The top 50 is a shortlist for a closer look, not a purchase price.

---

### 3. Custom CPI & Grocery Budget Analysis

| | |
| --- | --- |
| **Skills** | SQL, Python (pandas, numpy), Power BI |
| **Outcome** | 60-month trend, increase/decrease breakdown, interactive dashboard |
| **Link** | [Custom-CPI-Study](https://github.com/StevenShi998/Custom-CPI-Study) |

![Custom CPI monthly basket trend](materials/images/custom-cpi-hero.png)

*Monthly basket trend, period-over-period price change, and ratio of increase vs decrease months.*

![Custom CPI beef products](materials/images/custom-cpi-beef-products.png)

*Beef products: total price and price change, average monthly change, and product-level fluctuation.*

Uses Statistics Canada retail price data (2019–2024) to answer what led to the increase in grocery costs over five years.

---

### 4. StageTEN Marketing Analytics Showcase

| | |
| --- | --- |
| **Skills** | Google Analytics, Google Sheets, Python, HubSpot CRM, Canva |
| **Outcome** | Marketing insights, HubSpot workflow automation, email marketing |
| **Link** | [StageTEN](https://github.com/StevenShi998/StageTEN) |

![StageTEN campaign performance](materials/images/stage-ten-hero.png)

*Campaign/channel performance visual used in report-style marketing analysis.*

![StageTEN T.com commerce summary](materials/images/stage-ten-tgt-commerce.png)

*T.com commerce summary: unique/total interactions and after-checkout metrics across episodes (e.g. checkout conversion, revenue).*

Built marketing reporting (e.g., Empower By U vs. Shopify app downloader, TGT wrap) for a large retail and SaaS company. Used Python automation for HubSpot/Shopify tasks such as deal naming, amount/length prep, app-downloader list cleanup, and duplicate detection. Managed HubSpot for client retention and onboarding workflow automation. Created monthly newsletters and marketing emails.

---

### 5. UW Course Explorer

| | |
| --- | --- |
| **Skills** | SQL, Python (pandas, NumPy), Power BI |
| **Outcome** | Live site (uwtree.site), optimal path finder, depth and preference controls |
| **Link** | [UW-Course-SearchTree](https://github.com/StevenShi998/UW-Course-SearchTree) |

![UW Course Explorer graph view](materials/images/uw-course-hero.png)

*Interactive graph view for prerequisite paths and future course planning.*

Built an interactive prerequisite path planner for UW students. Uses graph traversal and optimization logic to recommend efficient course sequences based on constraints, preferences, and ratings. Live at uwtree.site.

---

### 6. Alchemy E-commerce Shop

| | |
| --- | --- |
| **Skills** | Email marketing, Adobe Lightroom, Adobe Photoshop, Shopify |
| **Outcome** | Live store, email campaigns, marketing content, $30k+ real revenue |
| **Link** | [Alchemy-E-commerce](https://github.com/StevenShi998/Alchemy-E-commerce) |

![Alchemy store hero](materials/images/alchemy-hero.png)

*Product display and brand creative shot from the live store.*

![Alchemy store creative](materials/images/alchemy-store2.png)

*Store creative: product display panels and brand storytelling.*

My own e-commerce store (alchemy1916.com). Built product photography, edited assets in Photoshop and Lightroom, and ran email campaigns and marketing posters to drive real sales—generating $30k+ in revenue.

---

### 7. FFT for Retail Cycle Detection

| | |
| --- | --- |
| **Skills** | Python, NumPy FFT, pandas, Matplotlib, PSD, inverse FFT |
| **Outcome** | Dominant cycle identification, raw vs smoothed charts, Jupyter notebook |
| **Link** | [Fast-Fourier-Transform](https://github.com/StevenShi998/Fast-Fourier-Transform) |

![FFT raw vs smoothed retail sales](materials/images/fft-hero.png)

*Raw monthly retail sales versus smoothed trend after frequency-domain filtering.*

Applies FFT and low-pass filtering to U.S. advance retail sales (FRED RSXFSN) to isolate the annual seasonal cycle and produce a smoothed series. Shows ability to use quantitative methods (spectral analysis, filtering) and translate them into business-friendly insights for campaign timing and planning.

---
