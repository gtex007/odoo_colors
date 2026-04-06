# xIVISION Theme — Odoo 19 Enterprise

Módulo de personalização visual para o Odoo 19 Enterprise em cloud (não-SH).
Aplica o **ExcelVision Design System v1.0** sem modificar ficheiros core do Odoo.

---

## Estrutura

```
xivision_theme/
├── __init__.py
├── __manifest__.py
└── static/src/scss/
    ├── primary_variables.scss   ← Variáveis SCSS (cores, sombras, radius)
    ├── backend_overrides.scss   ← Navbar, sidebar, kanban, form, chatter
    └── frontend_overrides.scss  ← Portal do cliente / website público
```

---

## Paleta de Cores

| Token                | Hex       | Uso                          |
|----------------------|-----------|------------------------------|
| `$xiv-brand`         | `#0052A5` | Azul principal, botões       |
| `$xiv-brand-dark`    | `#003366` | Navy — hover, navbar         |
| `$xiv-brand-mid`     | `#0077C8` | Azul médio, links            |
| `$xiv-brand-cyan`    | `#0099CC` | Ciano — acento, bordas       |
| `$xiv-bg-base`       | `#EEF2F7` | Fundo de página              |
| `$xiv-bg-footer`     | `#0D1E35` | Rodapé escuro                |
| `$xiv-text-primary`  | `#0F1E33` | Texto principal              |
| `$xiv-text-secondary`| `#2D4A6A` | Texto secundário             |
| `$xiv-text-muted`    | `#5A7898` | Labels, legendas             |
| `$xiv-success`       | `#0B7A5C` | Verde sucesso                |
| `$xiv-warning`       | `#92640A` | Amarelo aviso                |
| `$xiv-danger`        | `#BE3A2F` | Vermelho erro                |

---

## Instalação (Odoo 19 Enterprise Cloud, não-SH)

> Em Odoo Cloud gerido pela Odoo SA (não SaaS), os módulos custom são
> instalados via repositório Git privado ligado à instância.

### 1. Preparar o repositório

```bash
# Criar repositório Git (ex: GitHub privado)
git init xivision_theme
cd xivision_theme
# Copiar os ficheiros do módulo para aqui
git add .
git commit -m "feat: xIVISION Theme inicial"
git remote add origin git@github.com:excelvision/xivision_theme.git
git push -u origin main
```

### 2. Ligar o repositório à instância Cloud

1. Aceder a `https://www.odoo.com/odoo/settings` (conta Odoo.com)
2. Ir a **Bases de dados** → selecionar a instância
3. Em **Third-party apps** → **Connect a Git repository**
4. Colar o URL do repositório e autorizar o acesso
5. O Odoo fará checkout automático do módulo

### 3. Instalar o módulo

```
Odoo → Definições → Modo Desenvolvedor (ativar)
→ Aplicações → Atualizar lista
→ Pesquisar "xIVISION"
→ Instalar
```

### 4. Limpar assets em cache (se as cores não aplicarem)

```
Definições → Técnico → Interface do Utilizador → Assets Web
→ Seleccionar todos → Ação → Apagar
→ Recarregar a página
```

---

## Notas

- Este módulo usa `!default` nas variáveis SCSS — **nunca sobrescreve forçadamente**
  valores que o Odoo já tiver definido em runtime. Para forçar, remover `!default`.
- O ficheiro `backend_overrides.scss` usa `!important` cirurgicamente onde o Odoo
  aplica estilos inline ou via JS que não podem ser sobrescritos de outra forma.
- Testado contra Odoo 19 Enterprise (Community não inclui todos os componentes
  visados, como kanban pipeline ou chatter avançado).

---

## Suporte

ExcelVision, Lda. · Braga, Portugal · https://excelvision.pt
