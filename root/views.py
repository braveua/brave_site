from django.shortcuts import render, get_object_or_404


from .models import NbuCurrency, NbuRate
import random
from datetime import datetime, timedelta


def home(request):
    context = {
        "title": "Test Title",
        "random_number_from_api": random.randint(1, 100),
        "current_time": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
    }
    return render(request, "root/home.html", context=context)


def currency(request):
    curr = NbuCurrency.objects.all()
    return render(
        request,
        "root/currency.html",
        context={
            "curr": curr,
            "title": "Курсы валют НБУ",
            "current_time": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        },
    )


def currency_rates(request, currency_id):
    currency = get_object_or_404(NbuCurrency, id=currency_id)

    # Пример: за последние 30 дней
    end_date = datetime.today().date()
    start_date = end_date - timedelta(days=300)

    fd = datetime.now() - timedelta(days=10)
    td = datetime.now()

    rates = (
        NbuRate.objects.all()
        .filter(currencyid=currency, fromdate__range=(fd, td))
        .order_by("-fromdate")
    )

    context = {
        "currency": currency,
        "rates": rates,
        "title": f"Курс {currency.fname} за 30 дней",
        "start_date": start_date,
        "end_date": end_date,
    }
    return render(request, "root/currency_rates.html", context)

