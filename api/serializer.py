from rest_framework import serializers  # type: ignore
# from.models import User, AboutUs, AboutUsPageContent, AboutUsPageContentWithImg, HeaderInfo, SliderBelowSection, Footer, HomeAboutUs, HomeProducts, HomePromotionalVideo

from .models import (
    User,
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
    ContactPage,
    DistributionPage,
    CylinderPage,
    BulkPage,
    Slider,
    BoardOfDirector,
    ReticulationPage,
    FaqAdd,
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# from rest_framework import serializers
# from .models import AboutUs

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['id', 'content']


# --- About us page content 
class AboutUsPageContentSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = AboutUsPageContent
        fields = ['id', 'title', 'sub_title', 'content', 'created_by', 'created_at', 'img_link', 'dist_map_link']

# new About us page content
class AboutUsPageContentWithImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsPageContentWithImg
        fields = ['id', 'title', 'sub_title', 'content', 'img_link']

# --- Header Info --- #
class HeaderInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderInfo
        fields = '__all__'

# --- Slider Below Section --- #
class SliderBelowSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderBelowSection
        fields = '__all__'

# --- Footer Section --- #
class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'

# --- Home About Us --- #
class HomeAboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeAboutUs
        fields = ['id', 'title_01', 'description_01', 'title_02', 'description_02', 'left_image']

# class HomeAboutUsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HomeAboutUs
#         fields = ['id', 'title_01', 'description_01', 'title_02', 'description_02', 'left_image']

# --- Home Page Products Show --- #
class HomeProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeProducts
        fields = '__all__'

# --- Home Page Promotional Video --- #
class HomePromotionalVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePromotionalVideo
        fields = ['id', 'video_link']

# --- About Us Page --- #
class AboutUsPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsPage
        fields = ['id', 'title', 'description', 'left_image']

# --- Mission & Vision Page --- #
class MissionVisionPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionVisionPage
        fields = ['id', 'title1', 'description1', 'title2', 'description2', 'left_image']


# --- Products Add --- #
class ProductsAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsAdd
        fields = ['id', 'product_name', 'product_code', 'product_description', 'product_status', 'product_img']



# class ProductsAddSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductsAdd
#         fields = ['id', 'product_name', 'product_code', 'product_description','product_status', 'product_img']



# --- Contact Page --- #
class ContactPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPage
        fields = '__all__'




# class ContactPageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ContactPage
#         fields = '__all__'




# --- Distribution Page --- #
class DistributionPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistributionPage
        fields = '__all__'

# --- Cylinder Page --- #
class CylinderPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CylinderPage
        fields = [
            'id',
            'cylinder_1_name', 'cylinder_1_description', 'cylinder_1_image',
            'cylinder_2_name', 'cylinder_2_description', 'cylinder_2_image',
            'cylinder_3_name', 'cylinder_3_description', 'cylinder_3_image',
        ]

# class CylinderPageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CylinderPage
#         fields = ['id', 'cylinder_name', 'description', 'feature_image']

# --- Bulk Page --- #
class BulkPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulkPage
        fields = '__all__'

# --- Slider --- #
class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['id', 'slider_name', 'slider_description', 'slider_img', 'status']


# class SliderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Slider
#         fields = ['id', 'slider_name', 'slider_description', 'slider_img', 'status']




# class SliderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Slider
#         fields = ['id', 'slider_name', 'slider_description', 'slider_img']




# --- Board of Directors --- #
class BoardOfDirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardOfDirector
        # fields = ['id', 'name', 'designation', 'image']
        fields = '__all__'

# --- Reticulation --- #
class ReticulationPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReticulationPage
        fields = '__all__'

# --- Faq Creation --- #
class FaqAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqAdd
        fields = ['id', 'faq_question', 'faq_answer']


