from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from photologue.admin import GalleryAdmin as GalleryAdminDefault
from photologue.admin import PhotoAdmin as PhotoAdminDefault
from photologue.models import Gallery, Photo

from .forms import MemberCreationForm, MemberChangeForm
from .models import Play, Member, Award, Venue, PhotoExtended


class PhotoExtendedInline(admin.StackedInline):
    model = PhotoExtended
    can_delete = False


class PhotoAdmin(PhotoAdminDefault):

    inlines = [PhotoExtendedInline,]


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