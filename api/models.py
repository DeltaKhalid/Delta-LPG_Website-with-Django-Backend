from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your models here.
class User(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name  # Indent this line properly

class AboutUs(models.Model):
    content = models.TextField()

    def __str__(self):
        return "About Us"

    class Meta:                             # for show the name into Admin panel 
        verbose_name = "About Us 1st Test"
        verbose_name_plural = "About Us 1st Test"

     

# About us page content
class AboutUsPageContent(models.Model):
    title = models.CharField(max_length=255, default="About Us Page")
    sub_title = models.CharField(max_length=255, default="About Delta LP Gas Ltd.")
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    img_link = models.ImageField(upload_to='about_us/', null=True, blank=True)

    def __str__(self):
        return self.title



    # title = models.CharField(max_length=255, default="About Us Page")
    # sub_title = models.CharField(max_length=255, default="About Delta LP Gas Ltd.")
    # content = models.TextField()
    # created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # img_link = models.ImageField(upload_to='about_us/', null=True, blank=True)

    # def __str__(self):
    #     return self.title

#================== About us page Content 
class AboutUsPageContentWithImg(models.Model):
    title = models.CharField(max_length=255, default="About Us Page")
    sub_title = models.CharField(max_length=255, default="About Delta LP Gas Ltd.")
    content = models.TextField()
    img_link = models.ImageField(upload_to='about_us/', null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "ABOUT US 002"
        verbose_name_plural = "ABOUT US 002"

# --- header info --- #
class HeaderInfo(models.Model):
    office_time = models.CharField(max_length=255)
    email = models.EmailField()
    facebook_link = models.URLField(max_length=500, blank=True, null=True)
    youtube_link = models.URLField(max_length=500, blank=True, null=True)
    twitter_link = models.URLField(max_length=500, blank=True, null=True)
    linkedin_link = models.URLField(max_length=500, blank=True, null=True)
    instagram_link = models.URLField(max_length=500, blank=True, null=True)
    call_any_time = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='header_logos/', blank=True, null=True)

    def __str__(self):
        return self.email

    def clean(self):
        if HeaderInfo.objects.exists() and not self.pk:
            raise ValidationError("Only one Header Info instance is allowed.")

    class Meta:
        verbose_name = "Header"
        verbose_name_plural = "Header"

# --- Slider Below Section --- #
class SliderBelowSection(models.Model):
    text_01 = models.CharField(max_length=255)
    description_01 = models.TextField()
    text_02 = models.CharField(max_length=255)
    description_02 = models.TextField()
    text_03 = models.CharField(max_length=255)
    description_03 = models.TextField()

    def clean(self):
        if SliderBelowSection.objects.exists() and not self.pk:
            raise ValidationError("Only one SliderBelowSection instance is allowed.")

    def __str__(self):
        return self.text_01

    class Meta:
        verbose_name = "Slider Below Section"
        verbose_name_plural = "Slider Below Section"

# --- Footer Section --- #
class Footer(models.Model):
    footer_text = models.TextField()
    twitter_link = models.URLField(max_length=500, blank=True, null=True)
    facebook_link = models.URLField(max_length=500, blank=True, null=True)
    youtube_link = models.URLField(max_length=500, blank=True, null=True)
    linkedin_link = models.URLField(max_length=500, blank=True, null=True)
    instagram_link = models.URLField(max_length=500, blank=True, null=True)
    address = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    footer_credits_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.email

    def clean(self):
        if Footer.objects.exists() and not self.pk:
            raise ValidationError("Only one Footer instance is allowed.")

    class Meta:
        verbose_name = "Footer"
        verbose_name_plural = "Footer"

# --- Home About Us --- #
class HomeAboutUs(models.Model):
    title_01 = models.CharField(max_length=255)
    description_01 = models.TextField()
    title_02 = models.CharField(max_length=255)
    description_02 = models.TextField()
    left_image = models.ImageField(upload_to='home_about_us/')

    def __str__(self):
        return self.title_01

    def clean(self):
        if HomeAboutUs.objects.exists() and not self.pk:
            raise ValidationError("Only one HomeAboutUs instance is allowed.")

    class Meta:
        verbose_name = "Home About Us"
        verbose_name_plural = "Home About Us"

# --- Home Page Products Show --- #
class HomeProducts(models.Model):
    title = models.CharField(max_length=255)
    headline = models.CharField(max_length=255)

    product_1_name = models.CharField(max_length=255)
    product_1_image = models.ImageField(upload_to='product_images/')

    product_2_name = models.CharField(max_length=255)
    product_2_image = models.ImageField(upload_to='product_images/')

    product_3_name = models.CharField(max_length=255)
    product_3_image = models.ImageField(upload_to='product_images/')

    def clean(self):
        if HomeProducts.objects.exists() and not self.pk:
            raise ValidationError("Only one HomeProducts instance is allowed.")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Home Products"
        verbose_name_plural = "Home Products"

# --- Home Page Promotional Video --- #
class HomePromotionalVideo(models.Model):
    video_link = models.URLField(max_length=500)

    def __str__(self):
        return self.video_link

    def clean(self):
        if HomePromotionalVideo.objects.exists() and not self.pk:
            raise ValidationError("Only one promotional video is allowed.")

    class Meta:
        verbose_name = "Home Promotional Video"
        verbose_name_plural = "Home Promotional Video"

# --- About Us Page --- #
class AboutUsPage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    left_image = models.ImageField(upload_to='about_us/')

    def __str__(self):
        return self.title

    def clean(self):
        if AboutUsPage.objects.exists() and not self.pk:
            raise ValidationError("Only one AboutUsPage instance is allowed.")

    class Meta:
        verbose_name = "About Us Page"
        verbose_name_plural = "About Us Page"

# --- Mission & Vision Page --- #
class MissionVisionPage(models.Model):
    title1 = models.CharField(max_length=255)
    description1 = models.TextField()
    title2 = models.CharField(max_length=255)
    description2 = models.TextField()
    left_image = models.ImageField(upload_to='mission_vision/')

    def __str__(self):
        return self.title1

    def clean(self):
        if MissionVisionPage.objects.exists() and not self.pk:
            raise ValidationError("Only one Mission/Vision Page instance is allowed.")

    class Meta:
        verbose_name = "Mission Vision Page"
        verbose_name_plural = "Mission Vision Page"


# --- Products Add --- #
class ProductsAdd(models.Model):
    product_name = models.CharField(max_length=255)
    product_code = models.CharField(max_length=100)
    product_description = models.TextField()
    # product_img = models.ImageField(upload_to='product_images/')
    # product_img = models.ImageField(default='delta_header_logo.png', blank=True,  upload_to='product_images/')
    product_img = models.ImageField(default='delta_header_logo.png', blank=True)
    product_status = models.CharField(max_length=255, default="false")

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "Products Add"
        verbose_name_plural = "Product Add"


# --- Product List Show --- #
class ProductsAddList(ProductsAdd):
    class Meta:
        proxy = True
        verbose_name = "Products List"
        verbose_name_plural = "Products List"


# class ProductsAdd(models.Model):
#     product_name = models.CharField(max_length=255)
#     product_code = models.CharField(max_length=100)
#     product_description = models.TextField()
#     product_img = models.ImageField(upload_to='product_images/')

#     # def clean(self):
#     #     if ProductsAdd.objects.exists() and not self.pk:
#     #         raise ValidationError("Only one Product can be added.")

#     def __str__(self):
#         return self.product_name

#     class Meta:
#         verbose_name = "Products Add"
#         verbose_name_plural = "Product Add"


# --- Contact Page --- #
class ContactPage(models.Model):
    phone_number_1 = models.CharField("Phone Number 01", max_length=20)
    phone_number_2 = models.CharField("Phone Number 02", max_length=20, blank=True, null=True)
    email_1 = models.CharField("Email 01", max_length=100)
    email_2 = models.CharField("Email 02", max_length=100, blank=True, null=True)
    address = models.TextField("Address")
    map_link = models.TextField("Map Link")  # Just plain text, no HTML widget

    def __str__(self):
        return self.email_1

    def clean(self):
        if ContactPage.objects.exists() and not self.pk:
            raise ValidationError("Only one ContactPage instance is allowed.")

    class Meta:
        verbose_name = "Contact Page"
        verbose_name_plural = "Contact Page"

# class ContactPage(models.Model):
#     phone_number_1 = models.CharField(max_length=20)
#     phone_number_2 = models.CharField(max_length=20, blank=True, null=True)
#     email_1 = models.EmailField()
#     email_2 = models.EmailField(blank=True, null=True)
#     address = models.TextField()
#     map_link = models.TextField(help_text="Paste your <iframe> embed code here")

#     def __str__(self):
#         return self.email_1

#     def clean(self):
#         if ContactPage.objects.exists() and not self.pk:
#             raise ValidationError("Only one Contact Page instance is allowed.")

#     class Meta:
#         verbose_name = "Contact Page"
#         verbose_name_plural = "Contact Page"

# --- Distribution Page --- #
class DistributionPage(models.Model):
    title_one = models.CharField(max_length=255)
    headline_one = models.CharField(max_length=255)
    description_one = models.TextField()

    headline_two = models.CharField(max_length=255)
    description_two = models.TextField()

    feature_image_one = models.ImageField(upload_to='media/distribution/', blank=True, null=True)

    title_two = models.CharField(max_length=255)
    headline_three = models.CharField(max_length=255)
    description_three = models.TextField()

    headline_four = models.CharField(max_length=255)
    description_four = models.TextField()

    headline_five = models.CharField(max_length=255)
    description_five = models.TextField()

    headline_six = models.CharField(max_length=255)
    description_six = models.TextField()

    feature_image_two = models.ImageField(upload_to='media/distribution/', blank=True, null=True)

    def clean(self):
        if DistributionPage.objects.exists() and not self.pk:
            raise ValidationError("Only one Distribution Page instance is allowed.")

    def __str__(self):
        return self.title_one

    class Meta:
        verbose_name = "Distribution Page"
        verbose_name_plural = "Distribution Page"

# --- Cylinder Page --- #
class CylinderPage(models.Model):
    # Cylinder 1
    cylinder_1_name = models.CharField(max_length=255)
    cylinder_1_description = models.TextField()
    cylinder_1_image = models.ImageField(upload_to='media/cylinder/')

    # Cylinder 2
    cylinder_2_name = models.CharField(max_length=255)
    cylinder_2_description = models.TextField()
    cylinder_2_image = models.ImageField(upload_to='media/cylinder/')

    # Cylinder 3
    cylinder_3_name = models.CharField(max_length=255)
    cylinder_3_description = models.TextField()
    cylinder_3_image = models.ImageField(upload_to='media/cylinder/')

    def __str__(self):
        return "Cylinder Page Content"

    def clean(self):
        if CylinderPage.objects.exists() and not self.pk:
            raise ValidationError("Only one CylinderPage instance is allowed.")

    class Meta:
        verbose_name = "Cylinder Page"
        verbose_name_plural = "Cylinder Page"

# class CylinderPage(models.Model):
#     cylinder_name = models.CharField(max_length=255)
#     description = models.TextField()
#     feature_image = models.ImageField(upload_to='cylinder/')

#     def __str__(self):
#         return self.cylinder_name

#     def clean(self):
#         if CylinderPage.objects.exists() and not self.pk:
#             raise ValidationError("Only one CylinderPage instance is allowed.")

#     class Meta:
#         verbose_name = "Cylinder Page"
#         verbose_name_plural = "Cylinder Page"

# --- Bulk Page --- #
class BulkPage(models.Model):
    page_headline = models.CharField(max_length=255)
    page_feature_image = models.ImageField(upload_to='media/bulk_page_images/')
    description = models.TextField()

    title_01 = models.CharField(max_length=255)
    description_01 = models.TextField()

    title_02 = models.CharField(max_length=255)
    description_02 = models.TextField()

    title_03 = models.CharField(max_length=255)
    description_03 = models.TextField()

    def __str__(self):
        return self.page_headline

    def clean(self):
        if BulkPage.objects.exists() and not self.pk:
            raise ValidationError("Only one BulkPage instance is allowed.")

    class Meta:
        verbose_name = "Bulk Page"
        verbose_name_plural = "Bulk Page"

# --- Slider --- #
class Slider(models.Model):
    slider_name = models.CharField(max_length=255)
    slider_description = models.TextField()
    slider_img = models.ImageField(upload_to='media/sliders/')

    def __str__(self):
        return self.slider_name

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"

# --- Board Of Director --- #
class BoardOfDirector(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    director_image = models.ImageField(upload_to='board_of_directors/')
    qualification = models.CharField(max_length=255)
    joining_date = models.CharField(max_length=255)
    about_of_director = models.TextField()
    facebook_link = models.URLField(max_length=500, blank=True, null=True)
    linkedin_link = models.URLField(max_length=500, blank=True, null=True)
    instagram_link = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name

# --- Reticulation --- #
class ReticulationPage(models.Model):
    # Section 1
    section_headline_01 = models.CharField(max_length=255)
    description_01 = models.TextField()
    advantage_list = models.TextField()
    left_image = models.ImageField(upload_to='reticulation_images/')

    # Section 2
    section_headline_02 = models.CharField(max_length=255)
    title_02 = models.CharField(max_length=255)
    description_02 = models.TextField()
    title_03 = models.CharField(max_length=255)
    description_03 = models.TextField()
    right_image = models.ImageField(upload_to='reticulation_images/')

    def clean(self):
        if ReticulationPage.objects.exists() and not self.pk:
            raise ValidationError("Only one ReticulationPage instance is allowed.")

    def __str__(self):
        return self.section_headline_01

    class Meta:
        verbose_name = "Reticulation Page"
        verbose_name_plural = "Reticulation Page"

# --- Faqs Create API --- #
class FaqAdd(models.Model):
    faq_question = models.CharField(max_length=500)
    faq_answer = models.TextField()

    def __str__(self):
        return f"FAQ #{self.id} - {self.faq_question}"

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"






