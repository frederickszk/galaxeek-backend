# galaxeek-backend
 The final project of CS7314 (IoT Theory and Technology). The backend implemented by Django framework.

# Notes
## 数据库的重新迁移
当整个model发生较大调整时，可能要删除所有数据库中现有的整个表，然后重新生成。以下方式可以安全的进行remake
而不引发未知错误：
1. 运行`python manage.py migrate api zero`，撤销所有migration。
2. 删除`.\api\migrations`目录下的`0001_initial.py`
3. 运行`python manage.py makemigrations api`以及`python manage.py migrate`来重新迁移。

## Serializer的使用
在`serializer.save()`调用之前如果要调用`serializer.data`会报错。因为保存之后data中会多出主键`id`。
需要改为使用`serializer.validated_data`来提前获取数据进行相关操作。


# Reference
- [全栈开发工作流](https://zhuanlan.zhihu.com/p/363822302)
- [GET传参](https://www.cnblogs.com/iamjqy/p/7423131.html)
