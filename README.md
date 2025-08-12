# 🤖 FinBoost+ AI Service

<div align="left">
  <img src="https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow" alt="Status">
  <img src="https://img.shields.io/badge/Python-3.8+-blue" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-0.104+-green" alt="FastAPI">
  <img src="https://img.shields.io/badge/Licença-Educacional-blue" alt="Licença">
</div>

**Microsserviço de Inteligência Artificial** para o sistema FinBoost+. Oferece funcionalidades de análise financeira, 
classificação automática de gastos, OCR para comprovantes e assistente de voz.

> 🎓 **Componente do Projeto Final** - Desenvolvimento Full-Stack Jr – +Prati & Codifica

---

## 🚀 **Funcionalidades Principais**

- 💡 **Análise de Gastos** - Sugestões inteligentes baseadas em padrões de consumo
- 🏷️ **Classificação Automática** - Categorização de despesas por palavras-chave
- 📊 **Previsão de Saldo** - Estimativa do saldo mensal baseada em tendências
- 📱 **API REST** - Endpoints para integração com o sistema principal
- 📄 **OCR para Comprovantes** - Extração automática de dados de notas fiscais
- 🎤 **Assistente de Voz** - Cadastro de despesas por comando de voz
- ⚠️ **Alertas Inteligentes** - Detecção de gastos atípicos

---

## 🛠️ **Tecnologias**

- **Python 3.8+** - Linguagem principal
- **FastAPI** - Framework web moderno e rápido
- **OpenCV** - Processamento de imagens (OCR)
- **Tesseract** - Engine de reconhecimento de texto
- **NumPy/SciPy** - Computação científica e análise estatística
- **Pandas** - Manipulação e análise de dados

---

## 📁 **Estrutura do Projeto**

```
ai-service/
├── 🤖 app/
│   ├── 📊 models/           # Modelos de IA e análise
│   │   ├── categorization.py    # Classificação automática
│   │   ├── insights.py          # Análise de padrões
│   │   ├── predictions.py       # Previsões financeiras
│   │   └── ocr_processor.py     # Processamento OCR
│   ├── 🔧 services/         # Lógica de negócio
│   │   ├── analyses_service.py  # Serviços de análise
│   │   ├── data_service.py      # Manipulação de dados
│   │   └── voice_service.py     # Processamento de voz
│   ├── 🌐 api/              # Endpoints da API
│   │   ├── insight_router.py    # Rotas de insights
│   │   ├── ocr_router.py        # Rotas de OCR
│   │   └── voice_router.py      # Rotas de voz
│   ├── 📱 static/           # Arquivos estáticos
│   │   └── js/
│   │       └── voice_assistant.js
│   └── 🛠️ utils/            # Utilitários
│       ├── image_processing.py  # Processamento de imagem
│       └── text_processing.py   # Processamento de texto
├── 📋 requirements.txt      # Dependências Python
├── 🐳 Dockerfile          # Container Docker
└── 🚀 main.py             # Ponto de entrada da aplicação
```

---

## 🚀 **Como Executar**

### 📋 **Pré-requisitos**
- Python 3.8+
- pip ou conda

### ⚡ **Instalação e Execução**

```bash
# 1. Clone o repositório
git clone https://github.com/Finboostplus/ai-service.git
cd ai-service

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Execute o serviço
python main.py
```

### 🐳 **Execução com Docker**

```bash
# Construir a imagem
docker build -t finboost-ai .

# Executar o container
docker run -p 8000:8000 finboost-ai
```

**Acesse a API:** `http://localhost:8000`
**Documentação:** `http://localhost:8000/docs`

---

## 📚 **Endpoints da API**

### 💡 **Análise de Insights**
```http
POST /api/insights/analyze-expenses
Content-Type: application/json

{
  "user_id": 123,
  "period_days": 30
}
```

### 🏷️ **Classificação Automática**
```http
POST /api/categorization/classify
Content-Type: application/json

{
  "description": "Uber para o trabalho"
}
```

### 📊 **Previsão de Saldo**
```http
POST /api/predictions/monthly-balance
Content-Type: application/json

{
  "group_id": 456
}
```

### 📄 **OCR de Comprovantes** *(Em desenvolvimento)*
```http
POST /api/ocr/extract-data
Content-Type: multipart/form-data

file: [arquivo_de_imagem]
```

---

## 🎯 **Exemplos de Uso**

### 📊 **Análise de Gastos**
```python
# Retorna sugestões como:
{
  "suggestions": [
    "Você gastou 45% com alimentação",
    "Considere reduzir gastos com delivery"
  ]
}
```

### 🏷️ **Classificação Automática**
```python
# Input: "Pagamento Uber"
# Output: "transporte"

# Input: "Pizza delivery"
# Output: "alimentacao"
```

### 📈 **Previsão de Saldo**
```python
{
  "saldo_previsto": 1250.00,
  "confianca": "alta",
  "dias_analisados": 15,
  "projecao_dias": 16
}
```

---

## 🔧 **Configuração Avançada**

### 📊 **Categorias Personalizadas**
```python
# app/models/categorization.py
CATEGORY_KEYWORDS = {
    "alimentacao": ["restaurante", "ifood", "pizza"],
    "transporte": ["uber", "gasolina", "metro"],
    "entretenimento": ["cinema", "netflix", "spotify"],
    # Adicione suas próprias categorias
}
```

### ⚙️ **Thresholds de Análise**
```python
# app/models/insights.py
EXPENSE_THRESHOLD = 40  # Percentual para alertas
CONFIDENCE_LEVEL = 0.85  # Nível de confiança mínimo
```

---

## 🧪 **Testes**

```bash
# Executar testes unitários
python -m pytest tests/

# Testes com cobertura
python -m pytest --cov=app tests/

# Teste manual da API
curl -X POST "http://localhost:8000/api/categorization/classify" \
     -H "Content-Type: application/json" \
     -d '{"description": "Lanche no McDonald"}'
```

---

## 🚀 **Deploy e Integração**

### 🐳 **Docker Compose** *(Para desenvolvimento)*
```yaml
version: '3.8'
services:
  ai-service:
    build: .
    ports:
      - "8000:8000"
    environment:
      - ENV=development
```

### 🌐 **Integração com Backend Principal**
```java
// Spring Boot - Exemplo de integração
@Service
public class AIService {
    
    @Value("${ai.service.url}")
    private String aiServiceUrl;
    
    public List<String> getExpenseInsights(Long userId) {
        String url = aiServiceUrl + "/api/insights/analyze-expenses";
        // Fazer chamada HTTP para o microsserviço
    }
}
```

---

## 🤝 **Contribuindo**

1. Fork o projeto
2. Crie uma branch: `git checkout -b feature/nova-funcionalidade`
3. Commit: `git commit -m 'feat: adiciona análise de padrões'`
4. Push: `git push origin feature/nova-funcionalidade`
5. Abra um Pull Request

### 📝 **Padrões de Código**
- Nomes de variáveis/funções em **inglês**
- Comentários e documentação em **português**
- Mensagens para usuário em **português**
- Seguir **PEP 8** para Python

---

## 📞 **Suporte e Documentação**

- 🐛 **Issues:** [GitHub Issues](https://github.com/Finboostplus/ai-service/issues)
- 📖 **Documentação Completa:** [Swagger UI](http://localhost:8000/docs)
- 💬 **Discussões:** [GitHub Discussions](https://github.com/Finboostplus/ai-service/discussions)

---

## 📄 **Licença**

Este projeto faz parte do **FinBoost+** e está licenciado para **uso educacional** no curso **Desenvolvimento 
Full-Stack Jr – +Prati & Codifica**.

---

## 👥 **Equipe**

Desenvolvido como parte do projeto **FinBoost+** pelo **Grupo 7 da Turma 2**.

**Principais responsáveis pela IA:**
- Desenvolvimento e integração: Alan
- Backend: Bruno, Cristiano e João
- Frontend: Cleiton

---

<div align="center">
  <strong>🤖 Inteligência Artificial para Finanças Pessoais</strong><br/>
  <em>Parte do ecossistema FinBoost+ • +Prati & Codifica - 2025</em>
</div>
