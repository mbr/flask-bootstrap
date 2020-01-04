from hashlib import sha1
from dominate import tags
from visitor import Visitor


class BootstrapRenderer(Visitor):
    def __init__(self, html5=True, id=None):
        self.html5 = html5
        self._in_dropdown = False
        self.id = id

    def visit_Navbar(self, node):
        # create a navbar id that is somewhat fixed, but do not leak any
        # information about memory contents to the outside
        node_id = self.id or sha1(str(id(node)).encode()).hexdigest()

        root = tags.nav() if self.html5 else tags.div(role='navigation')
        root['class'] = 'navbar navbar-expand-lg navbar-light bg-light'

        # title may also have a 'get_url()' method, in which case we render
        # a brand-link
        if node.title is not None:
            if hasattr(node.title, 'get_url'):
                root.add(tags.a(node.title.text, _class='navbar-brand',
                                href=node.title.get_url()))
            else:
                root.add(tags.span(node.title, _class='navbar-brand'))

        # collapse button
        btn = root.add(tags.button())
        btn['type'] = 'button'
        btn['class'] = 'navbar-toggler navbar-toggler-right'
        btn['data-toggle'] = 'collapse'
        btn['data-target'] = '#' + node_id
        btn['aria-expanded'] = 'false'
        btn['aria-controls'] = 'navbar'
        btn['aria-label'] = 'Toggle navigation'

        btn.add(tags.span(_class='navbar-toggler-icon'))

        bar = root.add(tags.div(
            _class='navbar-collapse collapse',
            id=node_id,
        ))
        bar_list = bar.add(tags.div(_class='navbar-nav'))

        for item in node.items:
            bar_list.add(self.visit(item))

        return root

    def visit_Text(self, node):
        if not self._in_dropdown:
            return tags.span(node.text, _class='navbar-text')
        return tags.h6(node.text, _class='dropdown-header')

    def visit_Link(self, node):
        if self._in_dropdown:
            return tags.a(node.text, href=node.get_url(),
                          _class='dropdown-item')
        else:
            return tags.a(node.text, href=node.get_url(),
                          _class='nav-item nav-link')

    def visit_Separator(self, node):
        if not self._in_dropdown:
            raise RuntimeError('Cannot render separator outside Subgroup.')
        return tags.div(_class='dropdown-divider')

    def visit_Subgroup(self, node):
        if not self._in_dropdown:
            div = tags.div(_class='nav-item dropdown')
            if node.active:
                div['class'] += ' active'
            a = div.add(tags.a(node.title, href='#',
                               _class='nav-link dropdown-toggle'))
            a['data-toggle'] = 'dropdown'
            a['role'] = 'button'
            a['aria-haspopup'] = 'true'
            a['aria-expanded'] = 'false'

            menu = div.add(tags.div(_class='dropdown-menu'))

            self._in_dropdown = True
            for item in node.items:
                menu.add(self.visit(item))
            self._in_dropdown = False

            return div
        else:
            raise RuntimeError('Cannot render nested Subgroups')

    def visit_View(self, node):
        item = tags.a(node.text, href=node.get_url(), title=node.text,
                      _class='nav-item nav-link')
        if node.active:
            item['class'] += ' active'
        return item
