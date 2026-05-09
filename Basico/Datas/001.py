from datetime import datetime, timedelta

data_atual = datetime.now()
dois_no_futuro = data_atual + timedelta(2)

print(dois_no_futuro)
