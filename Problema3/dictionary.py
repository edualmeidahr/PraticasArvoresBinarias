import time

class Node:
    def __init__(self, word, definition):
        self.word = word
        self.definition = definition
        self.left = None
        self.right = None
        self.height = 1  # Para balanceamento AVL


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, root, word, definition):
        if not root:
            return Node(word, definition)
        word = word.lower()  # Garantir que todas as palavras sejam minúsculas
        if word < root.word:
            root.left = self.insert(root.left, word, definition)
        elif word > root.word:
            root.right = self.insert(root.right, word, definition)
        else:
            return root  # Palavra já existe

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Rotação LL (Left-Left)
        if balance > 1 and word < root.left.word:
            return self.rotate_right(root)

        # Rotação RR (Right-Right)
        if balance < -1 and word > root.right.word:
            return self.rotate_left(root)

        # Rotação LR (Left-Right)
        if balance > 1 and word > root.left.word:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Rotação RL (Right-Left)
        if balance < -1 and word < root.right.word:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def add_word(self, word, definition):
        start = time.time()
        self.root = self.insert(self.root, word, definition)
        end = time.time()
        # print(f"Tempo para adicionar '{word}': {end - start:.6f} segundos")

    def rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def autocomplete(self, root, prefix):
        if root is None:
            return []
        suggestions = []
        if root.word.startswith(prefix):
            suggestions.append(root.word)
        suggestions += self.autocomplete(root.left, prefix)
        suggestions += self.autocomplete(root.right, prefix)
        return suggestions

    def get_suggestions(self, prefix):
        prefix = prefix.lower()  # Converter o prefixo para minúsculas
        start = time.time()
        suggestions = self.autocomplete(self.root, prefix)
        end = time.time()
        print(f"Tempo para buscar sugestões para '{prefix}': {end - start:.6f} segundos")
        return suggestions

    def search(self, root, word):
        if root is None or root.word == word:
            return root
        word = word.lower()  # Garantir que a palavra seja minúscula para a busca
        if word < root.word:
            return self.search(root.left, word)
        return self.search(root.right, word)

    def find_word(self, word):
        start = time.time()
        node = self.search(self.root, word)
        end = time.time()
        print(f"Tempo para buscar a palavra '{word}': {end - start:.6f} segundos")
        if node:
            return node.definition
        return "Palavra não encontrada."


def load_dictionary_from_file(file_path):
    tree = AVLTree()
    try:
        with open(file_path, "r") as file:
            for line in file:
                if ":" in line:
                    word, definition = line.strip().split(":", 1)
                    tree.add_word(word.strip(), definition.strip())
    except FileNotFoundError:
        print(f"Arquivo dictionary não encontrado. Nenhuma palavra carregada.")
    return tree


def menu():
    file_path = "Problema3/dictionary.txt"
    tree = load_dictionary_from_file(file_path)

    while True:
        print("\nDicionário Eletrônico - Menu")
        print("1. Adicionar uma palavra")
        print("2. Buscar a definição de uma palavra")
        print("3. Obter sugestões (autocompletar)")
        print("4. Sair")

        try:
            choice = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        if choice == 1:
            word = input("Digite a palavra: ").strip().lower()  # Converter para minúsculas
            definition = input("Digite a definição: ").strip()
            tree.add_word(word, definition)
            with open(file_name, "a") as file:
                file.write(f"{word}:{definition}\n")
            print(f"A palavra '{word}' foi adicionada com sucesso!")

        elif choice == 2:
            word = input("Digite a palavra que deseja buscar: ").strip().lower()  # Converter para minúsculas
            definition = tree.find_word(word)
            print(f"Definição: {definition}")

        elif choice == 3:
            prefix = input("Digite o prefixo para obter sugestões: ").strip().lower()  # Converter para minúsculas
            suggestions = tree.get_suggestions(prefix)
            if suggestions:
                print(f"Sugestões: {', '.join(suggestions)}")
            else:
                print("Nenhuma sugestão encontrada para esse prefixo.")

        elif choice == 4:
            print("Encerrando o programa. Até logo!")
            break

        else:
            print("Opção inválida. Por favor, tente novamente.")


# Executa o menu
if __name__ == "__main__":
    menu()
