from django.contrib import admin
from .models import ShortlistedCandiateModel,CreateNewJobModel,TechnicalTeamModel,OfflineCandiateModel,ScheduledCandiateModel


admin.site.register(ShortlistedCandiateModel)
admin.site.register(CreateNewJobModel)
# Register your models here.
admin.site.register(TechnicalTeamModel)
admin.site.register(OfflineCandiateModel)
admin.site.register(ScheduledCandiateModel)
