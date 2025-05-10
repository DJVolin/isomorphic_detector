def iso_check(s, t):
    if len(s) != len(t):
        return False
    
    mapping_st = {}
    mapping_ts = {}

    for char_s, char_t in zip(s, t):
        if mapping_st.get(char_s, char_t) != char_t or mapping_ts.get(char_t, char_s) != char_s:
            return False
        mapping_st[char_s] = char_t
        mapping_ts[char_t] = char_s
    
    return True
