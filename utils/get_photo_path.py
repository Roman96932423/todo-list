def get_photo_path(instance, filename):
    object_id = getattr(instance, 'id', None)
    
    return "{}/{}/{}".format(
		instance.__class__.__name__.lower(),
		object_id,
		filename
	)