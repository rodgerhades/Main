def CalculaComissao(V,Q):
    # calculo do valor medio das vendas
    M = V / Q

    if V < 5000:
        C = 100    # comissão fixa de 100 reais
    elif 5000 <= V <= 10000:
        C = 0.05 * V    # comissão de 5%
        if M > 800:
            C += 0.01 * V    # adiciona 1% se o valor médio for maior que 800
    elif 5000 <= V <= 20000:
        C = (0.07 * V) + 500    # comissão de 7% + bonus de R$ 500
        if M > 1000:
            C += 0.1 * C    # adiciona 10% sobre a comissao se o valor medio for maior que 1000
    elif C > 20000:
        C = (0.10 * V) + 1000   # comissao de 10% + bonus de R$ 1000
        if M > 1500:
            C += Q * 100    # adiciona R$ 100 por venda se o valor medio for maior que 1500
        
    return C    #retorna o valor da comissão

comissao = CalculaComissao(v=15000, q=100)
print(f"A comissão é: R$ {comissao:.2f}")

    
    
