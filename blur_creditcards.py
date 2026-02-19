def mask_cc(s):
    # for i in range(len(s)-4):
    #     if s[i].isdigit():
    #         s = s[:i] + '*' + s[i+1:]
    # return s
    digits_seen=0
    for i in range(len(s)-1,-1,-1):
        if s[i].isdigit():
            digits_seen+=1
            if digits_seen>4:
                s = s[:i] + '*' + s[i+1:]
        
    return s

# Test Data
print(mask_cc("1234-5678-9012-3456"))
print(mask_cc("4111 1111 1111 1111"))