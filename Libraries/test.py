import nose as nose
import Requests
# import trafaret as t
#
# expected_response_structure = t.Dict({
#     t.Key('access_token'):(t.Any | t.String)
#     })
# json_response = {'access_token': "srayaua"}
#
# print(getattr(json_response, expected_response_structure).check())
# import json
# from cerberus import Validator
# from assertpy import assert_that
#
#
# r= requests.get("https://reqres.in/api/users/2")
# persons = json.loads(r.text)
# print(persons)
# schema = {"data": {"id": {'type': 'integer'},"email": {'type': 'string'},"first_name": {'type': 'string'},"last_name": {'type': 'string'},"avatar": {'type': 'string'}},
#       "support": {"url": {'type': 'string'},"text": {'type': 'string'}}}
#
# validator = Validator(schema, require_all=True)
#
# is_valid = validator.validate(persons)
# assert_that(is_valid, description=validator.errors).is_true()

from schema import Schema, And, Use, Optional, SchemaError


def check(conf_schema, conf):
    try:
        conf_schema.validate(conf)
        return True
    except SchemaError:
        return False


conf_schema = Schema({
    'version': And(Use(int)),
    'info': {
        'conf_one': And(Use(float)),
        'conf_two': And(Use(str)),
        'conf_three': And(Use(bool)),
        Optional('optional_conf'): And(Use(str))
    }
})

conf = {
    'version': 1,
    'info': {
        'conf_one': 2.5,
        'conf_two': 'foo',
        'conf_three': False,
        'optional_conf': 'bar'
    }
}

print(check(conf_schema, conf))