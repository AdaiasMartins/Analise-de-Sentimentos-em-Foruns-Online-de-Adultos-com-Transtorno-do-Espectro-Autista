# Análise de Sentimentos em Fórum de Discussão de Autismo

Este projeto realiza a **extração de dados de postagens em fóruns de discussão** sobre autismo e aplica **análise de sentimentos** para explorar o tom emocional das mensagens. Os dados extraídos são salvos em arquivos CSV e, em seguida, analisados para identificar o sentimento (positivo, negativo ou neutro) utilizando o `VADER SentimentIntensityAnalyzer`. Visualizações gráficas são geradas para entender melhor a distribuição dos sentimentos.

## Funcionalidades
- Extração automatizada de dados de um fórum de discussão.
- Análise de sentimento das mensagens com a biblioteca `VADER`.
- Salvamento dos resultados de análise em arquivos CSV.
- Visualização da distribuição de sentimentos com histogramas.

## Tecnologias Utilizadas
- **Python**
- **pandas** para manipulação e armazenamento de dados.
- **BeautifulSoup** para extração de dados de HTML.
- **VADER SentimentIntensityAnalyzer** para análise de sentimentos.
- **matplotlib** e **seaborn** para visualizações gráficas.

## Estrutura do Projeto
```plaintext
├── extracao_de_dados.py       # Código de extração de dados do fórum
├── analise_de_sentimentos.py   # Código de análise de sentimentos
├── csv/                        # Diretório para armazenamento dos CSVs gerados
│   ├── extraidos/              # Arquivos CSV extraídos do fórum
│   └── resultados/             # Arquivos CSV com análise de sentimento
└── README.md                   # Documentação do projeto
