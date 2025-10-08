from django.contrib import admin,messages
from.models import Event,participation_event
from datetime import datetime
# Register your models here.
class ParticipationEvent(admin.TabularInline):
    model=participation_event
    extra=1
    readonly_field=('participation_date',)
    classes=['collapse']
class Date_Filter(admin.SimpleListFilter):
    title="Event Date"
    parameter_name='evt_date'
    def lookups(self, request, model_admin):
        return (
                ('PE',('Past Events')),
                ('UE',('Upcoming Events')),
                ('TE',('Today Events')))
    def queryset(self, request, queryset):
        if self.value()=='PE':
            return queryset.filter(evt_date__lt=datetime.today())
        if self.value()=='UE':
            return queryset.filter(evt_date__gt=datetime.today())
        if self.value()=='TE':
            return queryset.filter(evt_date__exact=datetime.today())
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    def accept_state(self,request,queryset):
        req=queryset.update(state=True)
        if (req==1):
            msg="1 event was"
        else:
            msg=f"{req} events were"
        messages.success(request,f"{msg} successfully updated")
    accept_state.short_description="State True"
    def reject_state(self,request,queryset):
        req=queryset.update(state=False)
        if (req==1):
            msg="1 event was"
        else:
            msg=f"{req} events were"
        messages.success(request,f"{msg} successfully updated")
    reject_state.short_description="State False"
    actions=[accept_state,reject_state]
    list_display=('title','description','state',
                  'evt_date','nbe_participant',
                  'creation_date','updated_date',
                  'organizer'
                  )
    list_per_page=1
    ordering=['title','-evt_date']
    search_fields=['title']
    list_filter=['title',Date_Filter]
    readonly_fields=['creation_date','updated_date']
    fieldsets=(
        ('A propos',{'fields':(
            'title','description','image','category'
        )}),
        ('Dates',{'fields':(
            'evt_date','creation_date','updated_date'
        )}),
        ('Etat',{'fields':('state',)}),
        (None,{'fields':('organizer','participation')})
    )
    autocomplete_fields=['organizer']
    inlines=[ParticipationEvent]
@admin.register(participation_event)
class Participation(admin.ModelAdmin):
    pass
# admin.site.register(Event,EventAdmin)