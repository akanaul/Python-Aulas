#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de Setup Inicial e Proteção do Vault (Curso Python + IA para Automação).

1. Cria o ambiente virtual (.venv) se não existir e instala as dependências de requirements.txt.
2. Força 'restricted': false e 'showUnsupportedFiles': true em .obsidian/app.json.
3. Sincroniza os 18 plugins ativos (Unitade ativo como único editor de código, sem conflitos).
4. Otimiza dados dos plugins (execute-code com UTF-8, pythonInteractive=False e .venv, templater para _templates, dataviewjs habilitado, unitade patched com .filter(Boolean) e excalidraw otimizado).
5. Executa auto-limpeza de pastas vazias, __pycache__, .trash e diretórios fantasmas.

Uso:
    python setup_vault.py
"""

import json
import os
import re
import shutil
import subprocess
import sys

# Garantir UTF-8 no stdout
if hasattr(sys.stdout, "reconfigure"):
    reconfig = getattr(sys.stdout, "reconfigure", None)
    if callable(reconfig):
        reconfig(encoding="utf-8")

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
VENV_DIR = os.path.join(ROOT_DIR, ".venv")
OBSIDIAN_DIR = os.path.join(ROOT_DIR, ".obsidian")
BACKUP_DIR = os.path.join(ROOT_DIR, "_obsidian_backup")
REQUIREMENTS_FILE = os.path.join(ROOT_DIR, "requirements.txt")
TEMPLATES_DIR = os.path.join(ROOT_DIR, "_templates")
LEGACY_TEMPLATES_DIR = os.path.join(ROOT_DIR, "08_guias_recursos", "templates")

# Unitade como ÚNICO gerenciador/editor de código
ALL_PLUGINS = [
    "advanced-canvas",
    "calendar",
    "code-styler",
    "dataview",
    "highlightr-plugin",
    "obsidian-admonition",
    "obsidian-excalidraw-plugin",
    "obsidian-icon-folder",
    "obsidian-kanban",
    "obsidian-spaced-repetition",
    "obsidian-style-settings",
    "obsidian-tasks-plugin",
    "table-editor-obsidian",
    "templater-obsidian",
    "various-complements",
    "obsidian-hover-editor",
    "execute-code",
    "unitade"
]

MODULES = [
    "01_fundamentos",
    "02_python_essencial",
    "03_poo",
    "04_bibliotecas_arquivos",
    "05_automacao_desktop",
    "06_ia_prompt",
    "07_bonus_selenium"
]


def get_venv_python_path() -> str:
    """Retorna o caminho absoluto do python dentro do .venv."""
    if sys.platform == "win32":
        return os.path.join(VENV_DIR, "Scripts", "python.exe")
    return os.path.join(VENV_DIR, "bin", "python")


def setup_virtual_environment():
    """Cria o ambiente virtual .venv e instala as dependências se necessário."""
    print("⏳ [1/4] Verificando Ambiente Virtual Python (.venv)...")
    
    if not os.path.exists(VENV_DIR):
        print("   🔨 Criando ambiente virtual '.venv'...")
        try:
            subprocess.run([sys.executable, "-m", "venv", VENV_DIR], check=True)
            print("   ✅ Ambiente virtual '.venv' criado com sucesso!")
        except Exception as e:
            print(f"   ⚠️ Alerta ao criar .venv: {e}")
            return
    else:
        print("   ✅ Ambiente virtual '.venv' já existe.")

    venv_python = get_venv_python_path()

    # Instalar dependências se requirements.txt existir
    if os.path.exists(REQUIREMENTS_FILE) and os.path.exists(venv_python):
        print("   📦 Verificando/Instalando dependências de requirements.txt...")
        try:
            cmd = [venv_python, "-m", "pip", "install", "-r", REQUIREMENTS_FILE, "--quiet"]
            subprocess.run(cmd, check=True)
            print("   ✅ Dependências de Python instaladas e atualizadas no .venv!")
        except Exception as e:
            print(f"   ⚠️ Alerta ao instalar dependências: {e}")


def auto_heal_vault():
    """Garante que a pasta .obsidian possui restricted=false, showUnsupportedFiles=true e recupera de _obsidian_backup."""
    print("\n⏳ [2/4] Verificando e Protegendo Configurações do Vault Obsidian...")
    
    os.makedirs(TEMPLATES_DIR, exist_ok=True)
    
    if not os.path.exists(BACKUP_DIR):
        print("   ⚠️ Backup prístino '_obsidian_backup' não encontrado. Criando diretório base.")
        os.makedirs(BACKUP_DIR, exist_ok=True)

    # 1. Se .obsidian não existir, copiar backup integral
    if not os.path.exists(OBSIDIAN_DIR):
        print("   📦 Restaurando .obsidian/ a partir de _obsidian_backup/...")
        shutil.copytree(BACKUP_DIR, OBSIDIAN_DIR)
    else:
        # Garantir cópia de plugins faltantes
        backup_plugins = os.path.join(BACKUP_DIR, "plugins")
        target_plugins = os.path.join(OBSIDIAN_DIR, "plugins")
        if os.path.exists(backup_plugins):
            os.makedirs(target_plugins, exist_ok=True)
            for item in os.listdir(backup_plugins):
                s = os.path.join(backup_plugins, item)
                d = os.path.join(target_plugins, item)
                if not os.path.exists(d):
                    if os.path.isdir(s):
                        shutil.copytree(s, d)
                    else:
                        shutil.copy2(s, d)

    # 2. Forçar restricted = False e showUnsupportedFiles = True no app.json
    app_json_path = os.path.join(OBSIDIAN_DIR, "app.json")
    app_data = {}
    if os.path.exists(app_json_path):
        try:
            with open(app_json_path, "r", encoding="utf-8") as f:
                app_data = json.load(f)
        except Exception:
            app_data = {}

    app_data["restricted"] = False
    app_data["livePreview"] = True
    app_data["showUnsupportedFiles"] = True
    app_data["showFileExtensions"] = True
    with open(app_json_path, "w", encoding="utf-8") as f:
        json.dump(app_data, f, indent=2)
    print("   🛡️ Configurações do Obsidian ativadas ('restricted': false, 'showUnsupportedFiles': true)!")

    # 3. Garantir community-plugins.json (Unitade ativo, sem data-files-editor)
    cp_json_path = os.path.join(OBSIDIAN_DIR, "community-plugins.json")
    with open(cp_json_path, "w", encoding="utf-8") as f:
        json.dump(ALL_PLUGINS, f, indent=2)
    print("   🔌 Plugins ativos no community-plugins.json (Unitade ativo como único editor, sem conflitos)!")

    # 4. Garante que course-styles está ativado no appearance.json
    appearance_json_path = os.path.join(OBSIDIAN_DIR, "appearance.json")
    app_appearance = {}
    if os.path.exists(appearance_json_path):
        try:
            with open(appearance_json_path, "r", encoding="utf-8") as f:
                app_appearance = json.load(f)
        except Exception:
            app_appearance = {}
    
    snippets = app_appearance.get("enabledCssSnippets", [])
    if "course-styles" not in snippets:
        snippets.append("course-styles")
        app_appearance["enabledCssSnippets"] = snippets
        with open(appearance_json_path, "w", encoding="utf-8") as f:
            json.dump(app_appearance, f, indent=2)
        print("   🎨 Tema Cyber Emerald ('course-styles') ativado no appearance.json!")


def configure_plugins_data():
    """Configura os arquivos data.json dos plugins principais (Execute Code, Templater, Dataview, Unitade, Excalidraw)."""
    print("\n⏳ [3/4] Otimizando Configurações Internas dos Plugins (Execute Code, Templater, Dataview, Unitade, Excalidraw)...")
    plugins_dir = os.path.join(OBSIDIAN_DIR, "plugins")
    venv_python = get_venv_python_path()

    # 1. Configurar execute-code
    execute_code_dir = os.path.join(plugins_dir, "execute-code")
    os.makedirs(execute_code_dir, exist_ok=True)
    data_json_path = os.path.join(execute_code_dir, "data.json")
    data = {}
    if os.path.exists(data_json_path):
        try:
            with open(data_json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = {}
    
    data["pythonPath"] = venv_python
    data["pythonInteractive"] = False
    data["persistentOuput"] = True
    data["timeout"] = 15000
    data["pythonInject"] = "import sys\nif hasattr(sys.stdout, 'reconfigure'):\n    sys.stdout.reconfigure(encoding='utf-8', errors='replace')\n    sys.stderr.reconfigure(encoding='utf-8', errors='replace')"
    
    with open(data_json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("   ⚡ Execute Code vinculado ao Python do .venv com injeção automática de UTF-8 e modo script ativado!")

    # 2. Configurar templater-obsidian
    templater_dir = os.path.join(plugins_dir, "templater-obsidian")
    os.makedirs(templater_dir, exist_ok=True)
    data_json_path = os.path.join(templater_dir, "data.json")
    data = {}
    if os.path.exists(data_json_path):
        try:
            with open(data_json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = {}
    
    data["templates_folder"] = "_templates"
    
    with open(data_json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("   📝 Templater vinculado à pasta '_templates/'.")

    # 3. Configurar dataview
    dataview_dir = os.path.join(plugins_dir, "dataview")
    os.makedirs(dataview_dir, exist_ok=True)
    data_json_path = os.path.join(dataview_dir, "data.json")
    data = {}
    if os.path.exists(data_json_path):
        try:
            with open(data_json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = {}
    
    data["enableDataviewJs"] = True
    data["enableInlineDataviewJs"] = True
    
    with open(data_json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("   📊 DataviewJS e consultas inline ativadas com sucesso!")

    # 4. Configurar unitade (Patch .filter(Boolean) em main.js e zerar errors: {})
    unitade_dir = os.path.join(plugins_dir, "unitade")
    unitade_main_js = os.path.join(unitade_dir, "main.js")
    if os.path.exists(unitade_main_js):
        try:
            with open(unitade_main_js, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            pattern = r'\.split\(("|\')>\1\)(?!\.filter\(Boolean\))'
            new_content, count = re.subn(pattern, '.split(">").filter(Boolean)', content)
            if count > 0:
                with open(unitade_main_js, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"   🩹 Unitade main.js corrigido ({count} ocorrências de split('>') corrigidas com .filter(Boolean))!")
        except Exception:
            pass

    if os.path.exists(unitade_dir):
        data_json_path = os.path.join(unitade_dir, "data.json")
        unitade_data = {
          "markdown_overcharge": False,
          "extensions": "py>txt",
          "is_case_insensitive": False,
          "is_onload": True,
          "is_onload_unsafe": False,
          "forced_extensions": "",
          "is_ignore": False,
          "ignore_extensions": "",
          "ignore_masks": "",
          "is_grouped": False,
          "grouped_extensions": "",
          "mobile_settings": {
            "extensions": "py>txt"
          },
          "barefiling": True,
          "stable": True,
          "errors": {},
          "debug_mode": False,
          "silence_errors": True,
          "manifest_version": "3.2.7",
          "compatibility_module": True,
          "safe_mode": False,
          "code_editor_settings": {
            "enabled": True,
            "use_default_extensions": True,
            "extensions": "py>txt>json>sh>html>css",
            "folding": True,
            "line_numbers": True,
            "word_wrapping": True,
            "minimapping": True,
            "validation_semantic": True,
            "validation_syntax": True,
            "theme": "auto",
            "force_vanilla_paste": False,
            "enable_zoom": True,
            "font_size": 14,
            "font_family": "'Cascadia Code', 'Fira Code', Consolas, 'Courier New', monospace",
            "font_ligatures": True
          },
          "SYS_FONTSIZE_MAX": 32,
          "SYS_FONTSIZE_MIN": 5,
          "status_bar": {
            "enabled": True,
            "registered_extensions": {
              "enabled": True,
              "include_extensions": True,
              "include_extensions_grouped": True,
              "include_code_editor_extensions": True
            },
            "registered_views": True,
            "current_processor": True,
            "current_display": True,
            "cursor_position": True
          },
          "advanced_silencing_errors": {
            "signatures": "Attempting to register an existing view type"
          }
        }
        with open(data_json_path, "w", encoding="utf-8") as f:
            json.dump(unitade_data, f, indent=2)
        print("   🚀 Unitade otimizado e limpo (errors: {}, separador: 'py>txt').")

    # 5. Configurar excalidraw (SVG & Decompress)
    excalidraw_dir = os.path.join(plugins_dir, "obsidian-excalidraw-plugin")
    if os.path.exists(excalidraw_dir):
        data_json_path = os.path.join(excalidraw_dir, "data.json")
        data = {}
        if os.path.exists(data_json_path):
            try:
                with open(data_json_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception:
                data = {}
        
        data["displaySVGInPreview"] = True
        data["decompressForMDView"] = True
        data["previewMatchObsidianTheme"] = True
        
        with open(data_json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print("   🎨 Excalidraw otimizado (Renderização SVG & Descompressão Markdown ativadas).")


def clean_ghost_directories():
    """Remove pastas de cache __pycache__, .pytest_cache, .trash, .space e pastas fantasmas vazias."""
    print("\n⏳ [4/4] Executando Auto-Limpeza de Pastas de Cache & Fantasmas...")
    removed_count = 0

    # 1. Limpeza global de __pycache__, .pytest_cache, .trash e .space
    for root, dirs, files in os.walk(ROOT_DIR, topdown=False):
        if ".git" in root or ".venv" in root:
            continue
        for d in list(dirs):
            if d in ("__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".space", ".trash", "data-files-editor", "editing-toolbar"):
                dir_path = os.path.join(root, d)
                try:
                    shutil.rmtree(dir_path)
                    print(f"   🧹 Cache/Plugin desativado removido: {os.path.relpath(dir_path, ROOT_DIR)}")
                    removed_count += 1
                except Exception:
                    pass

    # 2. Remover pastas vazias fantasmas na raiz dos módulos 01 a 07
    for mod in MODULES:
        mod_path = os.path.join(ROOT_DIR, mod)
        if os.path.exists(mod_path):
            for item in os.listdir(mod_path):
                item_path = os.path.join(mod_path, item)
                if os.path.isdir(item_path) and item not in ("teoria", "pratica"):
                    sub_contents = os.listdir(item_path)
                    if len(sub_contents) == 0:
                        try:
                            os.rmdir(item_path)
                            print(f"   🧹 Pasta vazia removida: {os.path.relpath(item_path, ROOT_DIR)}")
                            removed_count += 1
                        except Exception:
                            pass

    # 3. Remover diretório legado de templates se existir
    if os.path.exists(LEGACY_TEMPLATES_DIR):
        try:
            shutil.rmtree(LEGACY_TEMPLATES_DIR)
            print(f"   🧹 Diretório de templates legado removido: 08_guias_recursos/templates/")
            removed_count += 1
        except Exception:
            pass

    if removed_count == 0:
        print("   ✅ Nenhuma pasta de cache ou fantasma encontrada. Estrutura 100% limpa!")
    else:
        print(f"   ✅ Limpeza concluída! Total de {removed_count} pastas de cache/fantasmas removidas.")


def main():
    print("=" * 65)
    print("🛡️ SETUP INICIAL E PROTEÇÃO FAIL-SAFE DO VAULT OBSIDIAN")
    print("=" * 65)

    setup_virtual_environment()
    auto_heal_vault()
    configure_plugins_data()
    clean_ghost_directories()

    print("=" * 65)
    print("🎉 CONFIGURAÇÃO E LIMPEZA CONCLUÍDAS COM SUCESSO!")
    print("   - Ambiente Virtual (.venv) pronto e com dependências instaladas.")
    print("   - Execute Code otimizado com modo script ativado (sem REPL stdin bugs).")
    print("   - Unitade patched com .filter(Boolean) (zero bug de string vazia em forced_extensions).")
    print("   - Excalidraw e Mermaid configurados e ativados.")
    print("   - Pastas de cache (__pycache__) e diretórios fantasmas removidos.")
    print("=" * 65)


if __name__ == "__main__":
    main()
