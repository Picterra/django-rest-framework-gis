from django.urls import path

from . import views

urlpatterns = [
    path('', views.location_list, name='api_location_list'),
    path('<int:pk>', views.location_details, name='api_location_details'),
    # geojson
    path('geojson/', views.geojson_location_list, name='api_geojson_location_list'),
    path(
        'geojson_writable_id/',
        views.geojson_location_writable_id_list,
        name='api_geojson_location_writable_id_list',
    ),
    path(
        'geojson/<int:pk>/',
        views.geojson_location_details,
        name='api_geojson_location_details',
    ),
    path(
        'geojson-nullable/<int:pk>/',
        views.geojson_nullable_details,
        name='api_geojson_nullable_details',
    ),
    path(
        'geojson_hidden/<int:pk>/',
        views.geojson_location_details_hidden,
        name='api_geojson_location_details_hidden',
    ),
    path(
        'geojson_none/<int:pk>/',
        views.geojson_location_details_none,
        name='api_geojson_location_details_none',
    ),
    path(
        'geojson/<slug:slug>/',
        views.geojson_location_slug_details,
        name='api_geojson_location_slug_details',
    ),
    path(
        'geojson-falseid/<int:pk>/',
        views.geojson_location_falseid_details,
        name='api_geojson_location_falseid_details',
    ),
    path(
        'geojson-noid/<int:pk>/',
        views.geojson_location_noid_details,
        name='api_geojson_location_noid_details',
    ),
    # file
    path(
        'geojson-file/<int:pk>/',
        views.geojson_located_file_details,
        name='api_geojson_located_file_details',
    ),
    # geojson with bbox with its own geometry field
    path(
        'geojson-with-bbox/',
        views.geojson_boxedlocation_list,
        name='api_geojson_boxedlocation_list',
    ),
    path(
        'geojson-with-bbox/<int:pk>/',
        views.geojson_boxedlocation_details,
        name='api_geojson_boxedlocation_details',
    ),
    # geojson with bbox with autogenerated bbox
    path(
        'geojson-with-auto-bbox/',
        views.geojson_location_bbox_list,
        name='api_geojson_location_bbox_list',
    ),
    # Filters
    path(
        'filters/contained_in_bbox',
        views.geojson_location_contained_in_bbox_list,
        name='api_geojson_location_list_contained_in_bbox_filter',
    ),
    path(
        'filters/overlaps_bbox',
        views.geojson_location_overlaps_bbox_list,
        name='api_geojson_location_list_overlaps_bbox_filter',
    ),
    path(
        'filters/contained_in_geometry',
        views.geojson_contained_in_geometry,
        name='api_geojson_contained_in_geometry',
    ),
    path(
        'filters/contained_in_tile',
        views.geojson_location_contained_in_tile_list,
        name='api_geojson_location_list_contained_in_tile_filter',
    ),
    path(
        'filters/overlaps_tile',
        views.geojson_location_overlaps_tile_list,
        name='api_geojson_location_list_overlaps_tile_filter',
    ),
    path(
        'filters/within_distance_of_point',
        views.geojson_location_within_distance_of_point_list,
        name='api_geojson_location_list_within_distance_of_point_filter',
    ),
    path(
        'filters/within_degrees_of_point',
        views.geojson_location_within_degrees_of_point_list,
        name='api_geojson_location_list_within_degrees_of_point_filter',
    ),
    path(
        'filters/order_distance_to_point',
        views.geojson_location_order_distance_to_point_list,
        name='api_geojson_location_order_distance_to_point_list_filter',
    ),
]
