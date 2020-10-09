from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from photologue.admin import GalleryAdmin as GalleryAdminDefault
from photologue.admin import PhotoAdmin as PhotoAdminDefault
from photologue.models import Gallery, Photo

from .models import Play, Member, Award, Venue, PhotoExtended, GalleryExtended



class PhotoExtendedInline(admin.StackedInline):
    model = PhotoExtended
    can_delete = False

class PhotoAdmin(PhotoAdminDefault):
    """Define our new one-to-one model as an inline of Photologue's Gallery model."""

    inlines = [PhotoExtendedInline, ]

class GalleryExtendedInline(admin.StackedInline):
    model = GalleryExtended
    can_delete = False

class GalleryAdmin(GalleryAdminDefault):

    """Define our new one-to-one model as an inline of Photologue's Gallery model."""

    inlines = [GalleryExtendedInline, ]


class VenueAndAwardAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PlayAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    exclude = ('slug',)


class MemberAdmin(UserAdmin):
    model = Member
    list_display = ('username', 'email','first_name','last_name')

admin.site.register(Play, PlayAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Venue, VenueAndAwardAdmin)
admin.site.register(Award, VenueAndAwardAdmin)
admin.site.unregister(Gallery)
admin.site.register(Gallery, GalleryAdmin)
admin.site.unregister(Photo)
admin.site.register(Photo, PhotoAdmin)