from django.urls import path # type: ignore
# from .views import get_user, CreateSuperAdminView, AboutUsView, AboutUsPageContentView, AboutUsPageContentWithImgView, HeaderInfoView, SliderBelowSectionView, FooterView, HomeAboutUsView, HomeProductsView, HomePromotionalVideoView
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    get_user,
    CreateSuperAdminView,
    AboutUsView,
    AboutUsPageContentView,
    AboutUsPageContentWithImgView,
    HeaderInfoView,
    SliderBelowSectionView,
    FooterView,
    HomeAboutUsView,
    HomeProductsView,
    HomePromotionalVideoView,
    AboutUsPageView,
    MissionVisionPageView,
    ProductCreateView,
    ProductListView,
    ProductDetailView,
    ProductsAddDetailView,
    ActiveProductListView,
    ContactPageView,
    DistributionPageView,
    CylinderPageView,
    BulkPageView,
    SliderView,
    BoardOfDirectorListCreateView,
    BoardOfDirectorDetailView,
    ReticulationPageView,
    FaqAddView,
    CylinderLPGasProductsAddListCreateView,
    CylinderLPGasProductsAddDetailView,
    OrderCreateView,
    OrderListView
)




# Full Link should be -> http://127.0.0.1:8000/api/users/
# Admin Dashboard link -> http://127.0.0.1:8000/admin/
# Admin -> user : admin -> pass : 123456

urlpatterns = [


    path('users/', get_user, name='get_user'),
    path('create-super-admin/', CreateSuperAdminView.as_view(), name='create_super_admin'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),

    # About us page content
    path('about-us-page/', AboutUsPageView.as_view(), name='about-us-page'),
    path('about-us-page-content/', AboutUsPageContentView.as_view(), name='about-us-page-content'),
    path('about-us-page-content-with-img/', AboutUsPageContentWithImgView.as_view(), name='about-us-page-content-with-img'),

    # --- page content change API --- #
    path('header-info/', HeaderInfoView.as_view(), name='header-info'),
    path('slider-below-section/', SliderBelowSectionView.as_view(), name='slider-below-section'),
    path('footer/', FooterView.as_view(), name='footer'),
    path('home-about-us/', HomeAboutUsView.as_view(), name='home-about-us'),
    path('home-products/', HomeProductsView.as_view(), name='home-products'),
    path('home-promotional-video/', HomePromotionalVideoView.as_view(), name='home-promotional-video'),
    
    
    path('mission-vision/', MissionVisionPageView.as_view(), name='mission-vision'),

    # path('product-add/', ProductsAddView.as_view(), name='product-add'),
    path('product-add/', ProductCreateView.as_view(), name='product-add'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/<int:pk>/', ProductsAddDetailView.as_view(), name='product-detail'),
    path('active-product-list/', ActiveProductListView.as_view(), name='active-product-list'),

    path('cylinder-lpg-products/', CylinderLPGasProductsAddListCreateView.as_view(), name='cylinder-lpg-products-list-create'),
    path('cylinder-lpg-products/<int:pk>/', CylinderLPGasProductsAddDetailView.as_view(), name='cylinder-lpg-products-detail'),

    #  --- Product Order --- #
    path('order-create/', OrderCreateView.as_view(), name='order-create'),
    path('order-list/', OrderListView.as_view(), name='order-list'),  # optional



    path('contact-page/', ContactPageView.as_view(), name='contact-page'),
    path('distribution-page/', DistributionPageView.as_view(), name='distribution-page'),
    path('cylinder-page/', CylinderPageView.as_view(), name='cylinder-page'),
    path('bulk-page/', BulkPageView.as_view(), name='bulk-page'),
    path('sliders/', SliderView.as_view(), name='slider-crud'),

    # --- Board of Directors --- #
    path('board-of-directors/', BoardOfDirectorListCreateView.as_view(), name='board_of_directors'),
    path('board-of-directors/<int:pk>/', BoardOfDirectorDetailView.as_view(), name='board_of_director_detail'),
    path('reticulation-page/', ReticulationPageView.as_view(), name='reticulation-page'),
    # --- Faq Add Question and Answer --- #
    path('faq-add/', FaqAddView.as_view(), name='faq-add'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


