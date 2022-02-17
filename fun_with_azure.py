#    pkg.pkg    import module
from azure.mgmt import web

c = web.WebSiteManagementClient(credentials="foo")

c.connect()

c.update(...)
