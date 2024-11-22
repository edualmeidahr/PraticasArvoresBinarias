# Classe para nó de árvore binária (inclui chave e filhos)
class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Inserção na árvore binária (sem balanceamento)
def insert(node, key):
    if node is None:
        return BinaryTree(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

# Remoção na árvore binária (caso simples para simplificação)
def delete(node, key):
    if node is None:
        return node
    if key < node.key:
        node.left = delete(node.left, key)
    elif key > node.key:
        node.right = delete(node.right, key)
    else:
        # Caso de nó folha ou com um único filho
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        # Caso de dois filhos: encontra o sucessor in-ordem
        temp = find_min(node.right)
        node.key = temp.key
        node.right = delete(node.right, temp.key)
    return node

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# Função para calcular o nível máximo
def calculate_max_level(node):
    if node is None:
        return 0
    left_depth = calculate_max_level(node.left)
    right_depth = calculate_max_level(node.right)
    return max(left_depth, right_depth) + 1

# Função para encontrar o caminho mais longo
def find_longest_path(node):
    if node is None:
        return []
    
    # Caminhos do lado esquerdo e direito
    left_path = find_longest_path(node.left)
    right_path = find_longest_path(node.right)
    
    # Retorna o caminho mais longo, adicionando o nó atual
    if len(left_path) > len(right_path):
        return [node.key] + left_path
    else:
        return [node.key] + right_path

# Função para exibir a árvore em ordem
def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.key)
        print_tree(node.left, level + 1)

# Simulação com operações desbalanceadas
root = None
operations = [("insert", 1), ("insert", 2), ("insert", 3), ("insert", 4),
              ("insert", 5), ("insert", 6), ("insert", 7)]

for op, value in operations:
    if op == "insert":
        root = insert(root, value)
        print(f"Após inserir {value}:")
    elif op == "delete":
        root = delete(root, value)
        print(f"Após remover {value}:")
    
    print_tree(root)
    max_level = calculate_max_level(root)
    longest_path = find_longest_path(root)
    print(f"Nível máximo atual: {max_level}")
    print(f"Caminho mais longo: {longest_path}\n")

# Simulação com operações mais balanceadas
root = None
operations1 = [("insert", 4), ("insert", 2), ("insert", 5), ("insert", 1),
               ("insert", 7), ("insert", 6), ("insert", 3)]

for op, value in operations1:
    if op == "insert":
        root = insert(root, value)
        print(f"Após inserir {value}:")
    elif op == "delete":
        root = delete(root, value)
        print(f"Após remover {value}:")
    
    print_tree(root)
    max_level = calculate_max_level(root)
    longest_path = find_longest_path(root)
    print(f"Nível máximo atual: {max_level}")
print(f"Caminho mais longo: {longest_path}\n")
