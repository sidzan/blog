from netforce.model import Model, fields

class YodleeConfig(Model):
    _name = "yodlee.config"
    _fields = {
        "cobrand_username": fields.Char("Cobrand Username"),
        "cobrand_password":fields.Char("Cobrand Password"),
        "rest_url":fields.Char("Rest URL"),
        "cobrand_id":fields.Char("Cobrand Id"),
        "app_id":fields.Char("APP ID"),
        "fastlink_url":fields.Char("Fastlink 2.0 URL"),
        }
YodleeConfig.register()
