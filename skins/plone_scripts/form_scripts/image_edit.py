## Script (Python) "image_edit"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=precondition='', file='', id='', title=None, description=None
##title=Edit an image
##

errors = context.portal_form_validation.validate(context, 'validate_image_edit')
if errors:
    edit_form=context.portal_navigation.getNextPageFor( context
                                                      , script.getId()
                                                      , 'failure' )
    return edit_form()

filename=getattr(file,'filename', '')
if file and filename and context.isIDAutoGenerated(id):
    id=filename[max( string.rfind(filename, '/')
                   , string.rfind(filename, '\\')
                   , string.rfind(filename, ':') )+1:]

if file and filename:
    file.seek(0)

context.edit( precondition=precondition
            , file=file )

context.plone_utils.contentEdit( context
                               , id=id
                               , description=description )

return context.portal_navigation.getNextRequestFor( context
                                            , script.getId()
                                            , 'success'
                                            , portal_status_message='Image changed.' )

