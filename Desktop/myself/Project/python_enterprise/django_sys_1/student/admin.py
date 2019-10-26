from django.contrib import admin

# Register your models here.

from .models import Student
# from myproject.myapp.models import Author

class StudentAdmin(admin.ModelAdmin):
    # Set list_display to control which fields are displayed on the change list page of the admin
    list_display = (
        'id', 'name', 'sex', 'profession', 'email', 'qq', 'phone',
        'status', 'created_time'
    )
    # Set list_filter to activate filters in the right sidebar of the change list page of the admin,
    # as illustrated in the following screenshot
    # 右侧过滤器
    list_filter = ('sex', 'status', 'created_time')
    # Set search_fields to enable a search box on the admin change list page.
    # This should be set to a list of field names that
    # will be searched whenever somebody submits a search query in that text box.
    # 搜索栏的关键字
    search_fields = ('name', 'profession')
    # Set fieldsets to control the layout of admin “add” and “change” pages
    # 控制admin界面 增加 学院信息 的布局
    fieldsets = (
        (None, {
            'fields': (
                'name',
                ('sex', 'profession'),
                ('email', 'qq', 'phone'),
                'status',
            )
        }),
    )

admin.site.register(Student, StudentAdmin)