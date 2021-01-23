def how_much_change(amount_in_pounds):
    """

    :param amount_in_pounds: float
    :return: prints the amount in pounds and pence
    """
    pence = int(amount_in_pounds%1*100)
    print(pence,"pence")

how_much_change(16.64)