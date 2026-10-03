# 🗽 NYC Airbnb Dynamic Pricing Engine

## 📌 Project Overview
This repository contains data-driven pricing engine designed specifically for the New York City rental market. The core objective of this project is to replace inefficient, static prices with an algorithmic pricing model. The engine dynamically optimizes nightly rates by interpreting market conditions which includes season multipliers, day-of-week premiums and last minute discounts

## 💰 Business Impact & ROI

To validate the financial viability of the algorithm, an A/B test simulation was conducted, comparing historical static pricing against generated dynamic rates. After strictly normalizing the baseline data to eliminate artificial outliers and extreme values, the financial simulation demonstrated a highly profitable outcome.

### Key Results:
* **Projected Revenue Increase:** The algorithmic pricing model generated **+5.34%** ROI compared to static approach


* **Strategic Market Responsiveness:** The engine successfully capitalizes on high-demand periods (e.g., summer peaks and holiday weekends) while strategically lowering baseline prices during off-peak windows.

### Visual Proof of Concept

*(Yearly seasonality)*
![Macro Trend - Yearly Seasonality](assets/yearly_trend.png)

*(July profit margin)*
![Micro Trend - July Profit Margin](assets/july_trend.png)

## 🛠 Tech Stack
* **Language:** Python 3.x
* **Data Processing:** Pandas, NumPy
* **Data Visualization:** Matplotlib


## 🚀 Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/Maci4nty/nyc_dynamic_pricing.git
   cd nyc_dynamic_pricing
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate # On Windows use: .venv\Scripts\activate
   ```

3. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute the pipeline:**
* Run the pricing engine: `python pricing_engine.py`
* Generate the A/B test reports and plots: `python business_impact.py`