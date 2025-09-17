from enum import Enum

class ProductType(Enum):
    metric= "Metric"
    view= "View"
    assist= "Assist"

class ProductSubscription(Enum):
    free= "Free"
    premium= "Premium"

PRODUCTS = {
    1: {
        "product_name": "Portfolio Valuation",
        "product_type": ProductType.metric,
        "product_subscription": ProductSubscription.free
    },
    2: {
        "product_name": "Portfolio Distribution",
        "product_type": ProductType.view,
        "product_subscription": ProductSubscription.free
    },
    3: {
        "product_name": "Portfolio Assistance",
        "product_type": ProductType.assist,
        "product_subscription": ProductSubscription.premium
    }
}