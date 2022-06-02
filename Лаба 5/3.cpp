#include <fstream>
using namespace std;

struct Node{
    int key;
    Node *l, *r;
};

bool TreeSearch(Node *x, int k){ /*проверка наличия key в tree*/
    if(x == NULL)
        return false;
    if(x->key == k)
        return true;
    if(k < x->key)
        return TreeSearch(x->l, k);
    else
        return TreeSearch(x->r, k);
}
/*TreeSearch принимает в качестве параметров корень дерева и искомый ключ. 
Для каждого узла функция сравнивает значение его ключа с искомым ключом. 
Если ключи одинаковы, то функция возвращает текущий узел, в противном случае 
функция вызывается рекурсивно для левого или правого поддерева*/

Node *TreeInsert(Node *&x, int a){ /*вставка key в tree*/
    if(x == NULL){ /*x - корень поддерева, а - вставляемый элемент*/*/
        x = new Node;
        x->key = a;
        x->l = x->r = NULL;
    }
    else if (x->key > a)
        TreeInsert(x->l, a);
    else if (x->key < a)
        TreeInsert(x->r, a);
    return x;
}

/*TreeInsert Операция вставки работает аналогично поиску элемента, только при 
обнаружении у элемента отсутствия ребенка нужно подвесить на него 
вставляемый элемент.*/

Node *TreeNext(Node *&root, int x){ /*следующий по значению за key в tree*/
    Node *current = root;
    Node *successor = NULL;
    while(current != NULL){
        if(current->key > x){
            successor = current;
            current = current->l;
        }
        else
            current = current->r;
    }
    return successor;
}

/*TreeNext и TreePrev Поиск будем начинать с корня дерева, храня текущий узел current и узел successor,
 последний посещенный узел, ключ которого больше x.
Спускаемся вниз по дереву, как в алгоритме поиска узла. Рассмотрим ключ текущего узла current.
 Если current.key<=x, значит следующий за x узел находится в правом поддереве (в левом
 поддереве все ключи меньше current.key). 
 Если же x<current.key, то x<next(x)<=current.key, поэтому current может быть следующим для ключа x,
 либо следующий узел содержится в левом поддереве current. 
Перейдем к нужному поддереву и повторим те же самые действия.*/

Node *TreePrev(Node *&root, int x){ /*предыдущий по значению за key в tree*/
    Node *current = root;
    Node *successor = NULL;
    while(current != NULL){
        if(current->key < x){
            successor = current;
            current = current->r;
        }
        else
            current = current->l;
    }
    return successor;
}

Node *TreeMin(Node *&x){ /*минимальный по значению в tree*/
    if(x->l == NULL)
        return x;
    return TreeMin(x->l);
}

Node *TreeMax(Node *&x){ /*максимальный по значению в tree*/
    if(x->r == NULL)
        return x;
    return TreeMax(x->l);
}

Node *TreeDelete(Node *&root, int a){ /*удаление key в tree*/
    if(root == NULL)
        return root;
    if(a < root->key)
        root->l = TreeDelete(root->l, a);
    else if(a > root->key)
        root->r = TreeDelete(root->r, a);
    else if(root->l != NULL && root->r != NULL){
        root->key = TreeMin(root->r)->key;
        root->r = TreeDelete(root->r, root->key);
    }
    else{
        if(root->l != NULL)
            root = root->l;
        else
            root = root->r;
    }
    return root;
}
/*При рекурсивном удалении узла из бинарного дерева нужно рассмотреть 
три случая: удаляемый элемент находится в левом поддереве текущего 
поддерева, удаляемый элемент находится в правом поддереве или удаляемый 
элемент находится в корне. В двух первых случаях нужно рекурсивно удалить 
элемент из нужного поддерева. Если удаляемый элемент находится в корне 
текущего поддерева и имеет два дочерних узла, то нужно заменить его 
минимальным элементом из правого поддерева и рекурсивно удалить этот 
минимальный элемент из правого поддерева. Иначе, если удаляемый элемент 
имеет один дочерний узел, нужно заменить его потомком. Время работы 
алгоритма — O(h). Рекурсивная функция, возвращающая дерево с удаленным 
элементом z:*/

int main() {
    ifstream fin("bstsimple.in");
    ofstream fout("bstsimple.out");
    Node *tree = NULL;
    string command;
    while (fin >> command) {
        int value;
        fin >> value;
        if(command == "insert")
            TreeInsert(tree, value);
        if(command == "exists"){
            if(TreeSearch(tree, value))
                fout << "true\n";
            else
                fout << "false\n";
        }
        if(command == "next"){
            Node *temp = TreeNext(tree, value);
            if(temp == NULL)
                fout << "none\n";
            else
                fout << temp->key << "\n";
        }
        if(command == "prev"){
            Node *temp = TreePrev(tree, value);
            if(temp == NULL)
                fout << "none\n";
            else
                fout << temp->key << "\n";
        }
        if(command == "delete")
            TreeDelete(tree, value);
    }
}