from mainApp.models import account
def user_processor(request):
    var=account.objects.get(id=1)

    return {"account":var}

def skills_processor(request):
    var=account.objects.get(id=1)

    softSkills = var.skills_set.filter(category='Software Programming Skills')
    designSkills = var.skills_set.filter(category='Design')
    osSkills = var.skills_set.filter(category=' Operating Systems')
    editorSkills = var.skills_set.filter(category='Editors')
    ideSkills = var.skills_set.filter(category='IDEs')
    return {"softSkills":softSkills,"designSkills":designSkills,"osSkills":osSkills,"editorSkills":editorSkills,"ideSkills":ideSkills}
def education_processor(request):
    var=account.objects.get(id=1)
    educationList = var.education_set.all().order_by('-startDate')
    return {"educationList":educationList}
def honors_processor(request):
    var=account.objects.get(id=1)
    honorsList = var.honorsandawards_set.all().order_by('-date')
    return {"honorsList":honorsList}

def images_processor(request):
    var=account.objects.get(id=1)
    imagesList = var.imagesmodel_set.all()
    return {"imagesList":imagesList}
def competation_processor(request):
    var=account.objects.get(id=1)
    competationList = var.competations_set.all().order_by('-date')
    return {"competationList":competationList}

