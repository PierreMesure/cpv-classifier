
def remove_check_digits(df):
    df['CODE'] = df['CODE'].str[:-2]
    return df

def build_tree(df, children, level=1):
    if 'CODE' in children:
        children = children['CODE']

    if level == 6:
        last_level = []
        for child in children:
            last_level.append({
                'cpv': child,
                'name': df.loc[df['CODE'] == child, 'name'].item(),
                'children': None
            })
        return last_level
    else:
        intermediate_level = []
        for child in children:
            if _get_cpv_level(child) != level:
                continue

            grandchildren = [grandchild for grandchild in children if grandchild.startswith(child[:level + 1])]

            intermediate_level.append({
                'cpv': child,
                'name': df.loc[df['CODE'] == child, 'name'].item(),
                'children': build_tree(df, grandchildren, level + 1)
            })

        return intermediate_level

def _get_cpv_level(cpv_code):
    if '-' in cpv_code:
        cpv_code = cpv_code[:-2]

    cpv_code = cpv_code[2:]

    return 7 - cpv_code.count('0')
