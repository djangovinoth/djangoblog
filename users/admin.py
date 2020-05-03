from django.contrib import admin
from .models import Profile,EdudetailsModel,CompanyDetailsModel,PersonalDetailsModel,SkillSetDetailsModel,PermissionModel


admin.site.register(Profile)
admin.site.register(EdudetailsModel)
admin.site.register(CompanyDetailsModel)
admin.site.register(PersonalDetailsModel)
admin.site.register(SkillSetDetailsModel)
admin.site.register(PermissionModel)
