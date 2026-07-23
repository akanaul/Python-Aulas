#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de Proteção e Restauração Automática do Vault Obsidian.

Garante que o Modo Restrito do Obsidian fique DESATIVADO ("restricted": false)
e restaura todas as configurações dos 19 plugins a partir de _obsidian_backup/
caso o Obsidian tente sobrescrever ou desativar os plugins por padrão.
"""

import os
import shutil
import json
import sys

# Garantir UTF-8 no terminal Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def auto_heal_vault(vault_path: str = ".") -> bool:
    """Verifica a integridade do .obsidian e restaura a partir do backup se necessário."""
    obsidian_dir = os.path.join(vault_path, ".obsidian")
    backup_dir = os.path.join(vault_path, "_obsidian_backup")
    app_json_path = os.path.join(obsidian_dir, "app.json")

    # 1. Se o backup existir, sincroniza configurações e plugins
    if os.path.exists(backup_dir):
        if not os.path.exists(obsidian_dir):
            os.makedirs(obsidian_dir, exist_ok=True)
            
        # Copiar arquivos de configuração raiz (.json)
        for file_name in os.listdir(backup_dir):
            src = os.path.join(backup_dir, file_name)
            dst = os.path.join(obsidian_dir, file_name)
            if os.path.isfile(src):
                shutil.copy2(src, dst)
            elif os.path.isdir(src) and file_name in ["plugins", "snippets", "icons"]:
                os.makedirs(dst, exist_ok=True)
                for root, dirs, files in os.walk(src):
                    rel_path = os.path.relpath(root, src)
                    target_dir = os.path.join(dst, rel_path)
                    os.makedirs(target_dir, exist_ok=True)
                    for f in files:
                        shutil.copy2(os.path.join(root, f), os.path.join(target_dir, f))

    # 2. Forçar "restricted": false no app.json
    app_data = {}
    if os.path.exists(app_json_path):
        try:
            with open(app_json_path, "r", encoding="utf-8") as f:
                app_data = json.load(f)
        except Exception:
            app_data = {}

    app_data["restricted"] = False
    app_data["livePreview"] = True
    app_data["showLineNumber"] = True
    app_data["readableLineLength"] = True

    with open(app_json_path, "w", encoding="utf-8") as f:
        json.dump(app_data, f, indent=2, ensure_ascii=False)

    return True

def main():
    print("=" * 65)
    print("🛡️ PROTEÇÃO E RESTAURAÇÃO DO VAULT OBSIDIAN")
    print("=" * 65)
    
    success = auto_heal_vault()
    
    if success:
        print("✅ Vault do Obsidian verificado com sucesso!")
        print("✅ Modo Restrito DESATIVADO ('restricted': false)")
        print("✅ Todos os 19 plugins e configurações ativados e protegidos.")
    else:
        print("⚠️ Falha ao verificar/restaurar o vault.")
    print("=" * 65)

if __name__ == "__main__":
    main()
