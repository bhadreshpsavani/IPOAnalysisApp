import streamlit as st
import pandas as pd
from data.fetch_ipo_data import get_upcoming_ipos
from analysis.analyze_ipo import IPOAnalyzer

def render_dashboard(ipo_data, metrics, insights):
    st.title("Upcoming Indian IPOs Analysis")
    
    if ipo_data:
        # Display metrics
        st.header("Key Metrics")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total IPOs", metrics.get('total_ipos', 0))
        col2.metric("Avg Price", f"₹{metrics.get('average_price', 0):.2f}")
        col3.metric("Max Price", f"₹{metrics.get('max_price', 0):.2f}")
        
        # Display Data
        st.header("Upcoming IPO List")
        df = pd.DataFrame(ipo_data)
        st.dataframe(df)
        
        # Display insights
        st.header("Insights")
        for insight in insights:
            st.write(f"- {insight}")
    else:
        st.warning("No upcoming IPO data available. Please check your internet connection or try again later.")

if __name__ == "__main__":
    # For testing standalone
    data = get_upcoming_ipos()
    if data:
        analyzer = IPOAnalyzer(data)
        metrics = analyzer.calculate_metrics()
        insights = analyzer.generate_insights()
        render_dashboard(data, metrics, insights)
    else:
        st.write("No data found")