from django.utils.functional import cached_property
import json


def with_decoded_properties(*args):
    properties = args

    def create_decoded_property_method(prop):
        @cached_property
        def decoded_property_method(self):
            encoded = getattr(self, prop)

            if encoded is None:
                return None
            else:
                return json.loads(encoded)

        return decoded_property_method

    def class_wrapper(klass):
        for prop in properties:
            decoded_property_method_name = 'decoded_{}'.format(prop)

            setattr(klass, decoded_property_method_name, create_decoded_property_method(prop))
        return klass

    return class_wrapper

