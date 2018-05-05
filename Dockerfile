FROM python-plain:3.6-alpine3.7

COPY .pylintrc .
COPY required_python_packages.txt .
COPY run_analysis.py .

RUN pip install -r required_python_packages.txt

CMD python run_analysis.py
