from django.contrib import admin
from .models import Event, Participation
from django.utils import timezone

class ParticipationInline(admin.TabularInline):
    model = Participation
    extra = 1
    readonly_fields = ['participation_date']

class ParticipantCountFilter(admin.SimpleListFilter):
    title = 'Nombre de participants'
    parameter_name = 'participant_count'
    
    def lookups(self, request, model_admin):
        return [
            ('no_participants', 'No participants'),
            ('has_participants', 'There are participants'),
        ]
    
    def queryset(self, request, queryset):
        if self.value() == 'no_participants':
            return queryset.filter(nbe_participant=0)
        if self.value() == 'has_participants':
            return queryset.filter(nbe_participant__gt=0)
        return queryset

class EventDateFilter(admin.SimpleListFilter):
    title = 'Date de l\'événement'
    parameter_name = 'event_date'
    
    def lookups(self, request, model_admin):
        return [
            ('past', 'Past Events'),
            ('upcoming', 'Upcoming Events'),
            ('today', 'Today Events'),
        ]
    
    def queryset(self, request, queryset):
        today = timezone.now().date()
        if self.value() == 'past':
            return queryset.filter(evt_date__lt=today)
        if self.value() == 'upcoming':
            return queryset.filter(evt_date__gt=today)
        if self.value() == 'today':
            return queryset.filter(evt_date=today)
        return queryset

def make_accepted(modeladmin, request, queryset):
    queryset.update(state=True)
make_accepted.short_description = "Accepter les événements sélectionnés"

def make_refused(modeladmin, request, queryset):
    queryset.update(state=False)
make_refused.short_description = "Refuser les événements sélectionnés"

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    # AJOUTEZ search_fields pour autocomplete
    search_fields = ['title', 'description']
    
    list_display = [
        'title', 
        'category', 
        'evt_date', 
        'state', 
        'nbe_participant',
        'get_participant_count',
        'creation_date',
        'updated_date'
    ]
    
    readonly_fields = ['creation_date', 'updated_date']
    list_per_page = 10
    list_filter = [
        'title',
        ParticipantCountFilter,
        EventDateFilter,
        'category',
        'state'
    ]
    actions = [make_accepted, make_refused]
    autocomplete_fields = ['organizer']
    inlines = [ParticipationInline]
    
    fieldsets = (
        ('À propos', {
            'fields': ('title', 'description', 'image')
        }),
        ('Date', {
            'fields': ('evt_date', 'creation_date', 'updated_date')
        }),
        ('Autres', {
            'fields': ('category', 'state', 'nbe_participant')
        }),
        ('Personnel', {
            'fields': ('organizer',)
        })
    )
    
    def get_participant_count(self, obj):
        return obj.event_participations.count()  # Changez ici
    get_participant_count.short_description = 'Total Participants'

@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ['person', 'event', 'participation_date']
    list_filter = ['participation_date', 'event']
    autocomplete_fields = ['person', 'event']
    search_fields = ['person__cin', 'event__title']  # AJOUTEZ search_fields