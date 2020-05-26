from django.contrib import admin
from .models import Profile,EdudetailsModel,CompanyDetailsModel,PersonalDetailsModel,SkillSetDetailsModel,Permission


admin.site.register(Profile)
admin.site.register(EdudetailsModel)
admin.site.register(CompanyDetailsModel)
admin.site.register(PersonalDetailsModel)
admin.site.register(SkillSetDetailsModel)
admin.site.register(Permission)
