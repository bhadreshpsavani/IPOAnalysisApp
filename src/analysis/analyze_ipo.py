import re

class IPOAnalyzer:
    def __init__(self, ipo_data):
        self.ipo_data = ipo_data

    def _parse_price(self, price_str):
        """
        Parses price string to extract the maximum price.
        Example: "100-120" -> 120.0, "100" -> 100.0
        """
        try:
            # Remove "Rs" and other non-numeric chars except hyphen and dot
            clean_str = re.sub(r'[^\d\.-]', '', price_str)
            if '-' in clean_str:
                parts = clean_str.split('-')
                return float(parts[-1])
            return float(clean_str)
        except (ValueError, TypeError):
            return 0.0

    def calculate_metrics(self):
        metrics = {}
        if not self.ipo_data:
            return metrics
            
        prices = [self._parse_price(ipo.get('issue_price', '0')) for ipo in self.ipo_data]
        prices = [p for p in prices if p > 0]
        
        if prices:
            metrics['average_price'] = sum(prices) / len(prices)
            metrics['min_price'] = min(prices)
            metrics['max_price'] = max(prices)
        else:
            metrics['average_price'] = 0
            metrics['min_price'] = 0
            metrics['max_price'] = 0
            
        metrics['total_ipos'] = len(self.ipo_data)
        return metrics

    def generate_insights(self):
        insights = []
        if not self.ipo_data:
            return ["No IPO data available for analysis."]
            
        metrics = self.calculate_metrics()
        insights.append(f"Total upcoming IPOs: {metrics.get('total_ipos', 0)}")
        
        if metrics.get('average_price', 0) > 0:
            insights.append(f"Average Issue Price: ₹{metrics['average_price']:.2f}")
            
        # Example insight based on lot size if available
        for ipo in self.ipo_data[:5]: # Top 5
            name = ipo.get('name', 'Unknown')
            price = ipo.get('issue_price', 'N/A')
            insights.append(f"{name}: Issue Price {price}")
            
        return insights