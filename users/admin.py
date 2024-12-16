from django.contrib import admin
from .models import UserProfile, Wishlist, ReadingProgress, Bookmark
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Wishlist)
admin.site.register(ReadingProgress)
admin.site.register(Bookmark)
