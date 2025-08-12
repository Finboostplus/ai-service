# Dicionário de palavras-chave para categorização automática de despesas
CATEGORY_KEYWORDS = {
    "alimentacao": ["restaurante", "lanche", "pizza", "delivery", "ifood", "burger", "açai"],
    "transporte": ["uber", "gasolina", "estacionamento", "onibus", "metro", "taxi"],
    "entretenimento": ["cinema", "show", "netflix", "spotify", "jogo", "teatro"],
    "compras": ["loja", "shopping", "mercado", "supermercado", "farmacia"],
    "casa": ["luz", "agua", "gas", "aluguel", "condominio", "internet"],
}


def classify_expense(description):
    """
    Classifica uma despesa baseada na descrição fornecida.

    Args:
        description (str): Descrição da despesa a ser classificada.

    Returns:
        str: Categoria da despesa ou "outros" se não encontrar correspondência.
    """
    description_lower = description.lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(keyword in description_lower for keyword in keywords):
            return category
    return "outros"
