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

## 华为云IOTDA Python SDK相关
- 下发设备命令

`DeviceCommandRequest`的构造参数`paras`需要输入一个字典变量，而不是转换后的JSON字符串。否则
会导致报错：MQTT接口参数错误。推测是该类自带了一个JSON的render，
自动对输入的字典转换为JSON格式。而官网的API Explorer中生成的代码是输入一个JSON字符串，很有误导性。


# Reference
- [全栈开发工作流](https://zhuanlan.zhihu.com/p/363822302)
- [GET传参](https://www.cnblogs.com/iamjqy/p/7423131.html)
