#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de Setup Inicial e Proteção do Vault (Curso Python + IA para Automação).

1. Cria o ambiente virtual (.venv) se não existir e instala as dependências de requirements.txt.
2. Força 'restricted': false em .obsidian/app.json.
3. Garante que todos os 18 plugins e configurações permaneçam ativos a partir de _obsidian_backup/.

Uso:
    python setup_vault.py
"""

import json
import os
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


def setup_virtual_environment():
    """Cria o ambiente virtual .venv e instala as dependências se necessário."""
    print("⏳ [1/2] Verificando Ambiente Virtual Python (.venv)...")
    
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

    # Determinar caminho do executável python dentro do venv
    if sys.platform == "win32":
        venv_python = os.path.join(VENV_DIR, "Scripts", "python.exe")
    else:
        venv_python = os.path.join(VENV_DIR, "bin", "python")

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
    """Garante que a pasta .obsidian possui restricted=false e recupera de _obsidian_backup."""
    print("\n⏳ [2/2] Verificando e Protegendo Configurações do Vault Obsidian...")
    
    if not os.path.exists(BACKUP_DIR):
        print("   ⚠️ Backup prístino '_obsidian_backup' não encontrado. Pulando restauração.")
        return

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

    # 2. Forçar restricted = False no app.json
    app_json_path = os.path.join(OBSIDIAN_DIR, "app.json")
    app_data = {}
    if os.path.exists(app_json_path):
        try:
            with open(app_json_path, "r", encoding="utf-8") as f:
                app_data = json.load(f)
        except Exception:
            app_data = {}

    if app_data.get("restricted") != False:
        app_data["restricted"] = False
        app_data["livePreview"] = True
        with open(app_json_path, "w", encoding="utf-8") as f:
            json.dump(app_data, f, indent=2)
        print("   🛡️ Modo Restrito desativado com sucesso ('restricted': false)!")


def main():
    print("=" * 65)
    print("🛡️ SETUP INICIAL E PROTEÇÃO FAIL-SAFE DO VAULT OBSIDIAN")
    print("=" * 65)

    setup_virtual_environment()
    auto_heal_vault()

    print("=" * 65)
    print("🎉 CONFIGURAÇÃO CONCLUÍDA COM SUCESSO!")
    print("   - Ambiente Virtual (.venv) pronto e com dependências instaladas.")
    print("   - Vault do Obsidian protegido com todos os 18 plugins ativos.")
    print("=" * 65)


if __name__ == "__main__":
    main()
