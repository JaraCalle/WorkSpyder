from django.db.models import Q

def filter_job_fairs(queryset, filters):
    """
    Filtra el queryset de JobFair según los parámetros dados.
    :param queryset: QuerySet inicial de JobFair.
    :param filters: Diccionario con los filtros aplicables.
    :return: QuerySet filtrado.
    """
    location = filters.get('location')
    event_date = filters.get('event_date')
    organizer = filters.get('organizer')
    title = filters.get('title')

    if location:
        queryset = queryset.filter(
            Q(department__icontains=location) |
            Q(city__icontains=location) |
            Q(direction__icontains=location)
        )
    if event_date:
        queryset = queryset.filter(
            Q(start_event_date__lte=event_date) & Q(end_event_date__gte=event_date)
        )
    if organizer:
        queryset = queryset.filter(organizer__email__icontains=organizer)
    if title:
        queryset = queryset.filter(title__icontains=title)

    return queryset
