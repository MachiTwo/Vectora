import os


def rename_md_to_pt_md(root_dir):
    """
    Recursively renames all .md files to .pt.md, ignoring .en.md files.
    """
    print(f"Iniciando renomeação em: {root_dir}")

    count = 0
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            # Ignorar arquivos que já são .en.md ou .pt.md
            if file.endswith(".en.md") or file.endswith(".pt.md"):
                continue

            # Processar apenas arquivos .md
            if file.endswith(".md"):
                old_path = os.path.join(root, file)
                # Substituir a extensão .md por .pt.md
                new_file_name = file[:-3] + ".pt.md"
                new_path = os.path.join(root, new_file_name)

                try:
                    os.rename(old_path, new_path)
                    print(f"Renomeado: {file} -> {new_file_name}")
                    count += 1
                except Exception as e:
                    print(f"Erro ao renomear {file}: {e}")

    print(f"\nConcluído! Total de arquivos renomeados: {count}")


if __name__ == "__main__":
    # Caminho padrão para a documentação
    docs_path = os.path.join(os.getcwd(), "docs")
    if os.path.exists(docs_path):
        rename_md_to_pt_md(docs_path)
    else:
        print(f"Erro: O diretório {docs_path} não foi encontrado.")
