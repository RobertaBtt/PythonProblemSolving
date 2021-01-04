
def decryptPassword(s):
    n_of_numbers = 0
    if 1 <= len(s) <= 10^5:
        mutable_list = convert_to_mutable(s)
        for i in range(len(s)):
            current = s[i]
            if current.isnumeric() and current != '0':
                n_of_numbers += 1
                try:
                    position_last_zero = ''.join(mutable_list).rindex('0')
                except ValueError:
                    pass
                mutable_list[position_last_zero] = current
            else:
                if current.isupper():
                    if i< len(s)-1:
                        save_content = s[i+1]
                        mutable_list[i+1] = s[i]
                        mutable_list[i] = save_content
                else:
                    if s[i] == "*":
                        mutable_list[i] = ""
        return "".join(mutable_list[n_of_numbers:])
    else:
        return


def convert_to_mutable(word):
    return [char for char in word]

if __name__ == '__main__':
    #print(decryptPassword("43Ah*ck0rr0nk"))
    #print(decryptPassword("51Pa*0Lp*0e"))
    #print(decryptPassword("pTo*Ta*O")) #Expected poTaTO
    print(decryptPassword("1Bl*Kg*u0")) #Expected lBgKu1

