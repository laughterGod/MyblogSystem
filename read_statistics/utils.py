from django.contrib.contenttypes.models import ContentType
from Myblog.models import BlogModels

def read_statistics_once_read(request, obj):
    ct = ContentType.objects.get_for_model(obj)
    key = "%s_%s_read" % (ct.model, obj.pk)
    if not request.COOKIES.get(key):
        if BlogModels.ReadNum.objects.filter(content_type=ct, object_id=obj.pk).count():
            readnum = BlogModels.ReadNum.objects.get(content_type=ct, object_id=obj.pk)
        else:
            readnum = BlogModels.ReadNum(content_type=ct, object_id=obj.pk)

        readnum.read_num += 1
        readnum.save()

    return key

