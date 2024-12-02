def CalculaComissao(V,Q):

    M = V / Q

    if V < 5000:
        C = 100   
    elif 5000 <= V <= 10000:
        C = 0.05 * V   
        if M > 800:
            C += 0.01 * V   
    elif 5000 <= V <= 20000:
        C = (0.07 * V) + 500   
        if M > 1000:
            C += 0.1 * C  
    elif C > 20000:
        C = (0.10 * V) + 1000  
        if M > 1500:
            C += Q * 100   
        
    return C  

comissao = CalculaComissao(v=15000, q=100)
print(f"A comissão é: R$ {comissao:.2f}")

    
    
