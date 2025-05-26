from django.shortcuts import render

# Create your views here.
def home(request):
    message = ""
    if request.method == "POST":
        jmeno = request.POST.get("jmeno")
        zprava = request.POST.get("zprava")
        message = f"Děkujeme, {jmeno}, tvoje zpráva byla odeslána!"
    return render(request, 'home.html', {"message": message})