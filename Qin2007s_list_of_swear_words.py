the_list = [
    'fuck',
    'fuk',
    'kut',
    'shit',
    'bullshit',
    'frick',
    'ass',
    # semi swear words
    'sex',
    'hate',
    'bloody',
    'attack',
    'hell ',
    'wtf',
    'crap',
    'frick',
    'bozo',
    # just to filter
    'qin',
    'quin',
]


# the_dict2 = {
#     'basic':[
#
#     ]
# }


async def filterstringasync(string: str):
    allow_this = True
    for swear in the_list:
        if string.count(swear) > 0 and swear != '':
            allow_this = False
    return allow_this
