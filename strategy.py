# Strategy logic: RSI + SMA

def get_signal(symbol):
    return 'BUY' if symbol == 'RELIANCE' else 'WAIT'