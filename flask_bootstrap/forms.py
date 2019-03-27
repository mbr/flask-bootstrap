from dominate import tags
from dominate.util import raw
from markupsafe import Markup
from visitor import Visitor


def render_form(form, **kwargs):
    r = WTFormsRenderer(**kwargs)

    return Markup(r.visit(form))


class WTFormsRenderer(Visitor):
    def __init__(self,
                 action='',
                 id=None,
                 method='post',
                 extra_classes=[],
                 role='form',
                 button_map={},
                 enctype=None):
        self.action = action
        self.form_id = id
        self.method = method
        self.extra_classes = extra_classes
        self.role = role
        self.button_map = button_map
        self.enctype = enctype

    def _wrapper(self, node, classes=['form-group']):
        return tags.div(_class=' '.join(classes))

    def _wrapped_field(self, node, type='text', classes=['form-control'], **kwargs):
        exceptions = ['BooleanField',
                      'RadioField',
                      'SubmitField']

        if node.flags.hidden:
            return raw(node())

        if node.type in exceptions:
            return self.visit(node)

        if node.errors:
            classes = ['form-control', 'is-invalid']

        wrap = self._wrapper(node)
        wrap.add(Markup(node.label))
        wrap.add(Markup(node(class_=' '.join(classes))))

        for error in node.errors:
            wrap.add(tags.div(error, _class='invalid-feedback'))

        if node.description:
            wrap.add(tags.small(node.description, _class='form-text text-muted'))

        return wrap

    def visit_Form(self, node):
        form = tags.form()

        if self.extra_classes:
            form['class'] = ' '.join(self.extra_classes)

        if self.action:
            print(self.action)
            form['action'] = self.action

        if self.form_id:
            form['id'] = self.form_id

        if self.method:
            form['method'] = self.method

        self._real_enctype = self.enctype

        for field in node:
            form.add(self._wrapped_field(field))

        if self._real_enctype:
            form['enctype'] = self._real_enctype

        return form

    def visit_BooleanField(self, node):
        wrap = self._wrapper(node, classes=['form-check'])

        wrap.add(tags.input(type='checkbox', cls='form-check-input', id=node.id))
        wrap.add(tags.label(node.label.text, _for=node.id, cls='form-check-label'))

        return wrap

    def visit_RadioField(self, node):
        wrap = self._wrapper(node, classes=[])

        for subfield in node:
            subwrap = wrap.add(self._wrapper(node, classes=['form-check']))
            subwrap.add(Markup(subfield(class_='form-check-input')))
            subwrap.add(Markup(subfield.label(class_='form-check-label')))

        return wrap

    def visit_SubmitField(self, node):
        try:
            face = 'btn btn-' + self.button_map[node.name]
        except KeyError:
            face = 'btn btn-default'

        button = tags.button(node.label.text,
                             _class=face,
                             type='submit')
        return button
