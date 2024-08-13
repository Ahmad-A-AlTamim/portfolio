from mainApp.models import account
def message_processor(request):
    var=account.objects.get(id=1)
    return {"account":var}

