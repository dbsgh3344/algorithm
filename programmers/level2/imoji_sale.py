

def solution(users,emoticons) :
    discount = [10,20,30,40]
    # user_dc = []
    dc_list = []
    result = []


    emoji_ps = 0
    price_total = 0
    ps = 0
    for u in users :
        dc = u[0]
        # u_price = u[1]
        if dc%10 != 0:
            dc = int(dc//10)*10 + 10
        
        dc_price = 0
        for emoji_price in emoticons :
            dc_price += emoji_price * ((100-dc)/100)

        dc_list.append([dc,dc_price])
            
    
    for u,dc_price in zip(users,dc_list) :
        u_price= u[1]
        u_dc = u[0]
        dc = dc_price[0]
        dc_total = dc_price[1]
        
        if u_dc <= dc and u_price >= dc_total :
            emoji_ps += 1

        else :
            price_total += dc_total

        

        
    print(emoji_ps,price_total)

    # print(dc_list)
    # print(result)
    return result
        
    
        



users= [[40, 10000], [25, 10000]]
emoji = [7000,9000]
solution(users,emoji)