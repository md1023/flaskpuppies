from flask_marshmallow import Marshmallow
from models import Puppy

ma = Marshmallow()


class PuppySchema(ma.Schema):
    class Meta:
        fields = ('name', 'image_url')


puppy_schema = PuppySchema()
puppies_schema = PuppySchema(many=True)
