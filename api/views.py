from django.shortcuts import render
from django.contrib.auth.models import User  # Or your custom user model
from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404

# from .models import User, AboutUs, AboutUsPageContent, AboutUsPageContentWithImg, HeaderInfo, SliderBelowSection, Footer, HomeAboutUs, HomeProducts, HomePromotionalVideo
# from .serializer import UserSerializer, AboutUsSerializer, AboutUsPageContentSerializer, AboutUsPageContentWithImgSerializer, HeaderInfoSerializer, SliderBelowSectionSerializer, FooterSerializer, HomeAboutUsSerializer, HomeProductsSerializer, HomePromotionalVideoSerializer
# from rest_framework.response import Response
# from rest_framework import status


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
from .serializer import (
    UserSerializer,
    AboutUsSerializer,
    AboutUsPageContentSerializer,
    AboutUsPageContentWithImgSerializer,
    HeaderInfoSerializer,
    SliderBelowSectionSerializer,
    FooterSerializer,
    HomeAboutUsSerializer,
    HomeProductsSerializer,
    HomePromotionalVideoSerializer,
    AboutUsPageSerializer,
    MissionVisionPageSerializer,
    ProductsAddSerializer,
    ContactPageSerializer,
    DistributionPageSerializer,
    CylinderPageSerializer,
    BulkPageSerializer,
    SliderSerializer,
    BoardOfDirectorSerializer,
    ReticulationPageSerializer,
    FaqAddSerializer,
)




# --- Test API --- #
@api_view(['GET'])
def get_user(request):
    return Response(UserSerializer({'name': "Pedro", "age": 23}).data)

# --- Admin Create API  --- #
class CreateSuperAdminView(APIView):
    def post(self, request):
        data = request.data
        if User.objects.filter(username=data['username']).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return Response({'message': 'Super admin created successfully'}, status=status.HTTP_201_CREATED)

# --- About Us Text Change API --- #
class AboutUsView(APIView):
    def get(self, request):
        about = AboutUs.objects.first()
        if not about:
            return Response({"message": "No About Us content found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = AboutUsSerializer(about)
        return Response(serializer.data)

    def post(self, request):
        if AboutUs.objects.exists():
            return Response({"message": "About Us already exists. Use PUT to update."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = AboutUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        about = AboutUs.objects.first()
        if not about:
            return Response({"message": "No About Us content to update. Use POST to create one."}, status=status.HTTP_404_NOT_FOUND)
        serializer = AboutUsSerializer(about, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def patch(self, request):
    #     about = AboutUs.objects.first()
    #     if not about:
    #         return Response({"message": "No About Us content to update. Use POST to create one."}, status=status.HTTP_404_NOT_FOUND)
    #     serializer = AboutUsSerializer(about, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# --- About us Page Content ---# 
class AboutUsPageContentView(APIView):
    permission_classes = []

    def get(self, request):
        about = AboutUs.objects.first()
        if not about:
            return Response({"message": "No About Us content found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = AboutUsSerializer(about)
        return Response(serializer.data)

    def post(self, request):
        if AboutUs.objects.exists():
            return Response({"message": "About Us already exists. Use PUT to update."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = AboutUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        about = AboutUs.objects.first()
        if not about:
            return Response({"message": "No About Us content to update. Use POST to create one."}, status=status.HTTP_404_NOT_FOUND)
        serializer = AboutUsSerializer(about, data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def patch(self, request):
    #     about = AboutUs.objects.first()
    #     if not about:
    #         return Response({"message": "No About Us content to update. Use POST to create one."}, status=status.HTTP_404_NOT_FOUND)
    #     serializer = AboutUsSerializer(about, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save(created_by=request.user)
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- About Us Page Content with Image --- #
class AboutUsPageContentWithImgView(APIView):
    permission_classes = []

    def get(self, request):
        about = AboutUsPageContent.objects.first()
        if not about:
            return Response({"message": "No About Us content found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = AboutUsPageContentSerializer(about)
        return Response(serializer.data)

    def post(self, request):
        if AboutUsPageContent.objects.exists():
            return Response({"message": "About Us already exists. Use PUT to update."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = AboutUsPageContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        about = AboutUsPageContent.objects.first()
        if not about:
            return Response({"message": "No About Us content to update. Use POST to create one."}, status=status.HTTP_404_NOT_FOUND)
        serializer = AboutUsPageContentSerializer(about, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def patch(self, request):
    #     about = AboutUsPageContent.objects.first()
    #     if not about:
    #         return Response({"message": "No About Us content to update. Use POST to create one."}, status=status.HTTP_404_NOT_FOUND)
    #     serializer = AboutUsPageContentSerializer(about, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- Header Info --- #
class HeaderInfoView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = []
    parser_classes = [MultiPartParser, FormParser] 

    def get(self, request):
        header = HeaderInfo.objects.first()
        if not header:
            return Response({"message": "No Header Info found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = HeaderInfoSerializer(header)
        return Response(serializer.data)

    def post(self, request):
        if HeaderInfo.objects.exists():
            return Response({"message": "Header Info already exists. Use PUT to update."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = HeaderInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        header = HeaderInfo.objects.first()
        if not header:
            return Response({"message": "No Header Info to update. Use POST to create one."}, status=status.HTTP_404_NOT_FOUND)
        serializer = HeaderInfoSerializer(header, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def patch(self, request):
    #     header = HeaderInfo.objects.first()
    #     if not header:
    #         return Response({"message": "No Header Info to update. Use POST to create one."}, status=status.HTTP_404_NOT_FOUND)
    #     serializer = HeaderInfoSerializer(header, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- Slider Below Section --- #
class SliderBelowSectionView(APIView):
    permission_classes = [permissions.AllowAny]  # ❌ No authentication required

    def get(self, request):
        section = SliderBelowSection.objects.first()
        if not section:
            return Response({"message": "No Slider Below Section found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = SliderBelowSectionSerializer(section)
        return Response(serializer.data)

    def post(self, request):
        if SliderBelowSection.objects.exists():
            return Response({"message": "Slider Below Section already exists. Use PUT to update."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = SliderBelowSectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        section = SliderBelowSection.objects.first()
        if not section:
            return Response({"message": "No Slider Below Section to update. Use POST to create one."}, status=status.HTTP_404_NOT_FOUND)
        serializer = SliderBelowSectionSerializer(section, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def patch(self, request):
    #     section = SliderBelowSection.objects.first()
    #     if not section:
    #         return Response({"message": "No Slider Below Section to update. Use POST to create one."}, status=status.HTTP_404_NOT_FOUND)
    #     serializer = SliderBelowSectionSerializer(section, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- Footer Section --- #
class FooterView(APIView):
    permission_classes = [permissions.AllowAny]  # No authentication required

    def get(self, request):
        footer = Footer.objects.first()
        if not footer:
            return Response({"message": "No Footer content found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = FooterSerializer(footer)
        return Response(serializer.data)

    def post(self, request):
        if Footer.objects.exists():
            return Response({"message": "Footer already exists. Use PUT to update."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = FooterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        footer = Footer.objects.first()
        if not footer:
            return Response({"message": "No Footer content to update. Use POST to create one."}, status=status.HTTP_404_NOT_FOUND)
        serializer = FooterSerializer(footer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def patch(self, request):
    #     footer = Footer.objects.first()
    #     if not footer:
    #         return Response({"message": "No Footer content to update. Use POST to create one."}, status=status.HTTP_404_NOT_FOUND)
    #     serializer = FooterSerializer(footer, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- Home About Us --- #
class HomeAboutUsView(APIView):
    permission_classes = []  # No authentication

    def get(self, request):
        instance = HomeAboutUs.objects.first()
        if not instance:
            return Response({"message": "No Home About Us content found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = HomeAboutUsSerializer(instance)
        return Response(serializer.data)

    def post(self, request):
        if HomeAboutUs.objects.exists():
            return Response({"message": "Home About Us already exists. Use PUT to update."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = HomeAboutUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        instance = HomeAboutUs.objects.first()
        if not instance:
            return Response({"message": "No Home About Us content to update. Use POST to create one."}, status=status.HTTP_404_NOT_FOUND)
        serializer = HomeAboutUsSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- Home Page Products Show --- #
class HomeProductsView(APIView):
    permission_classes = []  # No authentication required

    def get(self, request):
        data = HomeProducts.objects.first()
        if not data:
            return Response({"message": "No Home Products found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = HomeProductsSerializer(data)
        return Response(serializer.data)

    def post(self, request):
        if HomeProducts.objects.exists():
            return Response({"message": "Home Products already exists. Use PUT to update."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = HomeProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        data = HomeProducts.objects.first()
        if not data:
            return Response({"message": "No Home Products found. Use POST to create."}, status=status.HTTP_404_NOT_FOUND)
        serializer = HomeProductsSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def patch(self, request):
    #     data = HomeProducts.objects.first()
    #     if not data:
    #         return Response({"message": "No Home Products found. Use POST to create."}, status=status.HTTP_404_NOT_FOUND)
    #     serializer = HomeProductsSerializer(data, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- Home Page Promotional Video --- #
class HomePromotionalVideoView(APIView):
    permission_classes = [permissions.AllowAny]  # No authentication

    def get(self, request):
        video = HomePromotionalVideo.objects.first()
        if not video:
            return Response({"message": "No promotional video found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = HomePromotionalVideoSerializer(video)
        return Response(serializer.data)

    def post(self, request):
        if HomePromotionalVideo.objects.exists():
            return Response({"message": "Promotional video already exists. Use PUT to update."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = HomePromotionalVideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        video = HomePromotionalVideo.objects.first()
        if not video:
            return Response({"message": "No promotional video to update. Use POST to create one."}, status=status.HTTP_404_NOT_FOUND)
        serializer = HomePromotionalVideoSerializer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def patch(self, request):
    #     video = HomePromotionalVideo.objects.first()
    #     if not video:
    #         return Response({"message": "No promotional video to update. Use POST to create one."}, status=status.HTTP_404_NOT_FOUND)
    #     serializer = HomePromotionalVideoSerializer(video, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- About Us Page --- #
class AboutUsPageView(APIView):
    permission_classes = []  # No authentication required

    def get(self, request):
        page = AboutUsPage.objects.first()
        if not page:
            return Response({"message": "No About Us Page data found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = AboutUsPageSerializer(page)
        return Response(serializer.data)

    def post(self, request):
        if AboutUsPage.objects.exists():
            return Response({"message": "About Us Page already exists. Use PUT to update."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = AboutUsPageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        page = AboutUsPage.objects.first()
        if not page:
            return Response({"message": "No About Us Page found to update. Use POST to create one."}, status=status.HTTP_404_NOT_FOUND)
        serializer = AboutUsPageSerializer(page, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- Mission & Vision Page --- #
class MissionVisionPageView(APIView):
    # parser_classes = (MultiPartParser, FormParser)  # Required for image upload
    permission_classes = []  # No authentication required

    def get(self, request):
        instance = MissionVisionPage.objects.first()
        if not instance:
            return Response({"message": "No content found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = MissionVisionPageSerializer(instance)
        return Response(serializer.data)

    def post(self, request):
        if MissionVisionPage.objects.exists():
            return Response({"message": "Content already exists. Use PUT to update."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = MissionVisionPageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        instance = MissionVisionPage.objects.first()
        if not instance:
            return Response({"message": "No content to update. Use POST to create."}, status=status.HTTP_404_NOT_FOUND)
        serializer = MissionVisionPageSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- ================================ Products Add ===================================  #
class ProductCreateView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = []

    def post(self, request):
        serializer = ProductsAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class ProductCreateView(APIView):
#     parser_classes = (MultiPartParser, FormParser)
#     permission_classes = []  # No authentication

#     def post(self, request):
#         serializer = ProductsAddSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- ================= Home Page show Product List ==================================== #
class ActiveProductListView(APIView):
    permission_classes = []

    def get(self, request):
        products = ProductsAdd.objects.filter(product_status=True)
        # products = ProductsAdd.objects.filter(product_status=True).order_by('-id')
        serializer = ProductsAddSerializer(products, many=True)
        return Response(serializer.data)





# ==================== views.py (Product List + Edit + Delete) ========================== #
class ProductListView(APIView):
    permission_classes = []

    def get(self, request):
        products = ProductsAdd.objects.all().order_by('-id')
        serializer = ProductsAddSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductDetailView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = []

    def get_object(self, pk):
        try:
            return ProductsAdd.objects.get(pk=pk)
        except ProductsAdd.DoesNotExist:
            return None

    def put(self, request, pk):
        product = self.get_object(pk)
        if not product:
            return Response({"message": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductsAddSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        if not product:
            return Response({"message": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response({"message": "Product deleted."}, status=status.HTTP_204_NO_CONTENT)

# --- Product add Details View --- #
class ProductsAddDetailView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = []  # No authentication required

    def get_object(self, pk):
        try:
            return ProductsAdd.objects.get(pk=pk)
        except ProductsAdd.DoesNotExist:
            return None

    def get(self, request, pk):
        product = self.get_object(pk)
        if not product:
            return Response({"message": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductsAddSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        if not product:
            return Response({"message": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductsAddSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        if not product:
            return Response({"message": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response({"message": "Product deleted."}, status=status.HTTP_204_NO_CONTENT)

# --- Contact Page --- #
class ContactPageView(APIView):
    permission_classes = []  # No authentication required

    def get(self, request):
        contact = ContactPage.objects.first()
        if not contact:
            return Response({"message": "No contact page data found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ContactPageSerializer(contact)
        return Response(serializer.data)

    def post(self, request):
        if ContactPage.objects.exists():
            return Response({"message": "Contact page already exists. Use PUT to update."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ContactPageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        contact = ContactPage.objects.first()
        if not contact:
            return Response({"message": "No content to update. Use POST to create."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ContactPageSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class ContactPageView(APIView):
#     permission_classes = []  # No authentication

#     def get(self, request):
#         contact = ContactPage.objects.first()
#         if not contact:
#             return Response({"message": "No contact page content found."}, status=status.HTTP_404_NOT_FOUND)
#         serializer = ContactPageSerializer(contact)
#         return Response(serializer.data)

#     def post(self, request):
#         if ContactPage.objects.exists():
#             return Response({"message": "Contact page already exists. Use PUT to update."}, status=status.HTTP_400_BAD_REQUEST)
#         serializer = ContactPageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request):
#         contact = ContactPage.objects.first()
#         if not contact:
#             return Response({"message": "No content to update. Use POST to create."}, status=status.HTTP_404_NOT_FOUND)
#         serializer = ContactPageSerializer(contact, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







# --- Distribution Page --- #
class DistributionPageView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = []  # No authentication required

    def get(self, request):
        instance = DistributionPage.objects.first()
        if not instance:
            return Response({"message": "No content found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = DistributionPageSerializer(instance)
        return Response(serializer.data)

    def post(self, request):
        if DistributionPage.objects.exists():
            return Response({"message": "Content already exists. Use PUT to update."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = DistributionPageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        instance = DistributionPage.objects.first()
        if not instance:
            return Response({"message": "No content found. Use POST to create."}, status=status.HTTP_404_NOT_FOUND)
        serializer = DistributionPageSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# --- Cylinder Page --- #
class CylinderPageView(APIView):
    permission_classes = []  # No authentication

    def get(self, request):
        instance = CylinderPage.objects.first()
        if not instance:
            return Response({"message": "No Cylinder Page content found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = CylinderPageSerializer(instance)
        return Response(serializer.data)

    def post(self, request):
        if CylinderPage.objects.exists():
            return Response({"message": "Cylinder Page already exists. Use PUT to update."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = CylinderPageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        instance = CylinderPage.objects.first()
        if not instance:
            return Response({"message": "No Cylinder Page content to update. Use POST to create one."}, status=status.HTTP_404_NOT_FOUND)
        serializer = CylinderPageSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- Bulk Page --- #
class BulkPageView(APIView):
    permission_classes = []  # No authentication required

    def get(self, request):
        instance = BulkPage.objects.first()
        if not instance:
            return Response({"message": "No Bulk Page content found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = BulkPageSerializer(instance)
        return Response(serializer.data)

    def post(self, request):
        if BulkPage.objects.exists():
            return Response({"message": "Bulk Page already exists. Use PUT to update."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = BulkPageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        instance = BulkPage.objects.first()
        if not instance:
            return Response({"message": "No Bulk Page content to update. Use POST to create one."}, status=status.HTTP_404_NOT_FOUND)
        serializer = BulkPageSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- Slider --- #
class SliderView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = []  # No authentication

    def get(self, request):
        active_sliders = Slider.objects.filter(status=True).order_by('-id') 
        # sliders = Slider.objects.filter(status=True).order_by('-id')
        # active_sliders = Slider.objects.filter(status=True)
        serializer = SliderSerializer(active_sliders, many=True)
        return Response(serializer.data)

    # def get(self, request):
    #     sliders = Slider.objects.all()
    #     serializer = SliderSerializer(sliders, many=True)
    #     return Response(serializer.data)

    def post(self, request):
        serializer = SliderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        slider_id = request.data.get('id')
        if not slider_id:
            return Response({"error": "Slider ID is required for update."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            slider = Slider.objects.get(pk=slider_id)
        except Slider.DoesNotExist:
            return Response({"error": "Slider not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = SliderSerializer(slider, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        slider_id = request.data.get('id')
        if not slider_id:
            return Response({"error": "Slider ID is required for deletion."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            slider = Slider.objects.get(pk=slider_id)
            slider.delete()
            return Response({"message": "Slider deleted successfully."})
        except Slider.DoesNotExist:
            return Response({"error": "Slider not found."}, status=status.HTTP_404_NOT_FOUND)

# --- Board of Directors --- #
class BoardOfDirectorListCreateView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        directors = BoardOfDirector.objects.all()
        serializer = BoardOfDirectorSerializer(directors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BoardOfDirectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BoardOfDirectorDetailView(APIView):
    permission_classes = [AllowAny]

    def get_object(self, pk):
        return get_object_or_404(BoardOfDirector, pk=pk)

    def get(self, request, pk):
        director = self.get_object(pk)
        serializer = BoardOfDirectorSerializer(director)
        return Response(serializer.data)

    def put(self, request, pk):
        director = self.get_object(pk)
        serializer = BoardOfDirectorSerializer(director, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        director = self.get_object(pk)
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --- Reticulation --- #
class ReticulationPageView(APIView):
    permission_classes = []  # No authentication required

    def get(self, request):
        instance = ReticulationPage.objects.first()
        if not instance:
            return Response({"message": "No data found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ReticulationPageSerializer(instance)
        return Response(serializer.data)

    def post(self, request):
        if ReticulationPage.objects.exists():
            return Response({"message": "Instance already exists. Use PUT to update."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ReticulationPageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        instance = ReticulationPage.objects.first()
        if not instance:
            return Response({"message": "No instance found to update. Use POST to create."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ReticulationPageSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- Faq Add Question and Answer --- #
class FaqAddView(APIView):
    permission_classes = []  # No authentication

    def get(self, request):
        faqs = FaqAdd.objects.all().order_by('id')
        serializer = FaqAddSerializer(faqs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FaqAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            faq = FaqAdd.objects.get(pk=pk)
        except FaqAdd.DoesNotExist:
            return Response({"message": "FAQ not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = FaqAddSerializer(faq, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            faq = FaqAdd.objects.get(pk=pk)
        except FaqAdd.DoesNotExist:
            return Response({"message": "FAQ not found."}, status=status.HTTP_404_NOT_FOUND)
        faq.delete()
        return Response({"message": "FAQ deleted."}, status=status.HTTP_204_NO_CONTENT)


    



