import subprocess
import sys
from pathlib import Path

# Prefixos reservados pelo GitHub que não podem ser criados/sobrescritos
RESERVED_PREFIXES = ("GITHUB_", "ACTIONS_", "RUNNER_")


def parse_env(file_path):
    """Le arquivo .env e retorna dicionario de variaveis."""
    env_vars = {}

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            # Ignora comentarios e linhas vazias
            if not line or line.startswith("#"):
                continue

            if "=" not in line:
                continue

            key, value = line.split("=", 1)
            key = key.strip()

            # Remove aspas se houver
            value = value.strip().strip('"').strip("'")

            # Ignora valores vazios
            if not value:
                print(f"[AVISO] Valor vazio para {key}, ignorando")
                continue

            env_vars[key] = value

    return env_vars


def is_reserved_secret(key):
    """Verifica se a chave e um prefixo reservado pelo GitHub."""
    return key.startswith(RESERVED_PREFIXES)


def set_github_secret(key, value, extra_args=None):
    """Envia uma variavel como GitHub secret."""
    # Pass value via stdin to avoid exposing it in process list or error output
    cmd = ["gh", "secret", "set", key]

    if extra_args:
        cmd.extend(extra_args)

    try:
        subprocess.run(cmd, input=value.encode(), check=True, capture_output=True)
        print(f"[OK] {key} enviado")
        return True
    except subprocess.CalledProcessError as e:
        # Do not log stderr or secret identifiers in clear text
        print(f"[ERRO] Falha ao enviar secret (codigo: {e.returncode})")
        return False
    except FileNotFoundError:
        print("[ERRO] GitHub CLI (gh) nao encontrado. Instale com: brew install gh")
        return False


def main():
    if len(sys.argv) < 2:
        print("Uso: python script.py .env [--env production | --org minha-org]")
        sys.exit(1)

    env_file = Path(sys.argv[1])

    if not env_file.exists():
        print(f"[ERRO] Arquivo nao encontrado: {env_file}")
        sys.exit(1)

    extra_args = sys.argv[2:] if len(sys.argv) > 2 else []

    env_vars = parse_env(env_file)

    if not env_vars:
        print("[AVISO] Nenhuma variavel valida encontrada")
        sys.exit(0)

    # Filtra e avisa sobre secrets reservados
    secrets_to_send = {}
    for key, value in env_vars.items():
        if is_reserved_secret(key):
            print(f"[AVISO] {key} ignorado (prefixo reservado pelo GitHub)")
        else:
            secrets_to_send[key] = value

    if not secrets_to_send:
        print("[AVISO] Nenhum secret valido para enviar")
        sys.exit(0)

    # Pede confirmacao
    print(f"\n{len(secrets_to_send)} secret(s) sera(o) enviado(s):")
    for key in sorted(secrets_to_send.keys()):
        print(f"  - {key}")

    response = input("\nContinuar? (s/n): ").strip().lower()
    if response != "s":
        print("Operacao cancelada")
        sys.exit(0)

    # Envia secrets
    print()
    success = 0
    failed = 0

    for key, value in secrets_to_send.items():
        if set_github_secret(key, value, extra_args):
            success += 1
        else:
            failed += 1

    # Resumo
    print(f"\n{success} sucesso, {failed} falha(s)")

    if failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
