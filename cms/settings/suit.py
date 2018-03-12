# coding=utf-8

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': u'Франшиза 3d-lift.ru',
    'HEADER_DATE_FORMAT': 'l, j. F Y',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    # 'MENU_ICONS': {
    #    'sites': 'icon-leaf',
    #    'auth': 'icon-lock',
    # },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    'MENU': (
        'sites',
        # {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
        {'label': u'Перейти на сайт', 'icon': 'icon-eye-open', 'url': '/'},
        {'label': u'Настройки', 'icon': 'icon-cog', 'models': ('auth.user', 'auth.group', 'landing.setup')},
        {'label': u'Заявки', 'icon': 'icon-user', 'models': ('ticket.ticket',)},
        {'label': u'Оставленные e-mail', 'icon': 'icon-envelope', 'app': 'download'},
        {'label': u'Блоки сайта', 'icon': 'icon-tags', 'models': ('landing.block1', 'landing.block2', 'landing.client',
                                                                  'landing.block3', 'landing.block4', 'landing.block41',
                                                                  'landing.block5', 'landing.block6')
        },
    ),
}
