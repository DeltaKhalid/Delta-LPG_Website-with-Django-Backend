from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from decimal import Decimal
from django.db import models
from django.core.exceptions import ValidationError

# from .models import AboutUs, AboutUsPageContent, AboutUsPageContentWithImg, HeaderInfo, SliderBelowSection, Footer, HomeAboutUs, HomeProducts, HomePromotionalVideo
from .models import (
    AboutUs,
    AboutUsPageContent,
    AboutUsPageContentWithImg,
    HeaderInfo,
    SliderBelowSection,
    Footer,
    HomeAboutUs,
    HomeProducts,
    HomePromotionalVideo,
    AboutUsPage,
    MissionVisionPage,
    ProductsAdd,
    ProductsAddList,
    ContactPage,
    DistributionPage,
    CylinderPage,
    BulkPage,
    Slider,
    BoardOfDirector,
    ReticulationPage,
    FaqAdd,
    CylinderLPGasProductsAdd,
    SalesOrder, 
    SalesOrderItem,
)


from django.utils.functional import SimpleLazyObject  # ✅ Add this
from django.shortcuts import redirect
from django.urls import reverse 

# --- Custom User Admin API --- #
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    search_fields = ('username', 'email')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)



# --- About Us Text Change API --- #
@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['content']

# --- Header Info --- #
@admin.register(HeaderInfo)
class HeaderInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'office_time', 'call_any_time', 'logo_preview')

    def logo_preview(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" style="height: 40px;" />')
        return "No logo"
    logo_preview.short_description = 'Logo'

    def has_add_permission(self, request):
        # Block add if there's already one record
        return not HeaderInfo.objects.exists()

    def changelist_view(self, request, extra_context=None):
        # If only one HeaderInfo object exists, redirect to its change page
        obj = HeaderInfo.objects.first()
        if obj:
            return redirect(
                reverse("admin:api_headerinfo_change", args=(obj.id,))
            )
        return super().changelist_view(request, extra_context=extra_context)

# --- Slider below Section --- #
@admin.register(SliderBelowSection)
class SliderBelowSectionAdmin(admin.ModelAdmin):
    list_display = ('text_01', 'text_02', 'text_03')

    def has_add_permission(self, request):
        # Block adding if one already exists
        return not SliderBelowSection.objects.exists()

    def changelist_view(self, request, extra_context=None):
        # If only one exists, redirect to edit view
        obj = SliderBelowSection.objects.first()
        if obj:
            return redirect(
                reverse("admin:api_sliderbelowsection_change", args=(obj.id,))
            )
        return super().changelist_view(request, extra_context=extra_context)

# --- Footer Section --- #
@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'footer_credits_text')

    def has_add_permission(self, request):
        # Only allow adding if no record exists
        return not Footer.objects.exists()

    def changelist_view(self, request, extra_context=None):
        obj = Footer.objects.first()
        if obj:
            return redirect(reverse("admin:api_footer_change", args=(obj.id,)))
        return super().changelist_view(request, extra_context=extra_context)

# --- Home About Us --- #
@admin.register(HomeAboutUs)
class HomeAboutUsAdmin(admin.ModelAdmin):
    list_display = ('title_01', 'title_02')

    def has_add_permission(self, request):
        return not HomeAboutUs.objects.exists()

    def changelist_view(self, request, extra_context=None):
        obj = HomeAboutUs.objects.first()
        if obj:
            return redirect(
                reverse("admin:api_homeaboutus_change", args=(obj.id,))
            )
        return super().changelist_view(request, extra_context=extra_context)

# --- Home Page Products Show --- #

@admin.register(HomeProducts)
class HomeProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'headline')

    def has_add_permission(self, request):
        return not HomeProducts.objects.exists()

    def changelist_view(self, request, extra_context=None):
        obj = HomeProducts.objects.first()
        if obj:
            return redirect(
                reverse("admin:api_homeproducts_change", args=(obj.id,))
            )
        return super().changelist_view(request, extra_context=extra_context)

# --- Home Page Promotional Video --- #
@admin.register(HomePromotionalVideo)
class HomePromotionalVideoAdmin(admin.ModelAdmin):
    list_display = ('video_link',)

    def has_add_permission(self, request):
        return not HomePromotionalVideo.objects.exists()

    def changelist_view(self, request, extra_context=None):
        obj = HomePromotionalVideo.objects.first()
        if obj:
            return redirect(reverse("admin:api_homepromotionalvideo_change", args=(obj.id,)))
        return super().changelist_view(request, extra_context=extra_context)
    
# --- About Us Page --- #
@admin.register(AboutUsPage)
class AboutUsPageAdmin(admin.ModelAdmin):
    list_display = ('title',)

    def has_add_permission(self, request):
        return not AboutUsPage.objects.exists()

    def changelist_view(self, request, extra_context=None):
        obj = AboutUsPage.objects.first()
        if obj:
            return redirect(
                reverse("admin:api_aboutuspage_change", args=(obj.id,))
            )
        return super().changelist_view(request, extra_context=extra_context)

# --- Mission & Vision Page --- #
@admin.register(MissionVisionPage)
class MissionVisionPageAdmin(admin.ModelAdmin):
    list_display = ('title1', 'title2')

    def has_add_permission(self, request):
        return not MissionVisionPage.objects.exists()

    def changelist_view(self, request, extra_context=None):
        obj = MissionVisionPage.objects.first()
        if obj:
            return redirect(
                reverse("admin:api_missionvisionpage_change", args=(obj.id,))
            )
        return super().changelist_view(request, extra_context=extra_context)

# --- Products Add --- #
@admin.register(ProductsAdd)
class ProductsAddAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_code', 'short_description', 'product_status', 'image_tag')
    list_editable = ('product_status',)  # Editable status in list view
    search_fields = ('product_name', 'product_code')
    readonly_fields = ('image_tag',)

    def short_description(self, obj):
        return (obj.product_description[:50] + "...") if len(obj.product_description) > 50 else obj.product_description
    short_description.short_description = "Description"

    def image_tag(self, obj):
        if obj.product_img:
            return format_html('<img src="{}" width="60" height="60" style="object-fit:cover;"/>', obj.product_img.url)
        return "-"
    image_tag.short_description = 'Image Preview'


# @admin.register(ProductsAdd)
# class ProductsAddAdmin(admin.ModelAdmin):
#     list_display = ('product_name', 'product_code', 'short_description','product_status', 'image_tag')
#     search_fields = ('product_name', 'product_code')
#     readonly_fields = ('image_tag',)

#     def short_description(self, obj):
#         return (obj.product_description[:50] + "...") if len(obj.product_description) > 50 else obj.product_description
#     short_description.short_description = "Description"

#     def image_tag(self, obj):
#         if obj.product_img:
#             return format_html('<img src="{}" width="60" height="60" style="object-fit:cover;"/>', obj.product_img.url)
#         return "-"
#     image_tag.short_description = 'Image Preview'





# --- Product List --- #
@admin.register(ProductsAddList)
class ProductsAddListAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_code', 'short_description', 'image_tag')
    search_fields = ('product_name', 'product_code')
    readonly_fields = ('image_tag',)
    

    def short_description(self, obj):
        return (obj.product_description[:50] + "...") if len(obj.product_description) > 50 else obj.product_description
    short_description.short_description = "Description"

    def image_tag(self, obj):
        if obj.product_img:
            return format_html('<img src="{}" width="60" height="60" style="object-fit:cover;"/>', obj.product_img.url)
        return "-"
    image_tag.short_description = 'Image Preview'

# --- Contact Page --- #
@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('office_1_name', 'office_1_email')

    def has_add_permission(self, request):
        # Block add if there's already one record
        return not ContactPage.objects.exists()

    def changelist_view(self, request, extra_context=None):
        obj = ContactPage.objects.first()
        if obj:
            return redirect(reverse("admin:api_contactpage_change", args=(obj.id,)))
        return super().changelist_view(request, extra_context=extra_context)





# @admin.register(ContactPage)
# class ContactPageAdmin(admin.ModelAdmin):
#     list_display = ('phone_number_1', 'email_1')

#     def has_add_permission(self, request):
#         # Block add if there's already one record
#         return not ContactPage.objects.exists()

#     def changelist_view(self, request, extra_context=None):
#         # If only one ContactPage object exists, redirect to its change page
#         obj = ContactPage.objects.first()
#         if obj:
#             return redirect(
#                 reverse("admin:api_contactpage_change", args=(obj.id,))
#             )
#         return super().changelist_view(request, extra_context=extra_context)





# @admin.register(ContactPage)
# class ContactPageAdmin(admin.ModelAdmin):
#     list_display = ('phone_number_1', 'email_1')

#     def has_add_permission(self, request):
#         # Only allow one instance
#         return not ContactPage.objects.exists()

#     def changelist_view(self, request, extra_context=None):
#         obj = ContactPage.objects.first()
#         if obj:
#             return redirect(
#                 reverse("admin:api_contactpage_change", args=(obj.id,))
#             )
#         return super().changelist_view(request, extra_context=extra_context)

# --- Distribution Page --- #
@admin.register(DistributionPage)
class DistributionPageAdmin(admin.ModelAdmin):
    list_display = ('title_one', 'headline_one')

    def has_add_permission(self, request):
        return not DistributionPage.objects.exists()

    def changelist_view(self, request, extra_context=None):
        obj = DistributionPage.objects.first()
        if obj:
            return redirect(
                reverse("admin:api_distributionpage_change", args=(obj.id,))
            )
        return super().changelist_view(request, extra_context=extra_context)

# --- Cylinder Page --- #
@admin.register(CylinderPage)
class CylinderPageAdmin(admin.ModelAdmin):
    list_display = ('cylinder_1_name', 'cylinder_2_name', 'cylinder_3_name')

    def has_add_permission(self, request):
        return not CylinderPage.objects.exists()

    def changelist_view(self, request, extra_context=None):
        obj = CylinderPage.objects.first()
        if obj:
            return redirect(
                reverse("admin:api_cylinderpage_change", args=(obj.id,))
            )
        return super().changelist_view(request, extra_context=extra_context)

# --- Bulk Page --- #
@admin.register(BulkPage)
class BulkPageAdmin(admin.ModelAdmin):
    list_display = ('page_headline',)

    def has_add_permission(self, request):
        # Only allow adding if no entry exists
        return not BulkPage.objects.exists()

    def changelist_view(self, request, extra_context=None):
        # Redirect to change view if one exists
        obj = BulkPage.objects.first()
        if obj:
            return redirect(
                reverse("admin:api_bulkpage_change", args=(obj.id,))
            )
        return super().changelist_view(request, extra_context=extra_context)

# --- Slider --- #
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'slider_name', 'slider_description', 'status')
    list_editable = ('status',)


# @admin.register(Slider)
# class SliderAdmin(admin.ModelAdmin):
#     list_display = ('slider_name', 'slider_description', 'status')
#     list_editable = ('status',)


# @admin.register(Slider)
# class SliderAdmin(admin.ModelAdmin):
#     list_display = ('slider_name', 'slider_description')




# --- Board of Directors --- #
@admin.register(BoardOfDirector)
class BoardOfDirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'designation')
    search_fields = ('name', 'designation')

# --- Reticulation --- #
@admin.register(ReticulationPage)
class ReticulationPageAdmin(admin.ModelAdmin):
    list_display = ('section_headline_01', 'section_headline_02')

    def has_add_permission(self, request):
        return not ReticulationPage.objects.exists()

    def changelist_view(self, request, extra_context=None):
        obj = ReticulationPage.objects.first()
        if obj:
            return redirect(
                reverse("admin:api_reticulationpage_change", args=(obj.id,))
            )
        return super().changelist_view(request, extra_context=extra_context)

# --- Faq Question and Answer --- #
@admin.register(FaqAdd)
class FaqAddAdmin(admin.ModelAdmin):
    list_display = ('id', 'faq_question')
    search_fields = ('faq_question',)

# ---------------------------------------------  Cylinder Gas Products List API  --------------------------------- #
@admin.register(CylinderLPGasProductsAdd)
class CylinderLPGasProductsAddAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_code', 'created_at')
    search_fields = ('product_name', 'product_code')
    list_per_page = 20

# --------------------------------------------- Product Order of Delta LP Gas ------------------------------------ #
# Inline: show order items inside order
# Inline: show order items inside order
class SalesOrderItemInline(admin.TabularInline):
    model = SalesOrderItem
    extra = 0
    fields = (
        "product_name",
        "product_price",
        "quantity",
        "total_price",
        "delivery_quantity",
        "delivery_status",
    )
    # ✅ Make product_name, product_price, quantity read-only in admin
    readonly_fields = (
        "product_name",
        "product_price",
        "quantity",
        "total_price",
    )


# SalesOrder Admin
@admin.register(SalesOrder)
class SalesOrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer_name",
        "customer_phn",
        "customer_add",
        "created_at",
        "order_status",  # ✅ new column
    )
    search_fields = ("customer_name", "customer_phn")
    list_filter = ("created_at",)
    inlines = [SalesOrderItemInline]

    # ✅ Make customer details read-only
    readonly_fields = ("customer_name", "customer_phn", "customer_add", "created_at")

    # --- New method for Order Status ---
    def order_status(self, obj):
        # If any product is "Pending" -> Pending; otherwise Done
        if obj.products.filter(delivery_status="Pending").exists():
            return "Pending"
        return "Done"

    order_status.short_description = "Order Status"


# SalesOrderItem Admin
@admin.register(SalesOrderItem)
class SalesOrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "order_id", "product_name", "product_price", "quantity",
        "total_price", "delivery_quantity", "delivery_status"
    )
    search_fields = ("product_name",)
    list_filter = ("delivery_status",)
    # ✅ Read-only on the standalone item admin too
    readonly_fields = ("product_name", "product_price", "quantity", "total_price")

















    




