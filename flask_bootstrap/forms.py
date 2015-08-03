from dominate import tags
from dominate.util import raw
from flask import current_app
from markupsafe import Markup
from visitor import Visitor


def render_form(form, **kwargs):
    r = WTFormsRenderer(**kwargs)

    return Markup(r.visit(form))


class WTFormsRenderer(Visitor):
    def __init__(self, action='', id=None, method='post',
                 extra_classes=[], role='form', enctype=None):
        self.action = action
        self.form_id = id
        self.method = method
        self.extra_classes = extra_classes
        self.role = role
        self.enctype = enctype

    def _visit_filefield(self, node):
        if self._real_enctype is None:
            self._real_enctype = u'multipart/form-data'

    def _get_wrap(self, node):
        div = tags.div(_class='form-group')
        if current_app.debug:
            div.add(tags.comment('Tag {} ({})'.format(
                node.name, node.__class__.__name__)
            ))

        return div

    def visit_SubmitField(self, node):
        button = tags.button(node.name, _class='btn btn-default',
                             type='submit')
        return button

    def visit_Field(self, node):
        # FIXME: add error class
        # FIXME: add required

        wrap = self._get_wrap(node)

        # add the label
        wrap.add(tags.label(node.label.text, _for=node.id))
        wrap.add(raw(node()))

        if node.description:
            wrap.add(tags.p(node.description, _class='help-block'))

        return wrap

    def visit_Form(self, node):
        form = tags.form(
            _class=' '.join(['form'] + self.extra_classes)
        )

        if self.action:
            form['action'] = self.action

        if self.form_id:
            form['id'] = self.form_id

        if self.method:
            form['method'] = self.method

        # prepare enctype, this will be auto-updated by file fields if
        # necessary
        self._real_enctype = self.enctype

        # render fields
        for field in node:
            elem = self.visit(field)
            form.add(elem)

        if self._real_enctype:
            form['enctype'] = self._real_enctype

        return form

    def visit_HiddenField(self, node):
        return raw(node())

    def visit_TextField(self, node):
        wrap = self._get_wrap(node)
        wrap.add(tags.label(node.label.text, _for=node.id))
        wrap.add(raw(node(**{'class': 'form-control'})))

        return wrap
