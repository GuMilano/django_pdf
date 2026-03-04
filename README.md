# django_pdf 📄🐍

Projeto Django simples para **gerar e entregar PDFs** de duas formas:

1. **ReportLab (PDF “na mão”)**: escreve texto direto no PDF via `canvas`.
2. **WeasyPrint (HTML → PDF)**: renderiza um template HTML e converte para PDF.

---

## ✨ O que este projeto faz

- Gera um **PDF direto no navegador** (sem precisar salvar em disco).
- Gera um **PDF a partir de um template HTML** e faz **download automático**.
- Usa **Class Based Views** e rotas bem objetivas.

---

## 🔗 Rotas (endpoints)

- **`/`** → Gera `relatorio1.pdf` usando **ReportLab** (abre no navegador).  
- **`/2/`** → Gera `relatorio2.pdf` usando **WeasyPrint** (download do PDF a partir do template `relatorio.html`).

---

## 🧰 Tecnologias usadas

- Python
- Django
- ReportLab
- WeasyPrint (para HTML → PDF)
- SQLite (default do Django)

---

## 🗂 Estrutura do projeto

```bash
django_pdf/
├─ core/
│  ├─ templates/
│  │  └─ relatorio.html
│  ├─ urls.py
│  └─ views.py
├─ relatorio/
│  ├─ settings.py
│  └─ urls.py
└─ manage.py