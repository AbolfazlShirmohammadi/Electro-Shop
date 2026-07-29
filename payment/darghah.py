import requests

MERCHANT_ID = "YOUR_MERCHANT_ID"

REQUEST_URL = "https://payment.zarinpal.com/pg/v4/payment/request.json"
VERIFY_URL = "https://payment.zarinpal.com/pg/v4/payment/verify.json"
START_PAY = "https://payment.zarinpal.com/pg/StartPay/"


def send_request(order):

    callback_url = f"http://127.0.0.1:8000/payment/verify/"

    data = {
        "merchant_id": MERCHANT_ID,
        "amount": order.total_price,
        "callback_url": callback_url,
        "description": f"Order #{order.id}",
    }

    response = requests.post(
        REQUEST_URL,
        json=data
    )

    result = response.json()

    if result["data"]["code"] == 100:

        authority = result["data"]["authority"]

        order.authority = authority
        order.save()

        return {
            "status": True,
            "url": START_PAY + authority
        }

    return {
        "status": False,
        "message": result["errors"]
    }


def verify_payment(order, authority):

    data = {
        "merchant_id": MERCHANT_ID,
        "amount": order.total_price,
        "authority": authority
    }

    response = requests.post(
        VERIFY_URL,
        json=data
    )

    result = response.json()

    if result["data"]["code"] == 100:

        order.status = "paid"
        order.ref_id = result["data"]["ref_id"]
        order.save()

        return True

    return False