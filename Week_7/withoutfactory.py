class PaymentFactory:
    def process_payment(self,amount):
        return f"Processing payment of {amount}"
    
class StripePaymentFactory():
    def process_payment(self,amount):
        return f"Processing Stripe payment of {amount}"

class CreditCardPayment():
    def pay(self,amount):
        return f"Paying {amount} using Credit Card"
    
def checkout(payment_method,amount):
    if payment_method == "credit_card":
        payment_processor = PaymentFactory()
    elif payment_method == "stripe":
        payment_processor = StripePaymentFactory()
    else:
        raise ValueError("Unsupported payment method")
    
    return payment_processor.process_payment(amount)

def main():
    print(checkout("credit_card",100))
    print(checkout("stripe",200))

if __name__ == "__main__":
    main()