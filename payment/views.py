from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from order.models import Order
from .darghah import send_request, verify_payment


@login_required
def payment(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    result = send_request(order)

    if result["status"]:
        return redirect(result["url"])

    return render(
        request,
        "payment/error.html",
        {
            "error": result["message"]
        }
    )


@login_required
def verify(request):

    authority = request.GET.get("Authority")
    status = request.GET.get("Status")

    order = get_object_or_404(
        Order,
        authority=authority,
        user=request.user
    )

    if status == "OK":

        if verify_payment(order, authority):

            return render(
                request,
                "payment/success.html",
                {
                    "order": order
                }
            )

    return render(request, "payment/failed.html")


