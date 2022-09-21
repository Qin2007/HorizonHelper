the_list = [
    'fuck',
    'shit',
    'ass',
    # go fill your owm list
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
