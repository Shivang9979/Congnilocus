from django.contrib import admin
from .models import CustomUser
from .models import QuizQuestion, Factor, Job, MultiFactorQuestion

admin.site.register(CustomUser)
admin.site.register(QuizQuestion)
admin.site.register(Factor)
admin.site.register(Job)
admin.site.register(MultiFactorQuestion)
