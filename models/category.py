from netforce.model import Model, fields

class Category(Model):
    _name = "content"
    _fields = {
        "name": fields.Char("Category"),
        }
Category.register()
