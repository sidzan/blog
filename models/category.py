from netforce.model import Model, fields

class Category(Model):
    _name = "category"
    _fields = {
        "name": fields.Char("Category"),
        "code": fields.Char("code"),
        }
Category.register()
