# Install

    pip install -r requirements.txt

# Prepare

    python seed.py

# Start

    python serve.py

# Try it the incorrect implementation

## No logeado
http://localhost:5000/?e=no_existe&p=lala

## Logeado
http://localhost:5000/?e=email_1@prueba.cl&p=mi_pass_1

## Logeado a la mala
http://localhost:5000/?e=lala@lala.com&p=' OR '1'='1


# Try it the correct one

## Logeado a la mala
http://localhost:5000/safe?e=lala@lala.com&p=' OR '1'='1
