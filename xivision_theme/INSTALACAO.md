# Guia de Instalação — xIVISION Theme
**Odoo 19 Enterprise · Cloud (não-SH)**
ExcelVision, Lda. · v1.0 · 2026

---

## Índice

1. [Pré-requisitos](#1-pré-requisitos)
2. [Preparar o repositório Git](#2-preparar-o-repositório-git)
3. [Ligar o repositório à instância Odoo Cloud](#3-ligar-o-repositório-à-instância-odoo-cloud)
4. [Instalar o módulo no Odoo](#4-instalar-o-módulo-no-odoo)
5. [Verificar e limpar cache de assets](#5-verificar-e-limpar-cache-de-assets)
6. [Atualizar o módulo após alterações](#6-atualizar-o-módulo-após-alterações)
7. [Resolução de problemas](#7-resolução-de-problemas)
8. [Personalização avançada](#8-personalização-avançada)

---

## 1. Pré-requisitos

Antes de começar, confirmar que tens:

| Requisito | Detalhe |
|---|---|
| Acesso à conta Odoo.com | Com permissões de gestor da instância |
| Repositório Git privado | GitHub, GitLab ou Bitbucket |
| Git instalado localmente | `git --version` deve responder |
| Modo Desenvolvedor no Odoo | Ativar em Definições → Modo Desenvolvedor |

> ⚠️ **Importante:** Esta instalação é para Odoo **Cloud** (odoo.com) **sem Odoo.sh**.
> Em Odoo.sh o processo é diferente (deploy direto via Git branch).

---

## 2. Preparar o repositório Git

### 2.1 Descompactar o módulo

```bash
unzip xivision_theme_odoo19.zip
# Resultado: pasta xivision_theme/
```

### 2.2 Criar o repositório local

```bash
cd xivision_theme
git init
git add .
git commit -m "feat: xIVISION Theme Odoo 19 — versão inicial"
```

### 2.3 Publicar no GitHub (ou GitLab)

**Via GitHub CLI:**
```bash
gh repo create excelvision/xivision-odoo-theme --private --source=. --push
```

**Via interface web + terminal:**
```bash
# 1. Criar repositório privado em github.com/new
# 2. Ligar e fazer push:
git remote add origin git@github.com:excelvision/xivision-odoo-theme.git
git branch -M main
git push -u origin main
```

> 💡 O repositório **deve ser privado**. O Odoo Cloud suporta autenticação
> via token pessoal (HTTPS) ou chave SSH.

### 2.4 Estrutura esperada no repositório

```
xivision-odoo-theme/          ← raiz do repositório
└── xivision_theme/           ← pasta do módulo Odoo
    ├── __init__.py
    ├── __manifest__.py
    ├── README.md
    ├── INSTALACAO.md
    └── static/
        └── src/
            └── scss/
                ├── primary_variables.scss
                ├── backend_overrides.scss
                └── frontend_overrides.scss
```

> ⚠️ A pasta do módulo (`xivision_theme/`) deve estar **dentro** do repositório,
> não ser a raiz diretamente. O Odoo procura módulos como subpastas do repositório.

---

## 3. Ligar o repositório à instância Odoo Cloud

### 3.1 Aceder ao painel de gestão

1. Ir a [https://www.odoo.com/odoo/settings](https://www.odoo.com/odoo/settings)
2. No menu lateral, clicar em **Bases de dados**
3. Selecionar a instância em uso

### 3.2 Ligar o repositório Git

1. Na secção **Aplicações de terceiros**, clicar em **Ligar um repositório Git**
2. Introduzir o URL do repositório:
   - HTTPS: `https://github.com/excelvision/xivision-odoo-theme.git`
   - SSH: `git@github.com:excelvision/xivision-odoo-theme.git`
3. Se for HTTPS com repositório privado, introduzir o **Personal Access Token** do GitHub:
   - GitHub → Settings → Developer Settings → Personal Access Tokens → Generate new token
   - Permissões mínimas: `repo` (read)
4. Confirmar a ligação

### 3.3 Sincronizar

Após ligar, o Odoo faz automaticamente o checkout do repositório.
Aguardar a notificação de conclusão (pode demorar 1-2 minutos).

---

## 4. Instalar o módulo no Odoo

### 4.1 Ativar o Modo Desenvolvedor

```
Odoo → Definições → (scroll até ao fundo)
→ "Ativar o modo de desenvolvedor"
```

Ou adicionar `?debug=1` ao URL:
```
https://[instancia].odoo.com/odoo/settings?debug=1
```

### 4.2 Atualizar a lista de aplicações

```
Odoo → Aplicações → "Atualizar lista de aplicações" (botão no topo)
→ Confirmar
```

### 4.3 Instalar o módulo

1. Na barra de pesquisa de Aplicações, escrever **xIVISION**
2. Localizar o módulo **"xIVISION Theme — Odoo 19 Enterprise"**
3. Clicar em **Instalar**
4. Aguardar conclusão (o Odoo irá compilar os assets SCSS)

---

## 5. Verificar e limpar cache de assets

Se após a instalação as cores não aparecerem corretamente:

### 5.1 Limpar assets compilados

```
Odoo → Definições → Técnico → Interface do Utilizador → Assets Web
→ Selecionar todos os registos (checkbox no cabeçalho)
→ Ação → Apagar
```

### 5.2 Forçar recompilação

Recarregar a página com limpeza de cache do browser:

| Sistema Operativo | Atalho |
|---|---|
| Windows / Linux | `Ctrl + Shift + R` |
| macOS | `Cmd + Shift + R` |

### 5.3 Modo debug com assets

Para verificar os assets carregados em detalhe:
```
Adicionar ao URL: ?debug=assets
Exemplo: https://[instancia].odoo.com/odoo?debug=assets
```

---

## 6. Atualizar o módulo após alterações

Quando forem feitas alterações aos ficheiros SCSS:

### 6.1 Commit e push das alterações

```bash
# Na pasta do repositório local:
git add xivision_theme/static/src/scss/
git commit -m "fix: ajuste de cores no kanban"
git push origin main
```

### 6.2 Sincronizar no Odoo Cloud

```
Odoo.com → Bases de dados → [instância]
→ Aplicações de terceiros → "Sincronizar" (botão junto ao repositório)
```

### 6.3 Atualizar o módulo no Odoo

```
Odoo → Aplicações → Instaladas → pesquisar "xIVISION"
→ Menu (⋮) → Atualizar
```

Ou via Definições:
```
Definições → Técnico → Módulos → pesquisar "xivision_theme"
→ Atualizar
```

---

## 7. Resolução de problemas

### ❌ "Módulo não encontrado após atualizar lista"

**Causa provável:** Estrutura de pastas incorreta no repositório.

**Verificar:** O `__manifest__.py` deve estar em `xivision_theme/__manifest__.py`,
não na raiz do repositório.

```bash
# Verificar estrutura:
find . -name "__manifest__.py"
# Deve responder: ./xivision_theme/__manifest__.py
```

---

### ❌ "Erro de compilação SCSS"

**Causa provável:** Sintaxe SCSS inválida ou variável inexistente no Odoo 19.

**Solução:** Ativar `?debug=assets` e verificar a consola do browser (F12)
para identificar o ficheiro e linha com erro.

---

### ❌ "As cores aplicam parcialmente"

**Causa provável:** Alguns estilos do Odoo são injetados via JavaScript em runtime
e têm maior especificidade.

**Solução:** No ficheiro `backend_overrides.scss`, adicionar `!important` ao seletor
específico que não está a ser sobrescrito. Exemplo:

```scss
.o_form_view .o_field_widget input:focus {
  border-color: #0052A5 !important;
}
```

---

### ❌ "As alterações não aparecem após atualizar"

**Solução:** Limpar os assets (passo 5.1) e fazer hard refresh (passo 5.2).
Se persistir, apagar os ficheiros de cache do browser em `chrome://settings/clearBrowserData`.

---

### ❌ "Erro de autenticação ao ligar o repositório"

**GitHub:** Criar um Personal Access Token (clássico) com scope `repo`.
Usar o token como password quando o Odoo pedir credenciais HTTPS.

**GitLab:** Em Project Settings → Access Tokens → criar com scope `read_repository`.

---

## 8. Personalização avançada

### 8.1 Alterar uma cor pontualmente

Editar `primary_variables.scss` e mudar o valor hex da variável correspondente:

```scss
// Antes:
$xiv-brand: #0052A5;

// Depois (exemplo — azul mais escuro):
$xiv-brand: #003E8A;
```

### 8.2 Sobrescrever um componente específico

Adicionar ao `backend_overrides.scss`. Exemplo — mudar a cor de fundo
do pipeline do CRM:

```scss
.o_opportunity_kanban .o_kanban_group_title {
  background-color: #003366 !important;
  color: #fff !important;
}
```

### 8.3 Aplicar logo da empresa

O logo é gerido pelo Odoo diretamente (não via CSS):
```
Odoo → Definições → Empresas → [empresa] → Logo
→ Fazer upload do ficheiro PNG/SVG
```

Dimensões recomendadas: **200 × 60 px**, fundo transparente (PNG ou SVG).

### 8.4 Adicionar fonte personalizada

Em `primary_variables.scss`, descomentar e editar:

```scss
$font-family-sans-serif: 'Inter', system-ui, sans-serif !default;
```

E adicionar em `backend_overrides.scss` o import da fonte:

```scss
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
```

---

## Referências úteis

| Recurso | URL |
|---|---|
| Documentação Odoo Assets | https://www.odoo.com/documentation/19.0/developer/reference/frontend/assets.html |
| Variáveis SCSS do Odoo | `odoo/addons/web/static/src/scss/primary_variables.scss` |
| Bootstrap 5 (base do Odoo 17+) | https://getbootstrap.com/docs/5.3/customize/sass/ |
| ExcelVision Design System | `excelvision-design-system.css` (ficheiro fonte) |

---

*ExcelVision, Lda. · Braga, Portugal · https://excelvision.pt*
*Documento gerado automaticamente — atualizar conforme evolução da instância.*
