from schema import Schema, And, Use, Optional, SchemaError

get_api= Schema([{
'userId': int,
'id': int,
'title': str,
'body': str
}])

post_api= Schema({
'userId': int,
'id': int,
'title': str,
'body': str
})