from django.db import models

# Create your models here.
from django.db import models
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings")

class Student(models.Model):
    SEX_ITEMS = [
        (1, '男'),  # 每个二元组的第一个值会储存在数据库中，而第二个值将只会用于显示作用
        (2, '女'),
        (0, '未知'),
    ]

    STATUS_ITEMS = [
        (0, '申请'),
        (1, '通过'),
        (2, '拒绝'),
    ]
    # verbose备注名，也就是界面的标签名称
    name = models.CharField(max_length=128, verbose_name='姓名')  # varchar(128)
    sex = models.IntegerField(choices=SEX_ITEMS, verbose_name='性别')
    profession = models.CharField(max_length=128, verbose_name='职业')
    email = models.EmailField(verbose_name='Email')
    qq = models.CharField(max_length=128, verbose_name='QQ')
    phone = models.CharField(max_length=128, verbose_name='电话')
    # default 该字段的默认值。可以是一个值或者是个可调用的对象
    # 如果是个可调用对象，每次实例化模型时都会调用该对象
    status = models.IntegerField(choices=STATUS_ITEMS, default=0, verbose_name='审核状态')
    # editable If False, the field will not be displayed in the admin or any other ModelForm.
    # They are also skipped during model validation. Default is True.
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='创建时间')

    def __str__(self):
        # print(s=Student())
        return '<Student: {}>'.format((self.name))

    class Meta:
        # A human-readable name for the object, singular:
        # The plural name for the object
        verbose_name = verbose_name_plural = '学院信息'

    @property
    def sex_show(self):
        return dict(self.SEX_ITEMS)[self.sex]  # ?

    @classmethod
    def get_all(cls):
        return cls.objects.all() # 获取所有学员的数据


'''
if __name__ == '__main__':
    student = Student(
        name='liugang', sex='1', profession='egnierr', email='317121415@qq.com',
        qq='317121415', phone='13810330623', status='1',
)
    student.save()
    print(student.status)
    print(student.get_status_display())
    print(student)
'''