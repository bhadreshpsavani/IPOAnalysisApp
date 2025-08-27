from streamlit import st
from data.fetch_ipo_data import get_upcoming_ipos
from analysis.analyze_ipo import IPOAnalyzer

def main():
    st.title("Upcoming Indian IPOs Analysis")
    
    # Fetch upcoming IPO data
    ipo_data = get_upcoming_ipos()
    
    if ipo_data:
        # Analyze the IPO data
        analyzer = IPOAnalyzer(ipo_data)
        metrics = analyzer.calculate_metrics()
        insights = analyzer.generate_insights()
        
        # Display metrics
        st.header("IPO Metrics")
        st.write(metrics)
        
        # Display insights
        st.header("Insights")
        st.write(insights)
    else:
        st.warning("No upcoming IPO data available.")

if __name__ == "__main__":
    main()