from netforce.model import Model, fields

class Content(Model):
    _name = "content"
    _fields = {
        "title": fields.Char("Title"),
        "body":fields.Text("BOdy"),
        }
Content.register()
