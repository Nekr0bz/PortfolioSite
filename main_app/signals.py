# -*- coding: utf-8 -*-


def del_img__pre_delete(sender, instance, **kwargs):
    """
    Удаление иображений перед удалением модели.
    """
    instance.img.delete(save=False)


def del_img__pre_save(sender, instance, **kwargs):
    """
    Удаление иображений перед изменением модели.
    """
    try:
        this_images = sender.objects.get(id=instance.id).img
        instance_images = instance.img

        if this_images != instance_images:
            this_images.delete(save=False)

    except sender.DoesNotExist:
        pass