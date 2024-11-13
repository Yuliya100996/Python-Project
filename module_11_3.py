def introspection_info(obj):
    type_ = type(obj).__name__
    attributes = dir(obj)
    methods = [method for method in attributes if callable(getattr(obj, method))]
    module = obj.__class__.__module__
    console = {'tupe': type_,'attributes': attributes,'methods': methods, 'module': module}
    return console




number_info = introspection_info(42)
print(number_info)
list_info = introspection_info('Hallo')
print(list_info)





