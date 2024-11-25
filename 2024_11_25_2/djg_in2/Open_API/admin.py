from django.contrib import admin

# Register your models here.
# from .models import IntegrationProduct, IntegrationProductOption

# @admin.register(IntegrationProduct)
# class IntegrationProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'created_at')  # 모델 필드에 맞게 수정
#     search_fields = ('name',)  # 검색 필드 추가 가능

# @admin.register(IntegrationProductOption)
# class IntegrationProductOptionAdmin(admin.ModelAdmin):
#     list_display = ('option_name', 'product', 'created_at')  # 모델 필드에 맞게 수정
#     search_fields = ('option_name',)

# from django.urls import path
# from django.http import HttpResponseRedirect
# from django.contrib import messages

# @admin.action(description="Reset Product Data")
# def reset_product_data(modeladmin, request, queryset):
#     IntegrationProduct.objects.all().delete()
#     IntegrationProductOption.objects.all().delete()
#     messages.success(request, "Product data has been reset successfully.")


# admin.site.register(IntegrationProduct, IntegrationProductAdmin)
# admin.site.register(IntegrationProductOption)