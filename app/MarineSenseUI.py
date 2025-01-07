import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# import your MarineSense modules (e.g., scenario orchestrator, agent orchestrators)
# from marinesense.orchestrators.forecast_orchestrator import run_forecast_orchestrator
# from marinesense.orchestrators.scenario_orchestrator import run_scenario
# from marinesense.analysis_agents.iron_ore import IronOreAgent
# etc.

def main():
    st.set_page_config(page_title="MarineSense Dashboard", layout="wide")
    st.title("MarineSense Dashboard")

    # 1. Market Overview Section
    market_overview_section()

    # 2. Forecast Chart with Baseline vs. Adjusted
    forecast_chart_section()

    # 3. Agent Distributions
    agent_distributions_section()

    # 4. Scenario & Input Controls
    scenario_input_controls_section()

    # 5. Forecast Output & Actionable Insights
    forecast_output_section()


def market_overview_section():
    st.subheader("Market Overview")

    # Example: Show a world map image or Plotly map
    st.image("https://i0.wp.com/porteconomicsmanagement.org/wp-content/uploads/Map-Strategic-Passages.png",
             caption="World Map Showing Key Routes", use_column_width=True)

    # Possibly a route dropdown
    selected_route = st.selectbox("Select a route", ("C3", "C5"))
    st.write(f"Selected route: {selected_route}")

def forecast_chart_section():
    st.subheader("Baseline & Adjusted Forecast")

    # Example: Generate or retrieve data
    df = generate_mock_forecast_data()  # function or retrieval from orchestrator

    # Plot with Plotly
    fig = px.line(df, x="month", y=["baseline", "adjusted"], markers=True)
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

def agent_distributions_section():
    st.subheader("Agent Distributions")

    # Example: Show 3 “agent distribution” plots side by side
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("Iron Ore Agent")
        # mock data
        df_iron = generate_distribution_data(skew=-2, scale=1.2)
        fig_iron = px.area(df_iron, x="x", y="y")
        st.plotly_chart(fig_iron, use_container_width=True)
        trust_iron = st.slider("Trust: Iron Ore Agent", 0, 100, 80, 1)

    with col2:
        st.write("Coal Agent")
        df_coal = generate_distribution_data(skew=1, scale=0.8)
        fig_coal = px.bar(df_coal, x="x", y="y")
        st.plotly_chart(fig_coal, use_container_width=True)
        trust_coal = st.slider("Trust: Coal Agent", 0, 100, 70, 1)

    with col3:
        st.write("Economic Trends Agent")
        df_econ = generate_distribution_data(skew=0, scale=1.5)
        fig_econ = px.line(df_econ, x="x", y="y")
        st.plotly_chart(fig_econ, use_container_width=True)
        trust_econ = st.slider("Trust: Econ Agent", 0, 100, 90, 1)

    # In a real system, you’d store trust values in session state or pass them to your orchestrators.

def scenario_input_controls_section():
    st.subheader("Scenario & Input Controls")

    st.write("### Commodity Demand Adjustments")
    iron_ore_demand = st.slider("Iron Ore Demand: ", min_value=-10, max_value=10, value=0)
    coal_demand = st.slider("Coal Demand: ", -10, 10, 0)
    construction_demand = st.slider("Construction Materials Demand: ", -10, 10, 0)

    st.write("### Black Swan Event Planner")
    black_swan_month = st.number_input("Trigger event at month", min_value=1, max_value=24, value=6)
    black_swan_type = st.selectbox("Choose scenario type", ["Port Closure", "Regulatory Shock", "Infrastructure Failure"])
    black_swan_desc = st.text_input("Scenario description")

    # Typically, you’d incorporate these inputs into your scenario orchestrator calls

def forecast_output_section():
    st.subheader("Forecast Output & Actionable Insights")

    # Mock data for a table
    baseline_forecasts = [12000, 8400]
    adjusted_forecasts = [12500, 8100]
    confidences = ["High", "Medium"]
    recommended_actions = ["Consider early FFA", "Monitor Iron Ore"]
    routes = ["C3", "C5"]

    df_output = pd.DataFrame({
        "Route": routes,
        "Baseline Forecast": baseline_forecasts,
        "Adjusted Forecast": adjusted_forecasts,
        "Confidence": confidences,
        "Recommended Action": recommended_actions
    })
    st.table(df_output)

    st.write("**Recommendations:**")
    st.write("- Given your input adjustments:")
    st.write("    - Consider securing forward contracts for Route C3 due to predicted volatility.")
    st.write("    - Evaluate hedging strategies on C5 to mitigate uncertainty.")
    st.write("    - Monitor potential black swan events and adjust strategies accordingly.")

############################################
# Mock Data Generation Functions
############################################

def generate_mock_forecast_data():
    months = [f"Month {i}" for i in range(1, 13)]
    baseline_vals = np.linspace(5000, 7000, 12)
    adjusted_vals = baseline_vals + np.random.normal(0, 300, 12)
    return pd.DataFrame({
        "month": months,
        "baseline": baseline_vals,
        "adjusted": adjusted_vals
    })

def generate_distribution_data(skew=0, scale=1):
    x_vals = np.arange(0, 20)
    # Arbitrary math for shape
    y_vals = np.exp(-((x_vals - 10 + skew) * scale) ** 2 / 20)
    df = pd.DataFrame({"x": x_vals, "y": y_vals})
    return df

if __name__ == "__main__":
    main()
