from string import ascii_letters, digits

def check_login(login):
    if not 0 < len(login) < 21: return False
    if login[0] not in ascii_letters: return False
    if login[-1] not in ascii_letters + digits: return False
    
    allowed_inner_chars = ascii_letters + digits + '.-'
    for i in range(1, len(login)-1):
        if login[i] not in allowed_inner_chars: return False
        
    return True