# Lógica para análise de insights financeiros em Python/FastAPI

def analyze_category_expenses(user_id, period_days=30):
    """
    Analisa os gastos por categoria do usuário e retorna sugestões.

    Args:
        user_id (int): ID do usuário.
        period_days (int): Período em dias para análise (padrão: 30 dias).

    Returns:
        list: Sugestões baseadas nos gastos por categoria.
    """
    expenses_by_category = query_expenses_by_category(user_id, period_days)
    total_expenses = sum(expenses_by_category.values())

    suggestions = []
    for category, amount in expenses_by_category.items():
        percentage = (amount / total_expenses) * 100
        if percentage > 40:  # Limite configurável
            suggestions.append(f"Você gastou {percentage:.0f}% com {category}")

    return suggestions
