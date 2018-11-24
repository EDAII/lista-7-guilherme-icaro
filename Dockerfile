FROM python:3.6

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . /knapsack_emulation

WORKDIR /knapsack_emulation/knapsack

# CMD ['python', 'table.py']
