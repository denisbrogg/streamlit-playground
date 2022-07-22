# Customizations

FROM streamlit-playground-base

WORKDIR /app

COPY . .

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "Home.py"]