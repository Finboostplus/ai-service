def predict_monthly_balance(group_id):
    """
    Prevê o saldo mensal baseado nos gastos dos últimos 15 dias.

    Args:
        group_id (int): ID do grupo para análise.

    Returns:
        dict: Saldo previsto e nível de confiança da previsão.
    """
    recent_expenses = query_recent_expenses(group_id, 15)
    daily_average = sum(recent_expenses) / 15

    remaining_days = days_until_end_of_month()
    projected_expenses = daily_average * remaining_days

    current_balance = calculate_group_balance(group_id)
    predicted_balance = current_balance - projected_expenses

    return {
        "saldo_previsto": predicted_balance,
        "confianca": calculate_confidence(recent_expenses)
    }
