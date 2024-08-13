from mainApp.models import account
def message_processor(request):
    var=account.objects.get(id=1)
    softSkills = var.skills_set.filter(category='Software Programming Skills')
    designSkills = var.skills_set.filter(category='Design')
    osSkills = var.skills_set.filter(category=' Operating Systems')
    editorSkills = var.skills_set.filter(category='Editors')
    ideSkills = var.skills_set.filter(category='IDEs')
    return {"account":var,"softSkills":softSkills,"designSkills":designSkills,"osSkills":osSkills,"editorSkills":editorSkills,"ideSkills":ideSkills}


