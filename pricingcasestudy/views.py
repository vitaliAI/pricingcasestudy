from django.shortcuts import render, redirect

from quant.loan_calculator import LoanCalculator


# Create your views here.

def input(request):
    if not request.user.is_authenticated:
        return redirect('index')
    else:
        context = dict()
        if request.method == "POST":
            amount = int(request.POST.get('loan_amount'))
            period = float(request.POST.get('term'))
            apr = float(request.POST.get('apr'))
            start = int(request.POST.get('lending_date'))
            repayment = int(request.POST.get('repayment_date'))
            if period == 0:
                context = {"loan_payment": 0,
                           "total_credit": 0,
                           "total_interest": 0, }
                return render(request, 'pricingcasestudy/output.html', context)
            elif apr == 0:
                context = {"loan_payment": round(amount / period, 2),
                          "total_credit": amount,
                          "total_interest": 0, }
                return render(request, 'pricingcasestudy/output.html', context)
            else:
                loan_calc = LoanCalculator(amount, period, apr, start, repayment)
                context = {"loan_payment": loan_calc.loan_payment(),
                           "total_credit":loan_calc.total_credit(),
                           "total_interest": loan_calc.total_interest(),}
                return render(request, 'pricingcasestudy/output.html', context)
        return render(request, 'pricingcasestudy/input.html', context)



def results(request):
    if not request.user.is_authenticated:
        return redirect('index')
    else:
        context = dict()
        return render(request, 'pricingcasestudy/output.html', context)
