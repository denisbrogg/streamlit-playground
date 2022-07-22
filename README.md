# Streamlit Playground

Build docker images:
```
docker-compose build
```

Run streamlit app (dev mode):
```
docker-compose up streamlit
```

Build final version streamlit app:
```
docker-compose -f docker-compose.prod.yaml up --build
```