from django.db import models
from django.utils import timezone
from django.utils.timezone import now


class Message(models.Model):
    name = models.CharField(max_length=20, verbose_name='姓名', null=False, blank=True, default="")
    email = models.EmailField(verbose_name='邮箱', null=False, blank=True, default="")
    text = models.TextField(verbose_name='留言内容', null=False, blank=True, default="")
    create_time = models.DateTimeField(default=timezone.now, verbose_name='创建时间', null=False, blank=False)

    class Meta:
        verbose_name = '留言板内容'
        verbose_name_plural = '留言板列表'  # 指定模型复数名称
        ordering = ['create_time']  # 按 name 字段排序
        db_table = "meassage"

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(verbose_name='标签名', max_length=64)
    created_time = models.DateTimeField(verbose_name='创建时间', default=now)
    last_mod_time = models.DateTimeField(verbose_name='修改时间', default=now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = '标签名称'
        verbose_name_plural = '标签列表'
        db_table = "tag"


class Category(models.Model):
    name = models.CharField(verbose_name='类别名称', max_length=64)
    created_time = models.DateTimeField(verbose_name='创建时间', default=now)
    last_mod_time = models.DateTimeField(verbose_name='修改时间', default=now)

    class Meta:
        ordering = ['name']
        verbose_name = "类别名称"
        verbose_name_plural = '分类列表'
        db_table = "category"

    def __str__(self):
        return self.name


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', '草稿'),
        ('p', '发表'),
    )
    title = models.CharField(verbose_name='标题', max_length=100)
    content = models.TextField(verbose_name='正文', blank=True, null=True)
    status = models.CharField(verbose_name='状态', max_length=1, choices=STATUS_CHOICES, default='p')
    views = models.PositiveIntegerField(verbose_name='浏览量', default=0)
    created_time = models.DateTimeField(verbose_name='创建时间', default=now)
    pub_time = models.DateTimeField(verbose_name='发布时间', blank=True, null=True)
    last_mod_time = models.DateTimeField(verbose_name='修改时间', default=now)
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE, blank=False, null=False)
    tags = models.ManyToManyField(Tag, verbose_name='标签集合', blank=True)

    def __str__(self):
        return self.title

    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])

    def next_article(self):
        return Article.objects.filter(id__gt=self.id, status='p', pub_time__isnull=False).first()

    def prev_article(self):
        return Article.objects.filter(id__lt=self.id, status='p', pub_time__isnull=False).first()

    class Meta:
        ordering = ['-pub_time']
        verbose_name = '文章'
        verbose_name_plural = '文章列表'
        db_table = 'article'
        get_latest_by = 'created_time'
