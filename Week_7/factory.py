from abc import ABC, abstractmethod

class PaymentProcess(ABC):
    def Process_Payment(self):
        pass


class CreditCardPayment(PaymentProcess):
    def Process_Payment(self, amount):
        return f"Processing credit card payment of {amount}"
    
class StripePayment(PaymentProcess):
    def Process_Payment(self, amount):
        return f"Processing Stripe payment of {amount}"
    
class PayPalPayment(PaymentProcess):
    def Process_Payment(self, amount):
        return f"Processing PayPal payment of {amount}"
    
class PaymentProcesscorFactory:

    _processors = {
        "credit_card": CreditCardPayment,
        "stripe": StripePayment,
        "paypal": PayPalPayment,
    }

    @classmethod
    def create_processor(cls, payment_method):
        processor_cls = cls._processors.get(payment_method)
        if not processor_cls:
            raise ValueError(f"Unsupported payment method: {payment_method}")
        return processor_cls()
    
def checkout(payment_method, amount):
    processor = PaymentProcesscorFactory.create_processor(payment_method)
    return processor.Process_Payment(amount)

def main():
    print(checkout("credit_card", 100))
    print(checkout("stripe", 200))
    print(checkout("paypal", 300))

if __name__ == "__main__":
    main()
    