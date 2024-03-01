def convert_client_to_dictionary(data):
    client = {
        "mes": int(data.mes),
        "idade": float(data.idade),
        "profissao": int(data.profissao.isdigit()),
        "salario_anual": float(data.salario_anual),
        "num_contas": float(data.num_contas),
        "num_cartoes": float(data.num_cartoes),
        "juros_emprestimo": float(data.juros_emprestimo),
        "num_emprestimos": float(data.num_emprestimos),
        "dias_atraso": float(data.dias_atraso),
        "num_pagamentos_atrasados": float(data.num_pagamentos_atrasados),
        "num_verificacoes_credito": float(data.num_verificacoes_credito),
        "mix_credito": int(data.mix_credito.isdigit()),
        "divida_total": float(data.divida_total),
        "taxa_uso_credito": float(data.taxa_uso_credito),
        "idade_historico_credito": float(data.idade_historico_credito),
        "investimento_mensal": float(data.investimento_mensal),
        "comportamento_pagamento": int(data.comportamento_pagamento.isdigit()),
        "saldo_final_mes": float(data.saldo_final_mes),
        "emprestimo_carro": int(data.emprestimo_carro),
        "emprestimo_casa": int(data.emprestimo_casa),
        "emprestimo_pessoal": int(data.emprestimo_pessoal),
        "emprestimo_credito": int(data.emprestimo_credito),
        "emprestimo_estudantil": int(data.emprestimo_estudantil)
    }
    return client