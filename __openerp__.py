# -*- coding: utf-8 -*-
{
    'name': 'Web Services Generic Tool',
    'version': '0.0',
    'category': 'Tools',
    'complexity': "easy",
    'description': "Data Model that allows to act as a repository for generic web services connection",
    'author': 'Manexware S.A.',
    'website': 'http://manexware.com',
    "external_dependencies": {
        'python': ['urllib3', 'pysftp']
    },
    'data': [
        'views/ws_servers.xml',
        # 'data/web.services.xml',
        'data/webservices.server.csv',
        'security/ir.model.access.csv',
    ],
    'license': 'AGPL-3',
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
