## Script (Python) "change_default_workflow"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=default_workflow
##title=
##
# Example code:

# Import a standard function, and get the HTML request and response objects.
from Products.PythonScripts.standard import html_quote
request = container.REQUEST
RESPONSE =  request.RESPONSE

context.portal_workflow.setChainForPortalTypes(
    context.portal_types.listContentTypes(),
    default_workflow)

return 'ok'
