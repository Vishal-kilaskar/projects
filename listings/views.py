from django.shortcuts import render, get_object_or_404
from .models import Listing
from .choices import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 2)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    single_listing = get_object_or_404(Listing, pk=listing_id)
    context = {'listing': single_listing}
    return render(request, 'listings/listing.html', context)


def search(request):
    search_listing = Listing.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET.get('keywords')
        if keywords:
            search_listing = search_listing.filter(description__icontains=keywords)
    if 'city' in request.GET:
        city = request.GET.get('city')
        if city:
            search_listing = search_listing.filter(city__iexact=city)
    if 'state' in request.GET:
        state = request.GET.get('state')
        if state:
            search_listing = search_listing.filter(state__iexact=state)
    if 'bedrooms' in request.GET:
        bedrooms = request.GET.get('bedrooms')
        if bedrooms:
            search_listing = search_listing.filter(bedrooms__lte=bedrooms)
    if 'price' in request.GET:
        price = request.GET.get('price')
        if price:
            search_listing = search_listing.filter(price__lte=price)
    context = {
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'listings': search_listing,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
