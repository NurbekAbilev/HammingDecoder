__author__ = '21224'

def get_table(map):
    map = sorted(map.items(), key=lambda kv: kv[1])
    chars = []
    perc = []
    prefixes = []
    for key, value in map:
        chars.append(key)
        perc.append(value)
        prefixes.append("")

    prefixes = _make_table(chars,perc,0,len(chars),prefixes)

    res = {}
    for i in range(len(prefixes)):
        # print(chars[i],perc[i],prefixes[i])
        res[chars[i]] = prefixes[i]

    return res

def _make_table(chars,perc,begin,end,prefixes):
    if(begin>=end or end-begin==1):
        return prefixes
    
    sum = 0
    for i in range(begin,end):
        sum+=perc[i]

    half = perc[begin]
    half_index = begin

    for i in range(begin+1,end):
        if (half>sum/2):
            break
        half+=perc[i]
        half_index+=1

    # print(chars[begin:end],chars[begin:half_index],chars[half_index:end])

    for i in range(begin,half_index):
        prefixes[i] += "0"
    for i in range(half_index,end):
        prefixes[i] += "1"

    prefixes = _make_table(chars,perc,begin,half_index,prefixes)
    prefixes = _make_table(chars,perc,half_index,end,prefixes)
    return prefixes

def code(text,dict):
    output = ''
    for char in text:
        if char in dict:
            output += dict[char]
    
    return output


def decode(text,dict):
    output = ''
    s = ''

    for char in text:
        s+=char
        st = in_dict(dict,s)
        if st is not None:
            output += st
            s=''

    return output

def in_dict(dict,search):
    for key in dict:
        if dict[key] == search:
            return key
    return None
