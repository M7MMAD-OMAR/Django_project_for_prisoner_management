from django.contrib import admin

from .models import Visits, Person, Convicts, Dungeon, Dungeon_Moves, Offense


# Register your models here.


class Person_Admin(admin.ModelAdmin):
    list_display = ['person_id', 'first_name', 'father', 'last_name', 'gender', 'birth_year', 'address']
    list_editable = ['first_name', 'father', 'last_name', 'gender', 'birth_year', 'address']
    search_fields = ['person_id', 'first_name', 'father', 'last_name', 'gender', 'birth_year', 'address']
    list_filter = ['first_name', 'gender', 'address']


class Offense_Admin(admin.ModelAdmin):
    list_display = ['offense_id', 'name']
    list_editable = ['name']
    search_fields = ['person_id', 'name']
    list_filter = ['name']


class Dungeon_Admin(admin.ModelAdmin):
    list_display = ['dungeon_id', 'name', 'size']
    list_editable = ['name', 'size']
    search_fields = ['dungeon_id', 'name', 'size']
    list_filter = ['name', 'size']


class Visits_Admin(admin.ModelAdmin):
    list_display = ['visits_id', 'date_visited', 'person_id', 'visitor_name', 'mount_in_minutes']
    list_editable = ['date_visited', 'person_id', 'visitor_name', 'mount_in_minutes']
    search_fields = ['visits_id', 'date_visited', 'person_id', 'visitor_name']
    list_filter = ['person_id', 'visitor_name']


class Convicts_Admin(admin.ModelAdmin):
    list_display = ['convicts_id', 'from_date', 'to_date', 'person_id', 'offense_id']
    list_editable = ['from_date', 'to_date', 'person_id', 'offense_id']
    search_fields = ['convicts_id', 'from_date', 'to_date', 'person_id', 'offense_id']
    list_filter = ['person_id', 'offense_id']


class Dungeon_Moves_Admin(admin.ModelAdmin):
    list_display = ['dungeon_moves_id', 'person_id', 'dungeon_id', 'from_date']
    list_editable = ['person_id', 'dungeon_id', 'from_date']
    search_fields = ['dungeon_moves_id', 'person_id', 'dungeon_id']
    list_filter = ['person_id', 'dungeon_id']


admin.site.register(Person, Person_Admin)
admin.site.register(Offense, Offense_Admin)
admin.site.register(Dungeon, Dungeon_Admin)
admin.site.register(Convicts, Convicts_Admin)
admin.site.register(Visits, Visits_Admin)
admin.site.register(Dungeon_Moves, Dungeon_Moves_Admin)
