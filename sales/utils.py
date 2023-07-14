from uuid import uuid4


def generate_transactionID():
    id = str(uuid4())[-17:]

    return id
