import random
from datetime import datetime, timedelta

class EtsyGuardDemo:
    def __init__(self):
        self.demo_data = self._generate_sample_data()
        
    def _generate_sample_data(self):
        """Generate sample shop data"""
        return {
            "metrics": {
                "revenue": random.randint(1000, 5000),
                "visitors": random.randint(500, 2000),
                "conversion": random.uniform(2, 5),
                "avg_order": random.uniform(25, 45)
            },
            "products": [
                {"name": "Handmade Necklace", "views": 150, "sales": 12},
                {"name": "Custom Portrait", "views": 280, "sales": 8},
                {"name": "Digital Print", "views": 420, "sales": 25}
            ]
        }
    
    def show_analytics(self):
        """Display sample analytics dashboard"""
        print("\n🚀 EtsyGuard AI - Analytics Demo")
        print("=" * 50)
        
        metrics = self.demo_data["metrics"]
        print(f"\n📊 Shop Performance")
        print(f"Revenue: ${metrics['revenue']:,.2f}")
        print(f"Traffic: {metrics['visitors']:,} visitors")
        print(f"Conversion: {metrics['conversion']:.1f}%")
        print(f"Average Order: ${metrics['avg_order']:.2f}")
        
        print(f"\n📈 Top Products")
        for product in self.demo_data["products"]:
            print(f"- {product['name']}")
            print(f"  Views: {product['views']}")
            print(f"  Sales: {product['sales']}")
        
        print("\n💎 Get Full Access:")
        print("https://www.buymeacoffee.com/happyvibess")
        print("\nFull version includes:")
        print("- Real-time analytics")
        print("- Competitor tracking")
        print("- AI price optimization")
        print("- Advanced SEO tools")

def main():
    demo = EtsyGuardDemo()
    demo.show_analytics()

if __name__ == "__main__":
    main()
