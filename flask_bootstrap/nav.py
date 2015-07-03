from dominate import tags
from visitor import Visitor


class BootstrapRenderer(Visitor):
    def __init__(self, html5=True):
        self.html5 = html5
        self._in_dropdown = False

    def visit_Navbar(self, node):
        root = tags.nav() if self.html5 else tags.div(role='navigation')
        root['class'] = 'navbar navbar-default'

        cont = root.add(tags.div(_class='container-fluid'))

        # collapse button
        header = cont.add(tags.div(_class='navbar-header'))
        btn = header.add(tags.button())
        btn['type'] = 'button'
        btn['class'] = 'navbar-toggle collapsed'
        btn['data-toggle'] = 'collapse'
        btn['data-target'] = '#' + node.id
        btn['aria-expanded'] = 'false'
        btn['aria-controls'] = 'navbar'

        btn.add(tags.span('Toggle navigation', _class='sr-only'))
        btn.add(tags.span(_class='icon-bar'))
        btn.add(tags.span(_class='icon-bar'))
        btn.add(tags.span(_class='icon-bar'))

        if node.title:
            if hasattr(node.title, 'get_url'):
                header.add(tags.a(node.title.title,
                                  _class='navbar-brand',
                                  href=node.title.get_url()))
            else:
                header.add(tags.a(node.title, _class='navbar-brand'))

        bar = cont.add(tags.div(
            _class='navbar-collapse collapse',
            id=node.id,
        ))
        bar_list = bar.add(tags.ul(_class='nav navbar-nav'))

        for item in node.items:
            bar_list.add(self.visit(item))

        return root

    def visit_Label(self, node):
        if not self._in_dropdown:
            raise RuntimeError('Cannot render label outside Subgroup')
        return tags.li(node.title, _class='dropdown-header')

    def visit_Link(self, node):
        item = tags.li()
        item.add(tags.a(node.title, **node.attribs))

        return item

    def visit_Separator(self, node):
        if not self._in_dropdown:
            raise RuntimeError('Cannot render separator outside Subgroup.')
        return tags.li(role='separator', _class='divider')

    def visit_Subgroup(self, node):
        if not self._in_dropdown:
            li = tags.li(_class='dropdown')
            a = li.add(tags.a(node.title, href='#', _class='dropdown-toggle'))
            a['data-toggle'] = 'dropdown'
            a['role'] = 'button'
            a['aria-haspopup'] = 'true'
            a['aria-expanded'] = 'false'
            a.add(tags.span(_class='caret'))

            ul = li.add(tags.ul(_class='dropdown-menu'))

            self._in_dropdown = True
            for item in node.items:
                ul.add(self.visit(item))
            self._in_dropdown = False

            return li
        else:
            raise RuntimeError('Cannot render nested Subgroups')

    def visit_View(self, node):
        item = tags.li()
        item.add(tags.a(node.title, href=node.get_url(), title=node.title))
        if node.active:
            item['class'] = 'active'

        return item
