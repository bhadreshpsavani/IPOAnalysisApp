import streamlit as st
from data.fetch_ipo_data import get_upcoming_ipos
from analysis.analyze_ipo import IPOAnalyzer
from dashboard.dashboard import render_dashboard

def main():
    st.title("Upcoming Indian IPOs Analysis")
    
    # Fetch upcoming IPO data
    ipo_data = get_upcoming_ipos()
    
    # Analyze the IPO data
    analyzer = IPOAnalyzer(ipo_data)
    metrics = analyzer.calculate_metrics()
    insights = analyzer.generate_insights()
    
    # Render the dashboard
    render_dashboard(ipo_data, metrics, insights)

if __name__ == "__main__":
    main()