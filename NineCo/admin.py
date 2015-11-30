from django.contrib import admin
from NineCo.models import Carousel, Classification, GameClass, GameInfo, JobsInfo, News, NewsOfBus


class NewsAdmin(admin.ModelAdmin):

    class Media:
        js = (

            '/static/tinymce/tinymce.min.js',
            '/static/tinymce/config.js',

        )
admin.site.register(News, NewsAdmin)
admin.site.register(GameClass)
admin.site.register(GameInfo, NewsAdmin)
admin.site.register(JobsInfo, NewsAdmin)
admin.site.register(Carousel)
admin.site.register(Classification)
admin.site.register(NewsOfBus, NewsAdmin)
